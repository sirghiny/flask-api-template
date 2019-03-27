"""Base test class."""

from unittest import TestCase
from sqlalchemy import create_engine

from app.common.models import db

from main import create_app


class BaseCase(TestCase):
    """Base class to be inherited by all other testcases."""

    def setUp(self):
        """Set up test application."""
        create_engine('sqlite:///:memory:')
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """Delete database and recreate it with no data."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
