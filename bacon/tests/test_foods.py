import unittest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"]="testing"

class TestFoods(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_homepage_index(self):
        response = self.client.get("/")
        # data = response.get_json()
        self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, list)

    def test_login(self):
        response = self.client.get("/login/")
        # data = response.get_json()
        self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, list)

    def test_signup(self):
        response = self.client.get("/signup/")
        # data = response.get_json()
        self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, list)

    # def test_create_bad_course(self):
    #     response = self.client.post("/courses/", json={"course_name": ""})
    #     self.assertEqual(response.status_code, 400)