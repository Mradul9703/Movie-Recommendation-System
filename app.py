# Importing necessay libraries
import streamlit as st
import pickle
import requests
import time
import concurrent.futures

# Load data
movies = pickle.load(open('movies_df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API key
API_KEY = 'b1f80b889ebb3da66f215768dea0838b'


def fetch_poster(movie_id, retries=5):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return f'https://image.tmdb.org/t/p/w500/{poster_path}'
            else:
                return 'https://via.placeholder.com/300x450?text=No+Image'
        except Exception as e:
            time.sleep(1)  # short delay before retry
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

    st.toast("Please wait...", icon="⏳")
    names, posters = recommend(selected_movie)

    if names:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(posters[i])
                st.caption(names[i])
    else:
        st.warning("Could not generate recommendations.")