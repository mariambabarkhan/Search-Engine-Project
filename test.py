import os
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

from nltk.stem import WordNetLemmatizer

tokens = [] #for tokenized words

stop_words = stopwords.words('english') #stop words to be removed
withoutStopWords = [] #after removing stop words


current = os.listdir('E:\dataset')
for file in current: #iterates through all files in data set
    with open(os.path.join('E:\dataset', file), 'r') as f: #opens each file
        data = json.load(f)
        for i in data:
            tokens.append(word_tokenize(i["content"])) #each file tokenized

for word in tokens:
    if (word.isalnum() and word.casefold() not in stop_words):
        withoutStopWords.append(word)
        
print(withoutStopWords)



