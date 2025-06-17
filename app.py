from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    
    apps = [
    {'name': '💱Currency Converter', 'url': 'https://currency-converter-x250.onrender.com'},
    {'name': '🧮Calculator', 'url': 'https://calculator-z89q.onrender.com'}
]

    print("✅ Route hit: Rendering dashboard with apps:", apps)
    return render_template('dashboard.html', apps=apps)

if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
