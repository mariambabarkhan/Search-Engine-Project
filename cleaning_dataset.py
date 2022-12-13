import json 
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.corpus import wordnet

# from nltk.stem import WordNetLemmatizer
# from nltk.stem.snowball import SnowballStemmer 


data = open('final.txt')
#data = json.load(file) #returns a list(of dictionaries?)

# tokens = [] #for tokenized words
# withoutStopWords = []

# lemm = WordNetLemmatizer()

# stop_words = stopwords.words('english') 

# for i in data:
#     tokens.append(word_tokenize(i["content"]))


# for word in tokens:
#     for j in word:
#         if (j.isalnum() and j.casefold() not in stop_words):
#             withoutStopWords.append(j)



# withoutStopWords = nltk.pos_tag(withoutStopWords) #part of speech tags added

# finalWords=[]

# for word in withoutStopWords:
#     if(word[1].startswith('J')):
#         pos = wordnet.ADJ
#     elif(word[1].startswith('V')):
#         pos = wordnet.VERB
#     elif(word[1].startswith('R')):
#         pos = wordnet.ADV
#     else:
#         pos = wordnet.NOUN
#     finalWords.append(lemm.lemmatize(word[0], pos))

#final words: complete list of words in file

lexicon = {}
id=0

with open('final.txt', 'r', encoding='utf-8') as file:
    for line in file:
        for word in line.split():
            if(word in lexicon):
                pass
            else:
                lexicon.update({word:id})
                id+=1
            

# for i in finalWords:
#     if(i in lexicon):
#         pass
#     else:
#         lexicon.update({i:id})
#         id+=1


json_object = json.dumps(lexicon)

with open("finallexicon.json", "w", encoding='utf-8') as finalfile:
    finalfile.write(json_object)


# file1 = open("final.txt", "a", encoding='utf-8')

# for word in finalWords:
#     word=word.lower()
#     file1.write(word)
#     file1.write(" ")


    




