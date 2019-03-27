"""Common URLs."""

from app.common.views import WelcomeResource


urls = [
    {
        'resource': WelcomeResource,
        'routes': ['/', '/api/v1', '/api/v1/']
    }
]
