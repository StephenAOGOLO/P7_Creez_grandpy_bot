""" Getting API Google Map Key with the "config.py" module.
    - The API Google Map Key is stored as an environnement varible into the system.
    - "config.py" retrieving the key to use it for requests."""
from os import environ

GMAP_ID = environ.get("GMAP_ID")
