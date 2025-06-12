from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')  # This is a GET route for homepage
def home():
    return render_template('jsondemo.html')  # shows HTML form

@app.route('/api/info', methods=['POST'])  # POST route for API
def info():
    data = request.get_json()
    name = data['name']
    return jsonify({"message": f"Hello, {name}"})

if __name__ == '__main__':
    app.run(debug=True)
