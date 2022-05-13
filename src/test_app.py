try:
    import unittest
    from app import app
    from tasks import Tasks
except Exception as e:
    print('ImportError: Failed to import modules: {}'.format(e))

class TestApp(unittest.TestCase):

    # Test GET request
    def test_app(self):
        tester = app.test_client(self)
        response = tester.get('/tasks', content_type='application/json')
        status = response.status_code
        self.assertEqual(status, 200)

    # Test GET response valid data
    def test_app_valid_data(self):
        tester = app.test_client(self)
        response = tester.get('/tasks', content_type='application/json')
        self.assertEqual(response.json, {'tasks': Tasks})

    # Test Get request with invalid url
    def test_app_invalid_url(self):
        tester = app.test_client(self)
        response = tester.get('/invalid_url', content_type='application/json')
        status = response.status_code
        self.assertEqual(status, 404)

    # Test Get request valid data whit id
    def test_app_valid_data_with_id(self):
        tester = app.test_client(self)
        response = tester.get('/tasks/1', content_type='application/json')
        self.assertEqual(response.json, {'task': Tasks[0]})




if __name__ == '__main__':
    unittest.main()