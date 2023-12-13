from flask import Flask, render_template, request
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

app = Flask(__name__)

loaded_model = joblib.load("random_forest_model.pkl")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/personalities")
def personalities():
    return render_template("personalities.html")


@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.form.get("user_input")
    cleaned_input = clean(user_input)
    preprocess = pre_preocess(cleaned_input)
    final = numberize(preprocess)
    predictions = loaded_model.predict(final)

    return render_template("result.html", predictions=predictions)


def clean(text):
    text.strip("'").split("|||")
    text.lower()
    " ".join(text)
    return text


def pre_preocess(text):
    text = re.sub(r"(http|https|www)\S+", "link", text)

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))
    filtered_tokens = []
    for word in tokens:
        if word.lower() not in stop_words:
            filtered_tokens.append(word)

    stemmer = PorterStemmer()
    stemmed_tokens = []
    for word in filtered_tokens:
        stemmed_tokens.append(stemmer.stem(word))

    processed_text = " ".join(stemmed_tokens)

    return processed_text


def numberize(text):
    documents = [text]

    tfidf_vectorizer = TfidfVectorizer()

    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    feature_names = tfidf_vectorizer.get_feature_names_out()

    features_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
    return features_df


if __name__ == "__main__":
    app.run(debug=True)
