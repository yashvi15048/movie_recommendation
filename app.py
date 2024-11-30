import streamlit as st
import pickle
import pandas as pd


# Function to recommend movies
def recommend(movie):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]

    # Compute similarity scores for the selected movie
    distances = similarity[movie_index]

    # Sort movies by similarity scores in descending order
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Collect recommended movies
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)  # Use `iloc` to get the movie title
    return recommended_movies


# Load the data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# App title
st.title('🎥 Movie Recommender System')

# Dropdown for movie selection
selected_movies_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

# Recommend button
if st.button('Recommend'):
    recommendations = recommend(selected_movies_name)
    st.subheader('Here are 5 movies you might like:')
    for i in recommendations:
        st.write(i)
