#!/usr/bin/python3
"""Configure web application to listen
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(**text):
    """ Serves a http response to /python/<text>
        endpoint's view
        Args:
            text (str): optional parameter string
        Returns:
            str: returns http response text"""

    #: str: value stores variable value of kwargs argument
    value = text['text']
    msg = 'Python {}'.format(value.replace('_', ' '))
    return msg


if __name__ == '__main__':
    app.run(host='0.0.0.0')
