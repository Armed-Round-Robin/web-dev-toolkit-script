from flask import Flask, request

app = Flask(__name__)

# Store for cart items
cart = []

@app.route('/add_item', methods=['POST'])
def add_item():
    item_id = request.json.get('item_id')
    cart.append(item_id)
    # update inventory, etc.
    return {'status': 'Item added', 'current_cart': cart}

if __name__ == '__main__':
    app.run()
