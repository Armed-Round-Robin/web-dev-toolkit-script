from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {'id': 1, 'name': 'Tesla Coil Model', 'category': 'Electronics'},
    {'id': 2, 'name': 'Wireless Power Bank', 'category': 'Gadgets'},
    {'id': 3, 'name': 'Futuristic VR Headset', 'category': 'Gadgets'}
]

# Simple AI recommendation based on user interests
def recommend_products(preferences):
    recommendations = [p for p in products if p['category'] in preferences]
    return recommendations

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    prefs = data.get('preferences', [])
    recs = recommend_products(prefs)
    return jsonify(recs)

if __name__ == '__main__':
    app.run()
