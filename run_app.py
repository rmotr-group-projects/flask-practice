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


@app.route('/username/<string:first_name>/<string:last_name>')
def build_username(first_name, last_name):
   
    username = '{}{}'.format(first_name[0], last_name)
    return username.lower()

@app.route('/user')
def search_user():
 
    users = ['Jack', 'Morgan', 'Moe', 'Steve']
    search = request.args.get('search')
    filtered_users = [user for user in users if search.lower() in user.lower()]
    return 'Found {} users that match with search: "{}"'.format(
        len(filtered_users), search)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)