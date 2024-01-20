import streamlit as st
import pickle
import pandas as pd

import requests

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}'.format(movie_id))
#     st.text('https://api.themoviedb.org/3/movie/{}'.format(movie_id))
#     data = response.json()
#     st.text(data)
#     return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    # recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies['movie_id'][i[0]]
        recommended_movies.append(movies['title'][i[0]])
        # fetch poster from API
        # recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies


# movies_list = pickle.load(open('movies.pkl','rb'))  #now this variale contain final new_df of movies
# movies_list = movies_list['title'].values
# rb stands for read binary, wb stands for write binary

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

# option = st.selectbox(
#     "How would you like to be contacted?",
#     movies_list
# )

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

if st.button('Recommend'):
    st.text(recommend(selected_movie_name))