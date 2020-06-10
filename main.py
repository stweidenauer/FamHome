from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/user')
def user():
    return render_template('User.html')


if __name__ == '__main__':
    app.run(debug=True, port=8400)
