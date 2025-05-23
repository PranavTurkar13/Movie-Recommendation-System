# 🎬 Movie Recommendation System

A simple and effective **content-based Movie Recommendation System** that suggests similar movies based on your selection using vectorization and cosine similarity.

---

## 📽️ Overview

This project uses **Jupyter Notebook** for data preprocessing and model creation, and **Streamlit** for building a lightweight, interactive frontend.

---

## 📁 Dataset

- We have used a custom dataset containing movie metadata (title, overview, genres, keywords, cast, crew, etc.).
- The dataset has been cleaned and processed using pandas and stored as `movies.pkl`.
- You can replace or update the dataset for more accurate or personalized recommendations.

---

## 🧠 How It Works

- Combines textual features into a single column.
- Applies **TF-IDF/CountVectorizer** to convert text to vectors.
- Calculates **cosine similarity** between all movies.
- Suggests top 5 most similar movies.

---

## 🔄 Flowchart

📊 Model Flow  
![Flowchart](images/flowchar.png)



🧪 Model Training (Jupyter Notebook)
The model is trained in a Jupyter Notebook to:
Load and clean the dataset
Combine important features (overview, genre, cast, etc.)
Create the similarity matrix
Save it using pickle for frontend use

🎨 Frontend (Streamlit)
The frontend is created using Streamlit:
Dropdown to select movie
Button to generate recommendations
Displays recommended movie posters and titles

## 🖼️ Screenshots

📷 Recommendation Display  
![Recommendation Display](images/screenshot1.png)

📷 Top 10 Trending Movies  
![Top 10 Trending Movies ](images/screenshot2.png)

⚙️ Installation
# Clone the repo
git clone https://github.com/PranavTurkar13/Movie-Recommendation-System.git
cd Movie-Recommendation-System

# Install dependencies
pip install -r requirements.txt
▶️ Run the App
streamlit run recm.py

# Dataset
Dataset Link - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata


🙋‍♂️ Author
Pranav Turkar
GitHub: @PranavTurkar13


