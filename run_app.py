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
def build_username(first_name,last_name):
    username = first_name[0].lower() + last_name.lower()
    return username

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
    search = request.args.get('search')
    print(search)
    users = ['Jack', 'Morgan', 'Moe', 'Steve']
    lower_users = [x.lower() for x in users]
    print(lower_users)
    matching_users = [i for i in lower_users if search in i]
    print(len(matching_users))
    print(matching_users)
    '''
    for user in users:
        if search in user:
            number_of_users +=1
    '''
    return 'Found {} users that match with search: "{}"'.format(len(matching_users),search)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
