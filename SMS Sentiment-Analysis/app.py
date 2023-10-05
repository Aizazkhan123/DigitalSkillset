from flask import Flask, render_template, request
import pickle
import re
import nltk
import numpy as np


app = Flask(__name__)

# Load the sentiment analysis model and TF-IDF vectorizer
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)




@app.route('/', methods=['GET', 'POST'])
def analyze_sentiment():
    if request.method == 'POST':
        comment = request.form.get('comment')

        # Preprocess the comment
        preprocessed_comment = [comment]

        # Transform the preprocessed comment into a feature vector
        comment_vector = tfidf.transform(preprocessed_comment).toarray()


        # Predict the sentiment
        sentiment = clf.predict(comment_vector)

        return render_template('index.html', sentiment=sentiment)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
