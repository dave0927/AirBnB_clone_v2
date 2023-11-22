#!/usr/bin/python3
"""Script starts Flask web application"""

from flask import Flask

#: flask: app stores instance of Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start_app():
    """ start_app(): serves a response to request
        to web application base entry point"""

    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
