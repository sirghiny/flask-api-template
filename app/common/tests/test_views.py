"""Test common views."""
from json import loads

from app.common.tests.mixins import BaseCase


class TestWelcome(BaseCase):
    """Welcome resource tests."""

    def test_welcome(self):
        """Test welcome resource."""
        response = self.client.get('/')
        expected = {
            "status": "success",
            "data": {
                "message": "Welcome to this Flask API Template."
            }
        }
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, loads(response.data))
