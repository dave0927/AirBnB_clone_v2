#!/usr/bin/python3
""" Configure and start web application on
    port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State

#: flask obj: Stores reference to flask application
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_veiw():
    """ Serve 8-cities_by_states.html page to enpoint
        route /cities_by_states
        Args:
            No required argument
        Returns:
            return html page"""

    #: list of state obj: Stores collection of state obj
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/states<id>', strict_slashes=False)
def states_id_veiw(id):
    """ Serve 8-cities_by_states.html page to enpoint
        route /cities_by_states
        Args:
            No required argument
        Returns:
            return html page"""

    #: list of state obj: Stores collection of state obj
    states = storage.all(State)

    for state in states.values():
        if id == state.id:
            return render_template('9-states.html', state=state, id=id)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def end_db_session(exception):
    """ Terminate database session through session
        scope and transaction scope as soon as http
        request lifecycle ends."""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
