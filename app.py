# Flask app starts from this file
from flask import Flask, jsonify, request

app = Flask(__name__)

stores = []

@app.route('/')
def root_path():
    return "Welcome to the home page."

@app.route('/store', methods = ['POST']) #Data - {'name' : 'store_name'}
def create_store():
    request_data = request.get_json()
    store_data = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(store_data)

    return jsonify(store_data)

@app.route('/store') #Return Data - all store names [store_name1, store_name2, .... ]
def get_stores():
    return jsonify({'stores' : stores})

@app.route('/store/<string:name>')
def get_store_info(name): #Returns - [{'name' : 'store_name', 'items' : [ {'name' : 'item_name', 'price' : item_price} ]}]
    for store in stores:
        if store['name'].upper() == name.upper():
            return jsonify(store)
    return jsonify({'message' : f'{name} not found.'})

@app.route('/store/<string:name>/item', methods = ['POST'])
def store_item(name): #Adds item to the store. - {'name' : 'item_name', 'price' : item_price}
    request_data = request.get_json()
    is_store = False
    for store in stores:
         if store['name'].upper() == name.upper():
             is_store = True
             store['items'].append(request_data)
             break
    return jsonify(request_data) if is_store else jsonify({'message' : f"{name} not found."})

@app.route('/store/<string:name>/item')
def get_items(name): #Return - [{'item' : 'item_name', price : item_price}, ...]
    for store in stores:
        if store['name'].upper() == name.upper():
            return jsonify({'items' : store['items']})
    return jsonify({'message': f'{name} not found.'})

app.run(port=9000)
