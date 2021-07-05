# Flask app starts from this file
from flask import Flask

app = Flask(__name__)

stores = [
    {

    }

]

@app.route('/')
def root_path():
    return "Welcome to the home page."

@app.route('/store', methods = ['POST']) #Data - {'name' : 'store_name'}
def create_store():
    pass

@app.route('/store') #Return Data - all store names [store_name1, store_name2, .... ]
def get_stores():
    pass

@app.route('/store/<string:name>')
def get_store_info(name): #Returns - {'name' : 'store_name', 'items' : [ {'name' : 'item_name', 'price' : item_price} ]}
    pass

@app.route('/store/<string:name>/item', methods = ['POST'])
def store_item(name): #Adds item to the store. - {'name' : 'item_name', 'price' : item_price}
    pass

@app.route('/store/<string:name>/item')
def get_item(name): #Return - [{'item' : 'item_name', price : item_price}, ...]
    pass
app.run(port=9000)
