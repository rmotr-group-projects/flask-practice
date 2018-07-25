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
    username = (first_name.lower()[0] + last_name.lower())
    return username

@app.route('/user')
def search_user():
    users = ['Jack', 'Morgan', 'Moe', 'Steve']
    query = request.args.get('search', '')
    x = 1
    count = sum(x for user in users if query in user.lower())
    return 'Found {} users that match with search: "{}"'.format(count, query)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
