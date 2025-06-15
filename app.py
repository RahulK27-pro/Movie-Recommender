import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def fetch_poster(movie_id):
    # Set up retry strategy
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        # Fetch movie poster with a timeout of 10 seconds
        response = session.get('https://api.themoviedb.org/3/movie/{}?api_key=ad20c4d7cfe529dd0945cc3aa922fb11&language=en-US'.format(movie_id), timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return None  # Return None in case of an error

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster_url = fetch_poster(movie_id)
        recommended_movies_posters.append(poster_url or 'https://via.placeholder.com/500x750.png?text=No+Poster+Available')  # Fallback placeholder
    return recommended_movies, recommended_movies_posters

# Load the data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app UI
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Which movie do you want to get similar recommendation?',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    # Display the recommended movies in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
