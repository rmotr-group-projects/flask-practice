# Flask Practice

## About Flask

Flask is a highly used Python micro Web Framework. It provides basic functionality to build web applications, like routing, request/response handling, etc. It's a "small" framework compared to other ones (like Django), but in many cases that's a great advantage.


## Install Instructions
Fork this repo and create a new cloud9 workspace as we do with other projects. Then follow the usual steps:

```bash
$ mkvirtualenv flask-practice -p /usr/bin/python3
$ pip install -r requirements.txt
```


## Running the app server

Flask framework provides, out of the box, a way to run a development web server in your local machine. Just execute the `run_app.py` script available in the project and the application will stay listening at `localhost:8080`. (Make sure to have all the requirements previously installed)

```bash
$ python run_app.py
```


## Running tests

Tests are split among several functions. You can run them all together doing `pytest tests.py` or select individual based on keyword expressions like `pytest -k 'test_1' tests.py`.


## Tasks

### 1. Implement a simple Welcome view

This view was done for you as an example. Just implemented a basic view on `/` URL that returns a string welcoming to your Flask practice

### 2. Implement a view that receives URL parameters

This one was also done as an example. In this case, the view receives two numbers as URL parameters, and returns the sum of them in a formatted string.

i.e: Sending `/sum/100/200`, the response would be: `"The sum of 100 and 200 is: 300"`

### 3. Implement a view that builds usernames

In this case, you'll have to implement a view that receives user's first name and last name, and builds its lowercase username using first letter of the first name, concatenated with the last name. (Remember to validate that given parameters are strings)

i.e: Sending `/username/Elon/Musk` will return `emusk`

### 4. Implement a view with query parameters

For this exercise, you'll have to implement a view that receives a `?search=` query parameter in the URL, and returns the amount of users in the given users_list that contains that search string in their names.

i.e: `/user?search=mo` will return `'Found 2 users that match with search "mo"'`
