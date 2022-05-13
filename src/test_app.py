import json


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
    
    # Test Get request with invalid id
    def test_app_invalid_id(self):
        tester = app.test_client(self)
        response = tester.get('/tasks/100', content_type='application/json')
        response = response.json
        self.assertEqual(response['message'], 'Task not found')

    # Test POST request
    def test_app_post(self):
        tester = app.test_client(self)
        response = tester.post('/tasks', content_type='application/json', data=json.dumps({'id': 2, 'title': 'Test Task', 'description': 'Test Description', 'is_completed': False}))
        status = response.status_code
        self.assertEqual(status, 201)

    # Test POST request with invalid data
    def test_app_invalid_post(self):
        tester = app.test_client(self)
        response = tester.post('/tasks', content_type='application/json', data=json.dumps({'id': 2, 'title': 'Test Task', 'description': 'Test Description'}))
        status = response.status_code
        self.assertEqual(status, 400)

    # Test PUT request
    def test_app_put(self):
        tester = app.test_client(self)
        response = tester.put('/tasks/1', content_type='application/json', data=json.dumps({'id': 1, 'title': 'Test Task', 'description': 'Test Description', 'is_completed': False}))
        status = response.status_code
        self.assertEqual(status, 200)
    
    # Test PUT request with invalid id
    def test_app_invalid_put(self):
        tester = app.test_client(self)
        response = tester.put('/tasks/100', content_type='application/json', data=json.dumps({'id': 1, 'title': 'Test Task', 'description': 'Test Description', 'is_completed': False}))
        status = response.status_code
        self.assertEqual(status, 404)






if __name__ == '__main__':
    unittest.main()