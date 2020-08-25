""" Initialization with the "__init__.py" module
    -   Creating Flask application instance.
    - The "views" import is stated
    at the last position (Do not reset for good use)."""
from flask import Flask


app = Flask(__name__)
from . import views
