from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    # Validate the username and password
    # Your authentication logic goes here
    if username == 'admin' and password == 'admin123':
        return 'Login successful'
    else:
        return 'Invalid username or password'

@app.route('/forgot-password')
def forgot_password():
    return 'Forgot Password'

if __name__ == '__main__':
    app.run()
