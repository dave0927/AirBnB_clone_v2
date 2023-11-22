#!/usr/bin/python3
"""Configure and start web application to listen
on port 5000"""

from flask import Flask, render_template

#: flask: app stores instance of Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Serves a response to entry endpoint: '/'
        function view
        Args
            param: no parameter is required
        Returns:
            str: returns http response string value"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Serves a http response to '/hbnb' endpoint
        function view
        Args:
            param: no parameter is required
        Returns:
            str: returns http response string value"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Serves a http response to 'c/<text>' endpoint
        function view
        Args:
            text (str): optional passed in data to url
        Returns:
            str: returns http response string value"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(**text):
    """ Serves a http response to /python/<text>
        endpoint's view
        Args:
            text (str): optional parameter string
        Returns:
            str: returns http response string value"""

    #: str: value stores variable value of kwargs argument
    value = text['text']
    msg = 'Python {}'.format(value.replace('_', ' '))
    return msg


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(**n):
    """ Serve http response to /number/<n> endpoint
        function view
        Args:
            **n: Arbitrary keyword arguments
        Returns:
            str: Returns string value as a response"""
    return '{:d} is a number'.format(n['n'])


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_page(**n):
    """ Serve http response to /number_template/<n> endpoint
        function view
        Args:
            **n: Arbitrary keyword arguments
        Returns:
            file: Returns html page as a response"""
    return render_template('5-number.html', context=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_page_eo(**n):
    return render_template('6-number_odd_or_even.html', context=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
