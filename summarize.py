# TODO: Remove unsused libraries and finctions

# for scraping the webpage
from newspaper import Article

# for tokenizing the text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# for stemming
from nltk.stem import PorterStemmer

# for removing square brackets
import re

# Gensim summarizer
from gensim.summarization.summarizer import summarize

# downloads the article and parses the html, uses lxml parser
def downloadwebpage(url):
    # downloads the whole webpage
    article = Article(url)
    article.download()

    # parses the downloaded html
    article.parse()
    text = article.text
    return text

# split a paragraph into sentences.


def splitToSentences(content):
    # tokenizes each of the sentences
    return sent_tokenize(content)

# split text into paragraphs
def splitToParagraphs(content):
    # splits the sentences from new line and returns ones which have length greater than 0
    return [c for c in content.split("\n") if len(c) is not 0]

# stem and remove any stop words form a sentence


def removeStopwords(sentence):
    s = word_tokenize(sentence)

    # removes english stopwords from sentence (nltk corpus)
    s = [w for w in s if not w in stopwords.words('english')]

    # uses nltk's porter stemmer to stem the sentences

    stemmer = PorterStemmer()
    s = [stemmer.stem(word) for word in s]
    return s


def sum_it_up(content):
    # remove the reference numbers
    re.sub(r'\[.+\]','',content)

    # computes summary
    print(summarize(content))


def main():
    # TODO: remove static url and take input from user
    url = 'https://en.wikipedia.org/wiki/Elon_Musk'

    content = downloadwebpage(url)

    sum_it_up(content)


if __name__ == "__main__":
    main()
