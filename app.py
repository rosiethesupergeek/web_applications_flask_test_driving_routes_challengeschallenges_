import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

from flask import Flask, request # NOTE: we must import `request` too

app = Flask(__name__)

# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5000/hello?name=David"


# Request:
# GET /wave

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    # Send back a friendly greeting with the name
    return f"I am waving at {name}!"

# To make a request, run:
# curl "http://localhost:5001/wave?name=Leo"



# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"


# Request:
# POST /submit
#   With body parameter: name=Alice

@app.route('/submit', methods=['POST'])
def message():
    name = request.form['name'] # The value is 'Alice'
    message = request.form['message'] # the value is "Hello world"

    # Send back a fond farewell with the name
    return f"Thanks {name}, you sent this message: {message}"

# POST REQUESTS FOR EXERCISE ONE - TEST DRIVING ROUTES

@app.route('/count_vowels', methods=['POST'])
def vowel_count():
    text = request.form['text'] # The value is 'eee'
    vowels = []
    for letter in text:
        if letter.lower() in "aeiou":
            vowels.append(letter)
    returned_vowels = len(vowels)
    return f'There are {returned_vowels} vowels in "{text}"'

@app.route('/count_vowels', methods=['POST'])
def count_vowels_eunoia():
    text = request.form['text'] # the value is 'eunoia'
    vowels = []
    for letter in text:
        if letter.lower() in "aeiou":
            vowels.append(letter)
    returned_vowels = len(vowels)
    return f'There are {returned_vowels} vowels in "{text}"'

@app.route('/count_vowels', methods=['POST'])
def count_vowels_mercurial():
    text = request.form['text'] # the value is 'mercurial'
    vowels = []
    for letter in text:
        if letter.lower() in "aeiou":
            vowels.append(letter)
    returned_vowels = len(vowels)
    return f'There are {returned_vowels} vowels in "{text}"'


# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)




# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

