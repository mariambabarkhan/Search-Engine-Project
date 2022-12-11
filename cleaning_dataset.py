import json 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer 


file = open('pbs.json')
data = json.load(file) #returns a list(of dictionaries?)

tokens = [] #for tokenized words
withoutStopWords = []

lemm = WordNetLemmatizer()

stop_words = stopwords.words('english') 

for i in data:
    tokens.append(word_tokenize(i["content"]))


for word in tokens:
    for j in word:
        if (j.isalnum() and j.casefold() not in stop_words):
            withoutStopWords.append(j)



withoutStopWords = nltk.pos_tag(withoutStopWords) #part of speech tags added

finalWords=[]

snow_stemmer = SnowballStemmer(language='english')

for word in withoutStopWords:
    if(word[1].startswith('J')):
        pos = wordnet.ADJ
    elif(word[1].startswith('V')):
        pos = wordnet.VERB
    elif(word[1].startswith('R')):
        pos = wordnet.ADV
    else:
        pos = wordnet.NOUN
    finalWords.append(lemm.lemmatize(word[0], pos))

file1 = open("final.txt", "a", encoding='utf-8')

for word in finalWords:
    word=word.lower()
    file1.write(word)
    file1.write(" ")


