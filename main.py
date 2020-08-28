"""
Welcome to the main program.
When it starts the program process is following the steps below:
- Initialization with the "__init__.py" module.
- Preparing routes with the "views.py" module.
- Preparing operational functions with the "utils.py" module.
- Getting API Google Map Key with the "config.py" module.
- Displaying and managing HMI (Human Machine Interface) with the "main.py" module.
"""
# -*- coding: utf-8 -*-
from GrandPyBot import app


if __name__ == "__main__":
    app.run(debug=1000, port=1000)
