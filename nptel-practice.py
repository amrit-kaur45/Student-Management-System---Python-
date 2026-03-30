import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from textblob import TextBlob

authors = ['Hamilton', 'Madison', 'Jay' , 'Shared', 'Disputed']

federalist_by_author = {
    'Hamilton'  : "Text data for hamilton...",
    'Madison'  : "Text data for madison...",
    'Jay'  : "Text data for jay...",
    'Disputed'  : "Text data for disputed...",
    'Shared'  : "Text data for shared..."
}

author_tokens = {}
for author, text_data in federalist_by_author.items():
    tokens = [
        word for word in word_tokenize(text_data)
        if word.isalpha() and word.lower() not in stopwords.words("english")
    ]
    author_tokens[author] = tokens


author_word_lengths = {}
for author, tokens in author_tokens.items():
    word_lengths = [len(word) for word in tokens]
    author_word_lengths[author] = word_lengths


sentiment_scores = {}
for author, text_data in federalist_by_author.items():
    blob = TextBlob(text_data)
    sentiment_scores[author] = blob.sentiment.polarity


plt.figure(figsize=(12, 6))
for author in authors:
    fdist = FreqDist(author_word_lengths[author])
    fdist.plot(15, cumulative=False)
plt.legend(authors)
plt.show()


for author,sentiment in sentiment_scores.items():
    print(f"Sentiment analysis for {author} : Sentiment Score = {sentiment}")