# Fake News Detector: News Article Classification (Fake/Real)

## Objective
Classify news articles as **fake** or **real** using Natural Language Processing (NLP) and provide an interactive web interface for predictions.

---

## Project Overview

This project uses Python, machine learning, and NLP techniques to detect fake news articles. The main workflow includes:
- Data collection and preprocessing
- Feature extraction with TF-IDF
- Model training (Logistic Regression / Naive Bayes)
- Evaluation with multiple metrics
- Deployment via a **Streamlit** web app for real-time demo

---

## Features

- **Data Cleaning:** Extensive text preprocessing with NLTK (stopwords removal, stemming, etc.)
- **Feature Engineering:** Utilization of TF-IDF vectorization from Scikit-learn
- **Modeling:** Training and comparing Logistic Regression and Naive Bayes classifiers
- **Evaluation:** Reporting metrics such as Accuracy, Precision, Recall, F1 Score
- **Deployment:** Easy-to-use **Streamlit app** for live classification of news articles on the web

---

## Getting Started

### 1. Clone the Repository

### 2. Install Requirements
- Includes: `streamlit`, `scikit-learn`, `nltk`, `pandas`, `joblib`, etc.

### 3. Train Models (Optional)
- Use the provided Jupyter notebook to train and evaluate models.
- The trained model files (`lr_model.joblib` and `vectorizer.joblib`) are saved for direct app usage.

### 4. Run the Streamlit App
- Replace `app.py` with your actual Streamlit app filename.
- The app will open in your web browser for real-time news article classification.

---

## Project Structure

| File/Folder         | Description                             |
|---------------------|-----------------------------------------|
| `untitled.py`            | Streamlit web app for live demo         |
| `xyzw.ipynb`    | Jupyter notebook: data processing, modeling, evaluation   |
| `lr_model.joblib`   | Trained Logistic Regression model       |
| `vectorizer.joblib` | Trained TF-IDF vectorizer              |
| `README.md`         | Project overview and instructions       |

---

## Streamlit Web App

The project is showcased via a **Streamlit web app**.
- **Input:** Paste or write a news article
- **Output:** Instant prediction (Fake or Real), plus a simple explanation and model confidence

---

## Deliverables

- Annotated Jupyter notebook for all data science steps
- Trained model files (ready to use)
- Streamlit app for live, interactive predictions
- Instructions for local deployment and reproducibility

---

 
 ## Acknowledgments

- [Kaggle]((https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)) for datasets
- Streamlit, Scikit-learn, NLTK, Pandas for powerful open-source tools

---

