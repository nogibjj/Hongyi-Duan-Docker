import unittest
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Python application running in Docker!", response.data)

    def test_compute(self):
        response = self.app.post('/compute', json={"number": 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 25)

if __name__ == '__main__':
    unittest.main()