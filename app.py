# Importing necessay libraries
import streamlit as st
import pickle
import requests
import time
import concurrent.futures
import gdown
import os

# Load data

movies_fileID = '1U4SwudE2wuWXOR6ZYLbF6nhS4ryIO5Dl'
similarity_fileID = '1oJYlIlFAe8_ciUSG47xD9hcpclTfB9bH'

movies_url = f'https://drive.google.com/uc?id={movies_fileID}'
similarity_url = f'https://drive.google.com/uc?id={similarity_fileID}'

if not os.path.exists('movies_df.pkl'):
    gdown.download(movies_url, 'movies_df.pkl')
if not os.path.exists('similarity.pkl'):
    gdown.download(similarity_url, 'similarity.pkl')

movies = pickle.load(open('movies_df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API key
API_KEY = st.secrets["api_key"]

def fetch_poster(movie_id, retries=7):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return f'https://image.tmdb.org/t/p/w500/{poster_path}'
            else:
                return 'https://via.placeholder.com/300x450?text=No+Image'
        except Exception as e:
            time.sleep(0.5)  # short delay before retry
    # After retries, return placeholder
    return 'https://via.placeholder.com/300x450?text=Error'


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        movie_ids = []

        for i in movie_list:
            idx = i[0]
            recommended_movies.append(movies.iloc[idx].title)
            movie_ids.append(movies.iloc[idx].movie_id)

        # Fetch posters in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            posters = list(executor.map(fetch_poster, movie_ids))

        return recommended_movies, posters

    except Exception as e:
        st.error(f"Error: {str(e)}")
        return [], []


# Streamlit app
st.title("Movie Recommendation System")
selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend movies"):

    with st.spinner("Loading..."):
        names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i],caption = names[i])
