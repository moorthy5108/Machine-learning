import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')
def analyze_sentiment(review):
    #Create a SentimentIntensityAnalyzer
    sid=SentimentIntensityAnalyzer()

    #Get Sentiment Score
    scores=sid.polarity_scores(review)

    #Interpret the Sentment Scores
    if scores['compound']>=0.5:
        sentiment="Postive"
    elif scores['compound']<=-0.05:
        sentiment="Negative"
    else:
        sentiment="Neutral"

    return sentiment

#Apply product Rviews
reviews=[
    "This product is amzing! I love it",
    "This Quality is not as expected.I'm disapontrd",
    "It's an okay product,Nothing special.",
    "gets me through a regular of use",
    "The acting was good , but the movie could not have been better"
]

#Analyzer and print the sentiment for each review
for idx,review in enumerate(reviews,1):
    sentiment=analyze_sentiment(review)
    print(f"Review {idx}: {review}\nSentiment: {sentiment}\n")


