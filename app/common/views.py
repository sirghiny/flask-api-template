"""Welcome to the API view."""

from datetime import datetime

from flask_restful import Resource


class WelcomeResource(Resource):
    """Displays welcome message and any other introductory information."""

    def get(self):
        """Get the welcome message an display it."""
        # print(f'\nHit at: {datetime.now()}\n')
        return {
            "status": "success",
            "data": {
                "message": "Welcome to this Flask API Template."
            }
        }, 200
