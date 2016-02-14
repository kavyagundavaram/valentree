from flask import Flask, render_template, flash
import flask
import flask.ext.login as flask_login
import os

users = ['9171234567']
app = Flask(__name__)

f = open("env_var.txt", "r")
app.secret_key = f.readline()
f.close()

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(phoneNum):
    if phoneNum not in users:
        return flask.redirect(flask.url_for('login'))

    user = User()
    user.id = phoneNum
    return user

@login_manager.request_loader
def request_loader(request):
    phoneNum = request.form.get('phoneNum')
    if phoneNum not in users:
        return flask.redirect(flask.url_for('login'))

    user = User()
    user.id = phoneNum

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['phoneNum'] == users[phoneNum]

    return user

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template("login.html")

    phoneNum = flask.request.form['phoneNum']
    if flask.request.form['phoneNum'] in users:
        user = User()
        user.id = phoneNum
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))
    
    flash('Please use the number you entered in the TypeForm')
    return flask.redirect(flask.url_for('login'))



@app.route('/protected')
@flask_login.login_required
def protected():
    return render_template('protected.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
