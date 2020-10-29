from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/about')
def about():
    return 'about!'
#
#
# @app.route('/room_data')
# def about():
#     return 'about!'
#
#
# @app.route('/room_transfer')
# def about():
#     return 'about!'
#
#
# @app.route('/hospital_discharge')
# def about():
#     return 'about!'


if __name__ == '__main__':
    app.run()
