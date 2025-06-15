# 🎮 Movie Recommender System

A simple and interactive web application that recommends similar movies based on a selected title. Built with **Streamlit**, this app uses a precomputed similarity matrix and TMDB API to fetch movie posters dynamically.

## 🚀 Features

* 🔍 Recommends 5 similar movies based on cosine similarity
* 🎥 Fetches and displays movie posters via the TMDB API
* 💽 Clean and responsive UI using Streamlit
* 📆 Uses pre-trained model and movie dataset stored in `.pkl` files

---

## 📂 Project Structure

```
Movie-Recommender/
│
├── frontend/
│   └── app.py                  # Main Streamlit app
│
├── model/
│   ├── movie_list.pkl          # Pickled DataFrame with 'title' and 'movie_id'
│   └── similarity.pkl          # Pickled similarity matrix
│
└── README.md                   # This file
```

---

## 🧐 How It Works

1. **Input:** User selects a movie from the dropdown.
2. **Processing:**

   * The app locates the selected movie in the dataset.
   * Retrieves the top 5 similar movies based on cosine similarity.
   * Fetches poster URLs using the TMDB API.
3. **Output:** Recommended movie names and posters are displayed in a row.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender/frontend
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

> **Note:** Create `requirements.txt` with the following:
>
> ```
> streamlit
> pandas
> scikit-learn
> requests
> ```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🔑 API Key Setup

This app uses [The Movie Database (TMDB)](https://www.themoviedb.org/documentation/api) API to fetch movie posters.

* Replace the API key in `app.py`:

  ```python
  api_key = "your_actual_tmdb_api_key"
  ```

---

## 🧰 Sample Data Format

Ensure `movie_list.pkl` is a pandas DataFrame with these columns:

| title      | movie\_id |
| ---------- | --------- |
| The Matrix | 603       |
| Inception  | 27205     |


## 📌 To Do

* Add genre/category-based filters
* Save user history
* Add search functionality
* Deploy using Streamlit Cloud or Render

