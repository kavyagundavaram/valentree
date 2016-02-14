from flask import Flask, render_template, flash
import flask.ext.login as flask_login
import flask
import os
import csv

users = {}
app = Flask(__name__)

f = open("env_var.txt", "r")
app.secret_key = f.readline()
f.close()

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

def parse():
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users[row['user_num']] = {
                "user_name": row['user_name'],
                "match": {
                    "match_name": row['match_name'],
                    "match_school": row['match_school'],
                    "interest": row['interest'],
                    "day": row['day'],
                    "time": row['time'],
                    "airport": row['airport'],
                    "matched_num": row["matched_num"]
                }
            }


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
    user.is_authenticated = request.form['phoneNum'] in users.keys()

    return user

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template("login.html")

    phoneNum = flask.request.form['phoneNum']
    if flask.request.form['phoneNum'] in users.keys():
        user = User()
        user.id = phoneNum
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))
    
    flash('Please use the number you entered in the TypeForm')
    return flask.redirect(flask.url_for('login'))

@app.route("/logout")
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('login'))

@app.route('/protected')
@flask_login.login_required
def protected():
    return render_template('protected.html')

if __name__ == '__main__':
    parse()
    app.debug = True
    app.run()
