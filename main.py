from flask import Flask, render_template, request, flash, redirect, url_for, sessions
import hashL as hL

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def route_main():
    return render_template('checking_password.html',
                           state='normal')


@app.route('/hash', methods=['POST'])
def route_hash_password():
    password = request.form.get('password1')
    hash_password = hL.hash_password(password)
    return render_template('checking_password.html',
                           hash_password=hash_password,
                           state='normal')


@app.route('/verify', methods=['POST'])
def route_verify_password():
    password = request.form.get('password2')
    hash_password = request.form.get('hashed')
    verified_password = hL.verify_password(password, hash_password)
    if verified_password is True:
        message = "It's a match!"
        state = 'correct'
    else:
        message = "Doesn't match :("
        state = 'incorrect'
    return render_template('checking_password.html',
                           message=message,
                           state=state)


#


if __name__ == "__main__":
    app.run(debug=True,
            host='127.0.0.1',
            port=5000)
