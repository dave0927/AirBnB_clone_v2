#!/usr/bin/python3
""" Configure and start web application on
    port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State

#: flask obj: Stores reference to flask application
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_view():
    """ Serve 7-states_list.html page to endpoint
        route /states_list
        Args:
            No required argument
        Returns:
            return html page"""

    #: list of state obj: Stores collection of state obj
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def end_db_session(exception):
    """ Terminate database session through session
        scope and transaction scope as soon as http
        request ends"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
