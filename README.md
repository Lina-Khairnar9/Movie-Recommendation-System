# Movie Recommendation System

A content-based movie recommendation system built using Python and Streamlit that suggests similar movies based on user selection.

## Project Overview
* **Objective:** Recommend top matching movies by analyzing movie metadata (genres, keywords, cast, and overview).
* **Tech Stack:** Python, Pandas, Scikit-Learn, Streamlit.
* **Project Files:**
  * `Movie_Recommender_System.ipynb` - Data preprocessing, feature vectorization, and cosine similarity calculation.
  * `movie_dict.pkl` - Preprocessed movie dictionary used for fast lookup.
  * `web_application_code.py` -  Streamlit web app interface for selecting a movie and viewing recommendations.

## How to Run
1. Install required libraries (`pandas`, `scikit-learn`, `streamlit`, `requests`).
2. Run the web application:
   ```bash
   streamlit run web_application_code.py
   ```