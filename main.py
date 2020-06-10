from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/user')
def user():
    return render_template('User.html')


if __name__ == '__main__':
    app.run(debug=True, port=8400)
