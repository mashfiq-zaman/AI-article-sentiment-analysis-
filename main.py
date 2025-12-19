from textblob import TextBlob
from newspaper import Article

# with open('mytext.txt', 'r') as f:
#     text=f.read()

url ="https://www.dhakatribune.com/bangladesh/politics/398873/what-is-known-about-hadi%E2%80%99s-physical-condition"
article = Article(url)

article.download()
article.parse()
article.nlp()

text=article.summary #whole text w/o html
print(text)

blob=TextBlob(text)

sentiment= blob.sentiment.polarity
print(sentiment)
