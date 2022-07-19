import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
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
<p>A prototype API for liquor bar code scanner.</p>'''


@app.route('/api/v1/resources/liquors/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('liquors.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_liquors = cur.execute('SELECT * FROM liquors;').fetchall()

    return jsonify(all_liquors)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/liquors', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')
    product_id = query_parameters.get('product_id')

    query = "SELECT * FROM liquors WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if product_id:
        query += ' product_id=? AND'
        to_filter.append(product_id)
    if not (id or name or product_id):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('liquors.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    response = flask.jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run()

