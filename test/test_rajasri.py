import unittest
import json
from app import app, db

class MovieAppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True
        db.create_all()  # Ensure database is initialized

        # Register and log in a user for use in tests requiring authentication
        cls.client.post('/register', data=json.dumps({
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "Test@123"
        }), content_type='application/json')
        cls.client.post('/login', data=json.dumps({
            "email": "testuser@example.com",
            "password": "Test@123"
        }), content_type='application/json')

    @classmethod
    def tearDownClass(cls):
        db.drop_all()  # Clean up database after tests

    # Helper Methods
    def register_user(self, email, username, password):
        return self.client.post('/register', data=json.dumps({
            "email": email,
            "username": username,
            "password": password
        }), content_type='application/json')

    def login_user(self, email, password):
        return self.client.post('/login', data=json.dumps({
            "email": email,
            "password": password
        }), content_type='application/json')

    # 1. User Registration & Login
    def test_successful_registration(self):
        response = self.register_user("test@example.com", "testuser", "Test@123")
        self.assertEqual(response.status_code, 200)

    def test_duplicate_email_registration(self):
        self.register_user("test@example.com", "testuser", "Test@123")
        response = self.register_user("test@example.com", "newuser", "Test@123")
        self.assertEqual(response.status_code, 400)

    def test_invalid_email_registration(self):
        response = self.register_user("invalidemail", "testuser", "Test@123")
        self.assertEqual(response.status_code, 400)

    def test_successful_login(self):
        self.register_user("login@example.com", "loginuser", "Login@123")
        response = self.login_user("login@example.com", "Login@123")
        self.assertEqual(response.status_code, 200)

    def test_unregistered_user_login(self):
        response = self.login_user("notexist@example.com", "Password123")
        self.assertEqual(response.status_code, 401)

    # 2. Movie Information Retrieval
    def test_successful_movie_info_retrieval(self):
        response = self.client.get('/api/movie_details?title=Inception')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('Title', data)

    def test_movie_not_found(self):
        response = self.client.get('/api/movie_details?title=NonexistentMovie')
        self.assertEqual(response.status_code, 404)

    # 3. Movie Recommendations
    def test_successful_movie_recommendation(self):
        self.login_user("test@example.com", "Test@123")
        response = self.client.post('/predict', data=json.dumps({
            "movie_list": ["Inception", "Interstellar", "Memento"]
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data["recommended_movies"]), 3)

    def test_empty_movie_list_recommendation(self):
        self.login_user("test@example.com", "Test@123")
        response = self.client.post('/predict', data=json.dumps({
            "movie_list": []
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # 4. Wishlist & Watched Movies
    def test_add_to_wishlist(self):
        self.login_user("test@example.com", "Test@123")
        response = self.client.post('/api/add_to_wishlist/Inception')
        self.assertEqual(response.status_code, 200)

    def test_add_to_watched(self):
        self.login_user("test@example.com", "Test@123")
        response = self.client.post('/api/add_to_watched/Inception')
        self.assertEqual(response.status_code, 200)

    def test_duplicate_add_to_wishlist(self):
        self.login_user("test@example.com", "Test@123")
        self.client.post('/api/add_to_wishlist/Inception')
        response = self.client.post('/api/add_to_wishlist/Inception')
        self.assertEqual(response.status_code, 400)

    def test_add_to_wishlist_not_logged_in(self):
        self.client.get('/logout')  # Log out the test user
        response = self.client.post('/api/add_to_wishlist/Inception')
        self.assertEqual(response.status_code, 401)  # Expect unauthorized

    def test_add_to_watched_not_logged_in(self):
        self.client.get('/logout')  # Log out the test user
        response = self.client.post('/api/add_to_watched/Inception')
        self.assertEqual(response.status_code, 401)  # Expect unauthorized

    # 5. Search Functionality
    def test_successful_search(self):
        response = self.client.get('/search?term=Inception')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertGreater(len(data["results"]), 0)

    def test_no_results_search(self):
        response = self.client.get('/search?term=NonexistentMovie')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data["results"]), 0)

 # 6. Movie Detail Retrieval
    def test_movie_detail_retrieval(self):
        response = self.client.get('/movie/Inception')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('Title', data)

    def test_movie_detail_not_found(self):
        response = self.client.get('/movie/NonexistentMovie')
        self.assertEqual(response.status_code, 404)

    # 7. Miscellaneous
    def test_successful_logout(self):
        self.login_user("test@example.com", "Test@123")
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

   


