import pandas as pd
import string
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

nltk.download('stopwords')

# Load data
df = pd.read_csv("fake_reviews_dataset.csv").dropna(subset=["review"])

# Preprocess text
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

df["cleaned_review"] = df["review"].apply(preprocess_text)

# Vectorization with n-grams
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(df["cleaned_review"])
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save model & vectorizer
with open("fake_review_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
print("✅ Model and vectorizer saved.")
