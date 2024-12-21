import csv
from collections import Counter

class MovieRecommendationSystem:
    def __init__(self, movies_file, history_file):
        self.movies = self._load_movies(movies_file)
        self.history = self._load_history(history_file)

    def _load_movies(self, file_path):
        movies = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                movie_id, title = row
                movies[int(movie_id)] = title
        return movies

    def _load_history(self, file_path):
        history = []
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                history.append([int(movie_id) for movie_id in row])
        return history

    def recommend_movie(self, user_movies):
        similar_users = self._find_similar_users(user_movies)
        potential_movies = self._filter_watched_movies(user_movies, similar_users)
        if not potential_movies:
            return "No recommendations available."
        return self._find_most_popular_movie(potential_movies)

    def _find_similar_users(self, user_movies):
        similar_users = []
        user_movies_set = set(user_movies)
        for watched_movies in self.history:
            shared_movies = len(user_movies_set & set(watched_movies))
            if shared_movies >= len(user_movies) / 2:
                similar_users.append(watched_movies)
        return similar_users

    def _filter_watched_movies(self, user_movies, similar_users):
        user_movies_set = set(user_movies)
        all_movies = []
        for watched_movies in similar_users:
            all_movies.extend(movie for movie in watched_movies if movie not in user_movies_set)
        return all_movies

    def _find_most_popular_movie(self, movies):
        movie_counts = Counter(movies)
        most_popular_movie_id, _ = movie_counts.most_common(1)[0]
        return self.movies.get(most_popular_movie_id, "Unknown Movie")


# Constants for file paths
MOVIES_FILE = "movies.csv"
HISTORY_FILE = "history.csv"

if __name__ == "__main__":
    system = MovieRecommendationSystem(MOVIES_FILE, HISTORY_FILE)

    # Input user's movie history
    user_input = input("Enter the movies you have watched (comma-separated IDs): ")
    user_movies = [int(movie_id) for movie_id in user_input.split(",")]

    # Get recommendation
    recommendation = system.recommend_movie(user_movies)
    print(f"Recommended movie: {recommendation}")