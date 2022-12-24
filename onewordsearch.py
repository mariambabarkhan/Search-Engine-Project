#barrels + docIndex (need to be done b4)
#filenum?

#COMPLETE lexicon, fwd and inverted index files for dataset
#query: one word
#get titleIDs from titleLex->docID from invertedtitle->hitlist from fwdidnex
#get wordID from lexicon->docID from inverted index->hitlist from fwdIndex 
#ranking function:
#gets 2 list: docIDs and their hitlists for content AND title, compares and sorts docs in order of relevance

import json

def sorting(totalHitsTitle,totalHits): #will return sorted list of docs according to relevance!
    #templist: {docID:maxhit, docID:maxhits, docID:maxhits},
    titledocs = sorted(totalHitsTitle.items(), key=lambda i:i[1], reverse=True) #returns a list of tuples
    print("Title hits: ")
    for i in titledocs:
        print(i[0], end=" ")
    print("\n")
    contentdocs = sorted(totalHits.items(), key=lambda i:i[1], reverse=True) #returns a list of tuples
    print("Content hits:")
    for i in contentdocs:
        print(i[0], end=" ")
    
def searching(input): #assuming input = a ONE WORD query
    #Checking in Title Lex first:
    input = input.lower()
    tf = open("E:\indexfiles\ztitlelexFinal.json")
    data = json.load(tf)
    if data.get(input) is None:
        print("idher")
        titleID=-1
    else:
        titleID = str(data.get(input))
        tf.close()

        f = open("E:\indexfiles\invertedIndexTitleFinal.json")
        data = json.load(f)
        titledoclist = data.get(titleID) #LIST OF DOCS THAT HAVE WORD IN TITLE
        f.close()

    #Checking in Content Lex:           #word appears in content of doc, but not in title
    f = open("E:\indexfiles\lexiconFinal.json")
    data = json.load(f)
    if data.get(input) is None:
        contentID = -1
    else:
        contentID = str(data.get(input))
        f.close()

        f = open("E:\indexfiles\invertedIndexContentFinal.json")
        data = json.load(f)
        contentdoclist = data.get(contentID) #LIST OF DOCS where word is in content
        f.close()

        f = open("E:\indexfiles\zfwdIndexContentFinal.json")
        data = json.load(f)
        totalHits = {}
        totalHitsTitle = {}

        if titleID!=-1:
            for i in titledoclist: #sorting title hits docs based on frequency of word in content
                if data.get(str(i)).get(str(titleID)) is not None:
                    maxhits = data.get(str(i)).get(str(titleID))[-1]
                    totalHitsTitle.update({i:maxhits}) #docID:maxhits
                    print(i, "title hits:", maxhits, end=" ")

            for i in contentdoclist:
                if(i in titledoclist): #excluding docs already catered in titlehits
                    pass
                else:
                    maxhits = data.get(str(i)).get(contentID)[-1]
                    totalHits.update({i:maxhits}) #docID:maxhits
                    print(i, "content hits:", maxhits, end=" ")

        else:
            for i in contentdoclist:
                maxhits = data.get(str(i)).get(contentID)[-1]
                totalHits.update({i:maxhits}) #docID:maxhits
    #sorting(totalHitsTitle, totalHits)

searching("trump")
