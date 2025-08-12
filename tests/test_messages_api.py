import unittest
import json
from app import app

class TestMessagesAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_create_message_success(self):
        response = self.client.post('/api/messages', json={
            "name": "Jenny",
            "email": "jenny@example.com",
            "message": "Hello!"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_create_message_invalid(self):
        response = self.client.post('/api/messages', json={})
        self.assertEqual(response.status_code, 400)

    def test_get_messages(self):
        self.client.post('/api/messages', json={
            "name": "Jenny",
            "email": "jenny@example.com",
            "message": "Hello!"
        })
        response = self.client.get('/api/messages')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_update_message_not_found(self):
        response = self.client.put('/api/messages/invalid-id', json={"message": "Updated"})
        self.assertEqual(response.status_code, 404)

    def test_delete_message_not_found(self):
        response = self.client.delete('/api/messages/invalid-id')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
