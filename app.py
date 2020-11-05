from flask import Flask, render_template, url_for, Blueprint, request
from databaseIntegration.database_queries import Database
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
    human = Database(connection=connection, cursor=cursor)
    all_human = human.get_all_humans()
    context = {
        'all_human': all_human
    }
    return render_template("human_data_table.html", **context)


@app.route('/human_data_table/update', methods=["POST", "GET"])
def human_table_update():
    human = Database(connection=connection, cursor=cursor)
    if request.method == "POST":

@app.route('/room_data_table')
def room_table():
    room = Database(connection=connection, cursor=cursor)
    all_rooms = room.get_all_rooms()
    context = {
        'all_rooms': all_rooms
    }
    return render_template("room_data_table.html", **context)


if __name__ == '__main__':
    app.run()
