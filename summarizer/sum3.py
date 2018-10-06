# -*- coding: utf-8 -*-


import re
import numpy as np
from goose import Goose
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem.snowball import *
from nltk.tokenize import word_tokenize, sent_tokenize
import sys


title = ''
# split a paragraph into sentences.
def splitToSentences(content):
    return sent_tokenize(content)
   
# split text into paragraphs
def splitToParagraphs(content):
    return [c for c in content.split("\n") if len(c) is not 0]
      
# get the intersection between two sentences
def getIntersection(s1, s2):
    global title
    s1 = set(s1)
    s2 = set(s2)
    s3 = set(title)
    
    # if the sentences are empty the rank of this will be 0
    if (len(s1) + len(s2)) == 0:
        return 0
    
    # returning the score of the sentence s1 wrt s2
    return len(s1 & s2 & s3)/((len(s1) + len(s2))/2)
    
# create a key for an object from a sentence
def sentenceKey(sentence):
    sentence = re.sub(r'\W+', '', sentence)
    return sentence

# stem and remove any stop words form a sentence
def stemAndRemoveStopWords(sentence, stemmer):  
    s = word_tokenize(sentence)
    s = [w for w in s if not w in stopwords.words('english')]
    s = [stemmer.stem(word) for word in s]
    return s

def rankSentences(content):
    # create a list of all sentences
    paragraphs = splitToParagraphs(content)

    # sentences = splitToSentences(content)
    sentences = []
    
    for p in paragraphs:
        s = splitToSentences(p) 
        for x in s:
            sentences.append(x)
        
    n = len(sentences)
    
    # stem and remove stopwords
    stemmer = PorterStemmer()
    # stemmer = SnowballStemmer("english")
    cleanedSentences = [stemAndRemoveStopWords(x, stemmer) for x in sentences]
    
    # Create the sentence adjacency matrix
    values = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            values[i][j] = getIntersection(cleanedSentences[i], cleanedSentences[j])
    
    # create sentence adjacency matrix
    values = np.dot(values, (np.ones((n,n)) - np.eye(n)))
    score = np.sum(values, axis=1)
    sentenceDictionary = {sentenceKey(sentences[i]):score[i] for i in range(n)}
    thresholdScore = np.mean(score) + 0.3*np.std(score)
    return sentenceDictionary, thresholdScore


# get the best sentence from each paragraph
def getBestSentences(paragraph, sentenceDictionary, thresholdScore):
    sentences = splitToSentences(paragraph)
    
    bestSentence = ""
    maxScore = 0
    
    # loop through each sentence and find it its value 
    for s in sentences:
        key = sentenceKey(s)
        if key:
            if sentenceDictionary[key] >= thresholdScore:
                bestSentence += " " + s
    # for s in sentences:
    #     key = sentenceKey(s)
    #     if key:
    #         if sentenceDictionary[key] > maxScore:
    #             maxScore = sentenceDictionary[key]
    #             bestSentence = s
    
    return bestSentence
    
    
    
# summarize the text    
def summarize(content, sentenceDictionary, thresholdScore):
    global title
    paragraphs = splitToParagraphs(content)
    
    summary = []
    
    if title:
        summary.append(title.strip())
        summary.append("")
    
    for p in paragraphs:
        sentence = getBestSentences(p, sentenceDictionary, thresholdScore).strip()
        if sentence:
            summary.append(sentence)
    
    return ("\n").join(summary)
    

# Summarize the content
def doSummary(content): 
    sentenceDictionary, thresholdScore = rankSentences(content)  
    summary = summarize(content, sentenceDictionary, thresholdScore)
    return summary

# using the Goose library to extract the content of a url
def getContent(url):    
    g = Goose()
    article = g.extract(url=url)
    
    return article.title, article.cleaned_text

# grab the content of a url and return a summarized version of it
def parseWebpage(url):
    global title
    pat = ['\[(.*?)\]', '[\n\s].*([0-9]+[.][^0-9])', '[\n\s].*([^a-zA-Z][a-z][/)])']
    # reps = [('\xe2\x80\x93','-')]
    title, content = getContent(url)
    for pattern in pat:
        content =   re.sub(pattern, "", content)
    # for rep in reps:
    #     content = re.sub(rep[0],rep[1],content)
    print("Original text size: ",len(content))
    return doSummary(content)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        # url = "https://medium.com/war-is-boring/one-easy-way-to-blow-7-6-billion-10b0933124f5"
        url = "http://en.wikipedia.org/wiki/Github"

    summary = parseWebpage(url)
    print("Summarized word size:%d\n" % len(summary))
    print(summary.encode('UTF-8'))
