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


@app.route('/username/<first_name>/<last_name>')
def build_username(first_name, last_name):
    first = first_name.lower()[0]
    second = last_name.lower()
    return str(first+second)


@app.route('/user?search=<param>')
def search_user(param):

#     """
#         Implement a view that receives a '?search=' query parameter in the URL,
#         and returns the amount of users in the given users_list that contains
#         that search string in their names.
#         i.e: /user?search=mo will return 'Found 2 users that match with search "mo"'
#     """
#     # HINT: to access the query params you'll need to use request.args.get()
#     # function imported from flask
    request.args.get()
    users = ['Jack', 'Morgan', 'Moe', 'Steve']
    number = 0
    for user in users:
        if param in user:
            number+=1
    return 'Found {} users that match with search "{}"'.format(number, param)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
