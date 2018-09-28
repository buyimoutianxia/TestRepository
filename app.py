from flask import Flask
from flask import request,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template("form.html")

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return render_template('signin_ok.html', username='admin')
    return render_template('form.html', message = 'Bad UserName or PassWord', username = 'admin')

if __name__ == '__main__':
    app.run()
