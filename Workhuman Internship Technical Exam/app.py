
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

countries = [
    "Albania", "Andorra", "Australia", "Brazil", "Belgium", "Canada", 
    "China", "France", "Germany", "India", "Indonesia", "Ireland", 
    "Italy", "Japan", "Kenya", "Luxembourg", "Mexico", "New Zealand", 
    "Nigeria", "Portugal", "Russia", "South Africa", "South Korea", 
    "Spain", "Sweden", "Thailand", "Ukraine", "United Kingdom", 
    "United States of America", "Vietnam", "Zambia"
]

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = [country for country in countries if query in country.lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)