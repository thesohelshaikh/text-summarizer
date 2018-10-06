# for scraping the webpage
from newspaper import Article

# for tokenizing the text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# for stemming
from nltk.stem import PorterStemmer

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
    # TODO: look for better stemmer
    stemmer = PorterStemmer()
    s = [stemmer.stem(word) for word in s]
    return s

def summarize(content):
    paragraphs = splitToParagraphs(content)
    sentences = []
    
    for p in paragraphs:
        s = splitToSentences(p) 
        for x in s:
            sentences.append(x)
    
    cleanedSentences = [removeStopwords(x) for x in sentences]
    print(cleanedSentences)

def main():
    url = 'https://en.wikipedia.org/wiki/Elon_Musk' # TODO: remove static url and take input from user
    content = downloadwebpage(url)

    summarize(content)


if __name__== "__main__":
    main()