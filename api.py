import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
liquors = [
    {'id' : 0, 
     'name': 'Barefoot Wine',
     'price': '12',
     'product_id': '12345678'},
    {'id': 1, 
     'name': 'Grey Goose Vodka',
     'price': '50',
     'product_id': '12345671'},
    {'id' : 2,
     'name': 'Titos Vodka',
     'price': '20',
     'product_id': '12345672'},
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for liqour bar scanner.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/liquors/all', methods=['GET'])
def api_all():
    return jsonify(liquors)

@app.route('/api/v1/resources/liquors', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for liquor in liquors:
        if liquor['id'] == id:
            results.append(liquor)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()