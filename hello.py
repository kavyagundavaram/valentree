from flask import Flask, render_template
import flask
import flask.ext.login as flask_login

app = Flask(__name__)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
            <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='pw' id='pw' placeholder='password'></input>
                <input type='submit' name='submit'></input>
            </form>
            '''

@app.route('/')
def index():
    return "ayy lmao"

if __name__ == '__main__':
    app.debug = True
    app.run()
