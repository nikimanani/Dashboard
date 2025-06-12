from flask import Flask, render_template, redirect
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for CSRF protection

@app.route('/', methods=['GET', 'POST'])
def register():
    print("in register")
    form = RegistrationForm()
    if form.validate_on_submit():
        return f"Successfully registered: {form.username.data}"
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
