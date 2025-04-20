import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title="Movie Recommender", layout="wide")

# ------------------ Functions ------------------

@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""

@st.cache_data
def fetch_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    return {
        "overview": data.get("overview", "No overview available."),
        "release_date": data.get("release_date", "Unknown"),
        "genres": ", ".join([genre["name"] for genre in data.get("genres", [])])
    }

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    recommended_infos = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        recommended_infos.append(fetch_details(movie_id))
    return recommended_movies, recommended_posters, recommended_infos

# ------------------ Load Data ------------------

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ------------------ UI ------------------

st.markdown("<h1 style='text-align: center; color: cyan;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

select_movie_name = st.selectbox("Select a movie to get recommendations:", movies['title'].values)

if st.button('🎥 Show Recommendations'):
    with st.spinner('Fetching recommendations...'):
        names, posters, infos = recommend(select_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.markdown(f"**{names[i]}**")
            stars = int(movies[movies['title'] == names[i]]['vote_average'].values[0] // 2)
            st.markdown("⭐" * stars)
            st.caption(f"{infos[i]['release_date']} | {infos[i]['genres']}")
            with st.expander("📜 Overview"):
                st.write(infos[i]["overview"])

# ------------------ Trending Movies Section ------------------

st.markdown("---")
st.subheader("🔥 Top 10 Trending Movies")

movies['trending_score'] = movies['popularity'] * movies['vote_average']
top_10_trending = movies.sort_values('trending_score', ascending=False).head(10)

trend_cols = st.columns(5)
for i in range(10):
    col = trend_cols[i % 5]
    with col:
        movie_id = top_10_trending.iloc[i].movie_id
        title = top_10_trending.iloc[i].title
        poster = fetch_poster(movie_id)
        st.image(poster)
        st.markdown(f"**{title}**")
        st.caption(f"⭐ {top_10_trending.iloc[i]['vote_average']} | 🔥 Popularity: {int(top_10_trending.iloc[i]['popularity'])}")
