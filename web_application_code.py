import streamlit as st
import pickle
import pandas as pd
import requests
import textwrap
from PIL import Image, ImageDraw

def create_fallback_poster(title):
    img = Image.new("RGB", (300, 450), color=(25, 35, 60))
    draw = ImageDraw.Draw(img)
    draw.rectangle([12, 12, 288, 438], outline=(100, 149, 237), width=3)
    wrapped_title = textwrap.fill(title, width=18)
    draw.multiline_text((150, 225), wrapped_title, fill=(255, 255, 255), anchor="mm", align="center")
    return img

def fetch_poster(movie_id, title="Movie"):
    try:
        url = "http://omdbapi.com"
        params = {"t": title, "apikey": "2284227e"}
        data = requests.get(url, params=params, timeout=15).json()
        if data.get("Poster") and data["Poster"] != "N/A":
            return data["Poster"]
    except Exception:
        pass
    return create_fallback_poster(title)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_movies_poster.append(fetch_poster(movie_id, title))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("AI Based Movie Recommender System")
selected_movie_name = st.selectbox(
    'Select Movie From The Given List',
    movies['title'].values
)

if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])