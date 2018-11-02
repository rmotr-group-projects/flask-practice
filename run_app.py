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

@app.route('/username/<path:name>')
def build_username(name):
    first_name, second_name = name.split("/")
    return first_name[0].lower() + second_name.lower()
    

@app.route('/user')
def search_user():
    """
        Implement a view that receives a '?search=' query parameter in the URL,
        and returns the amount of users in the given users_list that contains
        that search string in their names.
        i.e: /user?search=mo will return 'Found 2 users that match with search "mo"'
    """
    search_term = request.args.get('search')
    # HINT: to access the query params you'll need to use request.args.get()
    # function imported from flask
    

    users = ['Jack', 'Morgan', 'Moe', 'Steve']
    found_list = [name for name in users if search_term in name.lower()]

    return "Found {number} users that match with search: \"{search_term}\"".format(search_term=search_term,number=(len(found_list)))


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
