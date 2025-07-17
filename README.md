# 🎬 Movie Recommendation System

A simple content-based movie recommendation system using machine learning and Streamlit. Enter any movie name and get 5 similar movie suggestions with posters!

## 🚀 Features

- Content-based filtering using cosine similarity
- Poster fetching via TMDB API
- Responsive UI with Streamlit
- Parallel API calls to speed up loading

## 📁 Files Included

- `Movie_Recommendation_Sysem.ipynb` – Jupyter Notebook for data cleaning, feature extraction, and similarity matrix generation
- `app.py` – Streamlit app to serve the model and show recommendations
- `movies_df.pkl` – Preprocessed movie dataset
- `similarity.pkl` – Cosine similarity matrix for recommendations
- `tmdb_5000_movies.csv`, `tmdb_5000_credits.csv` – Original datasets from TMDB

## 🧪 Demo

![Demo Screenshot](demo.png)  
> The UI shows 5 recommended movies with poster images.

## 🛠 Tech Stack

| Tool        | Purpose             |
|-------------|---------------------|
| Python      | Programming language |
| Streamlit   | Web app UI           |
| Scikit-learn| Similarity calculation |
| Pandas      | Data handling        |
| TMDB API    | Poster retrieval     |

## 🌐 TMDB API

Poster images are fetched using the TMDB API. You can generate your API key here:  
🔗 https://www.themoviedb.org/settings/api

In `app.py`, replace the API key if needed:
```python
API_KEY = 'your_api_key_here'
```

## ▶️ Run the App

To run the app on your system:

1. Install all dependencies 
2. Run the app using:

```bash
streamlit run app.py
```
