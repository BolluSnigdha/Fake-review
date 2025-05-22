from flask import Flask, render_template, request, jsonify
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Setup
app = Flask(__name__)
model = pickle.load(open('fake_review_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

nltk.download('stopwords')
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

# Preprocess function (must match training)
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html exists
@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    cleaned = clean_text(review)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    confidence = model.predict_proba(vectorized)[0][prediction] * 100
    label = "Fake Review ❌" if prediction == 1 else "Real Review ✅"
    result = f"{label} ({confidence:.2f}% confidence)"
    return jsonify({'prediction': result})



if __name__ == '__main__':
    app.run(debug=True)
