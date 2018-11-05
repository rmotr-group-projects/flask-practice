import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def welcome_view():
    return 'Welcome to our Flask Practice!'


@app.route('/sum/<int:first_number>/<int:second_number>')
def sum_of_two_numbers(first_number, second_number):
    total = first_number + second_number
    return 'The sum of {} and {} is: {}'.format(first_number, second_number, total)


@app.route('/username/<path:name>')
def build_username(name):
        first, second = name.split("/")
        return first[0].lower() + second.lower()

@app.route('/user')
def search_user():
    query = request.args.get('search')
    users = ['Jack', 'Morgan', 'Moe', 'Steve']
    hits = [contained for contained in users if query in contained.lower()]

    return 'Found {} users that match with search: "{}"'.format(len(hits), query)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
