from flask import Flask, render_template, request

app = Flask(__name__)

# Simple fixed rates (for demo)
rates = {
    'USD': 1.0,
    'EUR': 0.9,
    'INR': 75.0,
    'JPY': 110.0
}

@app.route('/', methods=['GET', 'POST'])
def converter():
    converted_amount = None
    if request.method == 'POST':
        amount = float(request.form.get('amount', 0))
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')

        if from_currency in rates and to_currency in rates:
            # Convert amount to USD first, then to target currency
            amount_in_usd = amount / rates[from_currency]
            converted_amount = round(amount_in_usd * rates[to_currency], 2)
    print("in currency")
    return render_template('currency_converter.html', rates=rates, result=converted_amount)

if __name__ == '__main__':
    app.run(port=5002,debug=True)
