import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/cleaned_books.csv")

import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()  # lowercase
    text = "".join([char for char in text if char not in string.punctuation])  # remove punctuation
    words = text.split()
    words = [word for word in words if word not in stop_words]  # remove stopwords
    return " ".join(words)

# Apply preprocessing
df["Title"] = df["Title"].fillna("")
df["Processed_Title"] = df["Title"].apply(preprocess_text)

# Convert titles into vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df["Processed_Title"])

# Compute similarity
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)


# 🔍 SEARCH FUNCTION
def search_book(query):
    query = preprocess_text(query)
    query_vec = vectorizer.transform([query])
    sim_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()

    top_indices = sim_scores.argsort()[-5:][::-1]

    results = df.iloc[top_indices]

    print("\n📚 Top Matches:")
    print(results[["Title", "Price", "Rating", "Availability"]])


# 🎯 FILTER FUNCTIONS
def filter_price(max_price):
    result = df[df["Price"] <= max_price]
    print(result[["Title", "Price"]].head(10))


def filter_available():
    result = df[df["Availability"] > 0]
    print(result[["Title", "Availability"]].head(10))


# 🤖 CHATBOT LOOP
def chatbot():
    print("🤖 AI Book Assistant Ready!")
    print("Type 'exit' to quit")

    while True:
        query = input("\nAsk something: ").lower()

        if query == "exit":
            break

        elif "price" in query:
            price = float(input("Enter max price: "))
            filter_price(price)

        elif "available" in query:
            filter_available()

        else:
            search_book(query)


chatbot()