import unittest
from app.app import app
import json
import requests

class TestML(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client(self)
        self.test_user = 11111
    
    def test_user_check(self):
        response = self.client.get('/api/check_user', data = {'user_id': self.test_user})
        self.assertEqual(response.statuse_code, 200)
        
    def test_train(self):
        with open('train.json', 'r') as file:
            train = json.load(file)
        with open('y_train.json', 'r') as file:
            y_train = json.load(file)
            
        response = requests.post("/api/ml_models/train", data = {'train': json.dumps(train.to_json()), 
                                                                 'y_train': y_train.to_json(), 
                                                                 'name': 'logreg',
                                                                 'user_id':self.test_user})
        self.assertEqual(response.statuse_code, 200)
        
    def test_count(self):
        response = requests.get("api/ml_models/count", data = {'user_id':self.test_user})
        self.assertEqual(response.statuse_code, 200)
        
    def test_predict(self):
        with open('test.json', 'r') as file:
            test = json.load(file)
        with open('y_test.json', 'r') as file:
            y_test = json.load(file)
            
        response = requests.post("/api/ml_models/predict/0", data = {'test': json.dumps(test.to_json()), 
                                                                 'y_test': y_test.to_json(), 
                                                                 'user_id':self.test_user})
        self.assertEqual(response.statuse_code, 200)

if __name__ == '__main__':
    unittest.main()