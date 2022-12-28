import json
import re
import math


file1 = open("E:\check\lexiconFinal.json")
lex = json.load(file1)

file2 = open("E:\check\invertedIndexContentFinal.json")
invIndex = json.load(file2)

file3 =  open("E:\check\zfwdIndexContentFinal.json")
fwdIndex = json.load(file3)

file4 = open("E:\check\docIndexFinal.json")
docIndex = json.load(file4)

docScores = {}

# def onewordsearch(input): #assuming input = a ONE WORD query
#     #Checking in Title Lex first:
#     if titleLex.get(input) is None:
#         titleID=-1
#         print(titleID)
#     else:
#         titleID = str(titleLex.get(input))
#         print(titleID)

#         titledoclist = invIndexTitle.get(titleID) #LIST OF DOCS THAT HAVE WORD IN TITLE
#         #print("titledocs:", titledoclist)

#     #Checking in Content Lex:           #word appears in content of doc, but not in title
#     if lex.get(input) is None:
#         contentID = -1
#     else:
#         contentID = str(lex.get(input))

#         contentdoclist = invIndex.get(contentID) #LIST OF DOCS where word is in content
#         #print("content docs:", contentdoclist)
#         totalHits = {}
#         totalHitsTitle = {}

#         if titleID!=-1:
#             for i in titledoclist: #sorting title hits docs based on frequency of word in content
#                 if fwdIndex.get(str(i)).get(str(contentID)) is not None:
#                     maxhits = fwdIndex.get(str(i)).get(str(contentID))[-1]
#                     #print("maxhits:", maxhits)
#                     totalHitsTitle.update({i:maxhits}) #docID:maxhits

#             for i in contentdoclist:
#                 if(i in titledoclist): #excluding docs already catered in titlehits
#                     pass
#                 else:
#                     if fwdIndex.get(str(i)).get(str(contentID)) is not None:
#                         maxhits = fwdIndex.get(str(i)).get(contentID)[-1]
#                         #print("maxhits:2", maxhits)
#                         totalHits.update({i:maxhits}) #docID:maxhits
#                         #print(i, "content hits:", maxhits, end=" ")

#         else:
#             if contentID!=-1:
#                 for i in contentdoclist:
#                     maxhits = fwdIndex.get(str(i)).get(contentID)[-1] #gets total occurences of word 
#                     totalHits.update({i:maxhits}) #docID:maxhits each doc: max hits
#             else:
#                 pass
#                 #do smth
#     sorting(totalHitsTitle, totalHits)

def search(input):
    querydocs = []
    input = input.lower()
    input = re.sub("[^\w\s]", "", input)
    
    print(input)
    wordlist = input.split(" ")

    # if len(wordlist)==1:
    #     onewordsearch(wordlist[0])
    # else:
    for i in wordlist:
        if lex.get(i) is None:
            ID=-1
        else:
            ID = str(lex.get(i)) #getting ID from lexicon
            doclist = invIndex.get(ID) #LIST OF DOCS THAT HAVE WORD
            querydocs.append(doclist)
            getRank(doclist, ID)
    #linearmerge(querydocs[0], querydocs[1], wordlist)
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
        termfreq = (fwdIndex.get(str(i)).get(ID)[-1])/(totalwords) #*need to divide by total num of words in doc
        idf = math.log((totaldoc/termdoc))
        tfidf = termfreq*idf
        if docScores.get(i) is not None: 
            docScores[i]+=tfidf
        else:
            docScores.update({i:tfidf})


#THSI SORTING FUNCTION IS NOT NEEDED ANYMORE :I GUESS
def sorting(totalHitsTitle,totalHits): #sorteing for ONE WORD query

    #sort dict in descending order of hits
    total = len(totalHitsTitle) + len(totalHits)
    print(total, "results found.")

    titledocs = sorted(totalHitsTitle.items(), key=lambda i:i[1], reverse=True) #returns a list of tuples
    print("Relevant documents:")
    for i in titledocs:
        print(docIndex.get(str(i[0]))[1])
        print(docIndex.get(str(i[0]))[0])
        print("\n")

    print("\n")
    
    contentdocs = sorted(totalHits.items(), key=lambda i:i[1], reverse=True) #returns a list of tuples
    for i in contentdocs:
        print(docIndex.get(str(i[0]))[1])
        print(docIndex.get(str(i[0]))[0])
        print("\n")
    

#get wordID->get doclist->get hits in doc
#calculate tf-idf for each doc
#repeat for each word in query
#results: {docID:tf-idf score} for each word? 
#if docIDs same-> print first ig 




def linearmerge(list1, list2,wordlist):
    i, j = 0
    result = []
    while i>len(list1) and j>len(list2):
        if(list1[i]>list2[j]):
            j+=1
        elif(list2[j]>list1[i]):
            i+=1
        else:
            result.append(list1[i])
    
    finalmatch = [] #will contain all documents with phrase matched!
    for i in result:
        pos1 = fwdIndex.get(str(result[i])).get(wordlist[0])
        pos2 = fwdIndex.get(str(result[i])).get(wordlist[1])
        k, l = 0
        while k>len(pos1) and l>len(pos2):
            if (abs(pos1[k]-pos2[j])==1):
                finalmatch.append(result[i])
                break
            else:
                if(pos1[k]>=pos2[l]):
                    l+=1
                else:
                    k+=1
    return finalmatch

#FINAL MATCH WILL CONTAIN all the documents with phrase matching (aik dafa run ker k check kerleina)
#so make function which will compare finalmatch to docScores (which will have dictioanry of docs ranked according to 
# tf-idf, by pageRank)


    
search("donald")
