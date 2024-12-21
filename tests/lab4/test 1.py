import unittest
from io import StringIO
import os
import sys

sys.path.append(os.path.abspath("C:/Users/FPT 2633/cs102/src/lab 4/src"))

from src.lab4.a1 import MovieRecommendationSystem

class TestMovieRecommendationSystem(unittest.TestCase):

    def setUp(self):
        self.movies_data = StringIO("1,Мстители: Финал\n2,Хатико\n3,Дюна\n4,Унесенные призраками\n")
        self.history_data = StringIO("2,1,3\n1,4,3\n2,2,2,2,2,3\n")

        self.movies_file = 'movies.csv'
        self.history_file = 'history.csv'

        with open(self.movies_file, 'w', encoding='utf-8') as f:
            f.write(self.movies_data.getvalue())

        with open(self.history_file, 'w', encoding='utf-8') as f:
            f.write(self.history_data.getvalue())

        self.system = MovieRecommendationSystem(self.movies_file, self.history_file)

    def test_load_movies(self):
        expected_movies = {1: "Мстители: Финал", 2: "Хатико", 3: "Дюна", 4: "Унесенные призраками"}
        self.assertEqual(self.system.movies, expected_movies)

    def test_load_history(self):
        expected_history = [[2, 1, 3], [1, 4, 3], [2, 2, 2, 2, 2, 3]]
        self.assertEqual(self.system.history, expected_history)

    def _find_similar_users(self, user_movies):
        similar_users = []
        for user in self.history:
            if any(movie in user_movies for movie in user):
                similar_users.append(user)
        return similar_users

    def _filter_watched_movies(self, user_movies, similar_users):
        watched_movies = set(user_movies)
        potential_movies = set()

        for user in similar_users:
            for movie in user:
                if movie not in watched_movies:
                    potential_movies.add(movie)

        return list(potential_movies)

    def test_find_most_popular_movie(self):
        movies = [1, 2, 3, 1, 2, 3, 1]
        most_popular = self.system._find_most_popular_movie(movies)
        self.assertEqual(most_popular, "Мстители: Финал")

    def test_recommend_movie(self):
        user_movies = [2, 1]
        recommendation = self.system.recommend_movie(user_movies)
        self.assertEqual(recommendation, "Дюна")

    def tearDown(self):
        if os.path.exists(self.movies_file):
            os.remove(self.movies_file)
        if os.path.exists(self.history_file):
            os.remove(self.history_file)

if __name__ == '__main__':
    unittest.main()