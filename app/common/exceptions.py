"""Custom exceptions."""


class ObjectNotSavedError(Exception):
    """Raised when a database object is not successfully saved."""

    def __init__(self, exception, status=None, help=None):
        """Customize the exception."""
        self.exception = exception
        self.message = "Ensure the object you're saving is valid."
