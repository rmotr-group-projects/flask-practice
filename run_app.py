import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def welcome_view():
    return 'Welcome to our Flask Practice!'


@app.route('/sum/<int:first_number>/<int:second_number>')
def sum_of_two_numbers(first_number, second_number):
    """Implement a view that receives two numbers and returns the sum of them"""
    total = first_number + second_number
    return 'The sum of {} and {} is: {}'.format(first_number, second_number, total)


@app.route('/username/<string:first_name>/<string:last_name>')
def build_username(first_name, last_name):
    """
        Implement a view that receives user's first name and last name,
        and returns its username built with first letter of the first name,
        concatenated with the last name.

        i.e: username for "Elon Musk" would be "emusk"
    """
    return '{first_name_initial}{last_name}'.format(first_name_initial=first_name[0], last_name=last_name).lower()


@app.route('/user')
def search_user():
    """
        Implement a view that receives a '?search=' query parameter in the URL,
        and returns the amount of users in the given users_list that contains
        that search string in their names.
        i.e: /user?search=mo will return 'Found 2 users that match with search "mo"'
    """
    # HINT: to access the query params you'll need to use request.args.get()
    # function imported from flask
    users = ['Jack', 'Morgan', 'Moe', 'Steve']
    search_term = request.args.get('search')
    match_count = len(list(filter(lambda x: search_term in x.lower(), users)))
    return 'Found {match_count} users that match with search: "{search_term}"'.format(match_count=match_count, search_term=search_term)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
