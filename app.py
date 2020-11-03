from flask import Flask, render_template, url_for, Blueprint
from databaseIntegration.human_data import Human
from databaseIntegration.database import create_connection, close_connection
from databaseIntegration.database_config import Config

app = Flask(__name__)
connection, cursor = create_connection(host=Config.database_host,
                                       port=Config.database_port,
                                       user=Config.database_user,
                                       password=Config.database_password,
                                       database=Config.database_name)
blue_print = Blueprint('clinic', __name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/human_data_table')
def human_table():
    human = Human(connection=connection, cursor=cursor)
    all_human = human.get_all_humans()
    context = {
        'all_human': all_human
    }
    return render_template("human_data_table.html", **context)


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
