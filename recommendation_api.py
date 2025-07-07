from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load product data from a JSON file
try:
    with open('products.json', 'r') as f:
        products = json.load(f)
except FileNotFoundError:
    # Fallback sample data
    products = [
        {'id': 1, 'name': 'Tesla Coil Model', 'category': 'Electronics', 'price': 99.99},
        {'id': 2, 'name': 'Wireless Power Bank', 'category': 'Gadgets', 'price': 49.99},
        {'id': 3, 'name': 'Futuristic VR Headset', 'category': 'Gadgets', 'price': 199.99}
    ]

# Function for product recommendations based on preferences
def recommend_products(preferences):
    # Filter products matching user interests
    recs = [p for p in products if p['category'].lower() in [pref.lower() for pref in preferences]]
    return recs

# Optional: advanced filtering or ML suggestions can be added here later

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    preferences = data.get('preferences', [])
    
    if not preferences:
        return jsonify({"error": "Preferences list is empty or missing."}), 400
    
    recs = recommend_products(preferences)
    return jsonify({"recommendations": recs})

# Additional endpoint: get all products (with pagination)
@app.route('/products', methods=['GET'])
def get_products():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except ValueError:
        return jsonify({"error": "Invalid pagination parameters."}), 400
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(products[start:end])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
