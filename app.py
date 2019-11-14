from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "My first store",
        "items": [
            {
                "name": "Item1",
                "price": 15.99
            }
        ]
    }
]

# POST - used to receive data
# GET - used to send data back only


# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    # raise ValueError(f'Store {name} does not exist')
    return {"message": f'Store {name} was not found'}


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name, price):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            store_items = store["items"]
            return jsonify({"items": store_items})
    return {"message": f'Store {name} was not found to retrieve items'}


app.run(port=5000)
