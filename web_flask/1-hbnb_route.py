#!/usr/bin/python3
""" Start and configure web application to
    listen on port 5000/tcp."""

from flask import Flask

#: flask: app stores instance of Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Serves a http response to a request
        on / endpoint route."""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Serves a http response to a request
        on /hbnb endpoint route."""

    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
