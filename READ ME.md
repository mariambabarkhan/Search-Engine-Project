# Search-Engine-Project

FOR INDEXING YOUR DATASET:

This code is a search engine that takes a set of articles and processes them to create a lexicon, forward index, and inverted index for both the content 
and titles of the articles. The user can then search for a specific query and the search engine will return the relevant articles ranked by their relevance 
to the query.The code begins by importing a number of necessary libraries, including json, re, math, time, SnowballStemmer, and Tkinter. It also sets up a 
SnowballStemmer object for use in stemming words later on.The code then defines several global variables, including docID, titleID, and wordID, which are used
to assign unique IDs to documents, titles, and words, respectively. It also defines a number of dictionaries, including lexicon for storing the lexicon of the 
article content, titlelex for storing the lexicon of the article titles, fwdIndexContent and fwdIndexTitle for storing the forward indices of the article content
and titles, respectively, and invertedIndexContent and invertedIndexTitle for storing the inverted indices of the article content and titles, respectively.
The code also defines a set of stop words and a stopwords_dict for storing them.The code then defines a number of functions. The first, stemming(wordlist),
takes a list of words and returns a new list with each word stemmed using the SnowballStemmer object defined earlier. The tokenize(dict, name) function takes a 
dictionary and a string representing whether the input is the content or title of an article, and returns a list of tokens after tokenizing the input, removing 
stop words, and stemming the remaining words. The createlexicon(wordlist, name) function takes a list of words and a string representing whether the input is
the content or title of an article, and creates a lexicon by adding each unique word in the input to the appropriate lexicon dictionary with a unique ID. The 
createFwdIndex(content, name) function takes a list of words and a string representing whether the input is the content or title of an article, and creates a 
forward index by storing the position of each word in the input along with its unique ID in a dictionary. The createInvertedIndex(name) function takes a string 
representing whether the input is the content or title of an article, and creates an inverted index by storing the list of documents that contain each unique word 
in the appropriate inverted index dictionary with the word's unique ID as the key.The code then defines a window object using Tkinter and sets various
properties of the window, including its title and dimensions. It also defines a number of Tkinter objects for use in creating a user interface. The code then
enters a main loop, waiting for user input. When a user enters a search query, the code processes the query using the functions defined earlier and returns the
relevant articles ranked by their relevance to the query.

FOR SEARCHING QUERIES AND GENERATING GUI:

Search Engine "GBW - GOOGLE BUT WORSE"
This search engine allows users to input a query and returns a list of relevant documents.
The search engine is case-insensitive and ignores punctuation and numbers in the query. It also stems the query words before searching, so it will return 
results for words with the same stem as the query words.

Features
Stemming: The search engine uses the Snowball stemmer to stem the query words before searching. This means that it will return results for words 
with the same stem as the query words. For example, a search for "running" will also return results for "ran," "runs," etc.
Ranking: The search engine ranks the results based on the term frequency-inverse document frequency (TF-IDF) of the query words in the document. 
It also gives a higher rank to documents that have the query words in their titles.

Usage
To use the search engine, call the search function with a string as the argument. This string should be the query that you want to search for.
search("example query")
This will return a list of documents that are relevant to the query "example query." The list will be sorted by the rank of each document,
with the highest ranked documents appearing first.

You can access the list of results by using the resultList variable. For example:
search("example query")
print(resultList)
This will print the list of results to the console. The list will include the number of results found, followed by the title and URL of each relevant document.

Dependencies
json
re
math
time
nltk
tkinter
shutil
