#!/usr/bin/python3
""" Configure web application to listen
    on port 5000"""

from flask import Flask

#: flask: app stores instance of Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Serves a response to entry endpoint url"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Serves a http response to 'hbnb' endpoint"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):

    """ Serves a http response to 'c/<text>' endpoint
        Args:
            text (str): passed in data to url
        Returns:
            str: The return value"""

    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
