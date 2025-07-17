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
- `requirements.txt` - For required libraries

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

## 📦 Data & Pickle Files

This project requires the following `.pkl` files which are not included in the repo:
- `movies_df.pkl`
- `similarity.pkl`

You can generate them yourself by:
1. Downloading the dataset from Kaggle:  
   🔗 [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

2. Running `Movie_Recommendation_Sysem.ipynb` to:
   - Clean and merge the datasets
   - Create the feature vectors
   - Export files using:

```python
import pickle

pickle.dump(movies_df, open('movies_df.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
```

## ▶️ Run the App

To run the app on your system:

1. Install all dependencies 
2. Run the app using:

```bash
streamlit run app.py
```
