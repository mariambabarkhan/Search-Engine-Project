import json
import re
import math
import time
from nltk.stem.snowball import SnowballStemmer


snow_stemmer = SnowballStemmer(language='english')


file1 = open("E:\indexfilesfinal\lexiconFinal.json")
lex = json.load(file1)

file2 = open("E:\indexfilesfinal\invertedIndexContentFinal.json")
invIndex = json.load(file2)

file3 =  open("E:\indexfilesfinal\\fwdIndexContentFinal.json")
fwdIndex = json.load(file3)

file4 = open("E:\indexfilesfinal\docIndexFinal.json")
docIndex = json.load(file4)

file4 = open("E:\indexfilesfinal\\titlelexFinal.json")
titlelex = json.load(file4)

file4 = open("E:\indexfilesfinal\\fwdIndexTitleFinal.json")
titlefwd = json.load(file4)

file4 = open("E:\indexfilesfinal\invertedIndexTitleFinal.json")
titleinv = json.load(file4)

docScores = {}


def titlesearch(wordlist):
    for i in wordlist:
        if titlelex.get(i) is not None:
            ID = str(titlelex.get(i)) #getting ID from lexicon
            doclist = titleinv.get(ID) #LIST OF DOCS THAT HAVE WORD IN TITLE
    for i in doclist:
        docScores.update({i:1})


def search(input):
    querydocs = []
    input = input.lower()
    input = re.sub("[^\w\s]", "", input)

    
    wordlist = input.split(" ")
    wordsfinal = []
    for word in wordlist:
        wordsfinal.append(snow_stemmer.stem(word))
    
    titlesearch(wordsfinal)
    
    for i in wordsfinal:
        if lex.get(i) is None:
            ID=-1
        else:
            ID = str(lex.get(i)) #getting ID from lexicon
            doclist = invIndex.get(ID) #LIST OF DOCS THAT HAVE WORD
            querydocs.append(doclist)
            getRank(doclist, ID)
    sortingdocs()

def sortingdocs(): #sorting docs for multiple word query
    finaldocs = sorted(docScores.items(), key=lambda i:i[1], reverse=True)
    print(len(finaldocs), "results found")
    for i in finaldocs:
        print(docIndex.get(str(i[0]))[1])
        print(docIndex.get(str(i[0]))[0])
        print("\n")

def getRank(doclist, ID):
    global docScores
    termdoc = len(doclist)
    totaldoc = len(fwdIndex)
    for i in doclist:
        totalwords = len(fwdIndex.get(str(i)))
        termfreq = (fwdIndex.get(str(i)).get(ID))/(totalwords) #*need to divide by total num of words in doc
        idf = math.log((totaldoc/termdoc))
        tfidf = termfreq*idf
        if docScores.get(i) is not None: 
            docScores[i]+=tfidf
        else:
            docScores.update({i:tfidf})

start = time.time()    
search("usa afghanistan")
print("time:", time.time()-start)
