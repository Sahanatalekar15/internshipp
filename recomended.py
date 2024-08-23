import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data
movies = [
    {'MovieID': 101, 'Title': "Movie A", 'Genres': "Action, Thriller"},
    {'MovieID': 102, 'Title': "Movie B", 'Genres': "Romance, Drama"},
    {'MovieID': 103, 'Title': "Movie C", 'Genres': "Action, Adventure"},
    {'MovieID': 104, 'Title': "Movie D", 'Genres': "Comedy"}
]

# User preferences
user_preferences = "Action, Adventure"

# Create a list of movie genres
movie_genres = [movie['Genres'] for movie in movies]

# Create TF-IDF matrix for movie genres
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movie_genres)

# Create TF-IDF vector for user preferences
user_tfidf = vectorizer.transform([user_preferences])

# Calculate cosine similarity between user preferences and movies
similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix).flatten()

# Get movie recommendations
recommended_movie_indices = np.argsort(similarity_scores)[::-1]
recommended_movies = [movies[i] for i in recommended_movie_indices]

# Print recommendations
print("Recommended movies based on your preferences:")
for movie in recommended_movies:
    print(f"{movie['Title']} (Genres: {movie['Genres']})")
