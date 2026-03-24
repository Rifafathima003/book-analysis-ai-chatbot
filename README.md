# 📚 Book Analysis & AI Chatbot

## 🚀 Project Overview
This project builds an end-to-end data pipeline:
- Web scraping book data
- Data cleaning & preprocessing
- Exploratory Data Analysis (EDA)
- AI-powered chatbot for book search

---

## 🛠️ Tech Stack
- Python
- BeautifulSoup (Web Scraping)
- Pandas (Data Processing)
- Matplotlib & Seaborn (EDA)
- Scikit-learn (TF-IDF, Cosine Similarity)
- NLTK (NLP Preprocessing)

---

## 📊 Features

### 🔍 Web Scraping
- Extracts book title, price, rating, availability

### 🧹 Data Cleaning
- Converts price to numeric
- Maps ratings to numbers
- Cleans availability

### 📈 EDA
- Rating distribution
- Price analysis
- Price vs Rating insights

### 🤖 AI Chatbot
- Search books using natural language
- Finds similar books using TF-IDF
- Filter by price
- Filter by availability

---

## 💡 Example Queries
- "cheap books under 20"
- "available books"
- "travel books"
- "harry potter"

---

---

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper
python src/scraper.py

# Clean data
python src/preprocess.py

# Run chatbot
python src/ai_chatbot.py

---

## 📸 Project Output

### 🤖 Chatbot Example
![Chatbot Output](assets/chatbot.png)

### 📊 Rating Distribution
![Rating Plot](assets/rating_plot.png)

### 💰 Price Distribution
![Price Plot](assets/price_plot.png)

---


## 🪛 Future Enhancement
- Streamlit UI
- Real-time API integration
- LLM-based chatbot

Author:
RIFA FATHIMA