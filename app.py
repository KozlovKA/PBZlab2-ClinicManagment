from flask import Flask, render_template, url_for, Blueprint, request, redirect
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
        human_id = request.form["human_id"]
        gender = request.form["gender"]
        age = request.form["age"]
        preliminary_diagnosis = request.form['preliminary_diagnosis']
        admission_to_the_hospital = request.form['admission_to_the_hospital']
        arrival_date = request.form['arrival_date']
        approximate_growth = request.form['approximate_growth']
        hair_type = request.form["hair_type"]
        room_number = request.form["room_number"]
        full_name = request.form["full_name"]
        # try:
        human.human_data_upgrade(human_id, gender, age, preliminary_diagnosis, admission_to_the_hospital,
                                 arrival_date, approximate_growth, hair_type, room_number, full_name)

        # except:
        #     return "Ошбика"
    return redirect('/human_data_table')


@app.route('/human_data_table/add_human', methods=["POST", "GET"])
def human_table_add():
    human = Database(connection=connection, cursor=cursor)
    if request.method == "POST":
        human_id = request.form["human_id"]
        gender = request.form["gender"]
        age = request.form["age"]
        preliminary_diagnosis = request.form['preliminary_diagnosis']
        admission_to_the_hospital = request.form['admission_to_the_hospital']
        arrival_date = request.form['arrival_date']
        approximate_growth = request.form['approximate_growth']
        hair_type = request.form["hair_type"]
        room_number = request.form["room_number"]
        full_name = request.form["full_name"]
        # try:
        human.human_add(human_id, gender, age, preliminary_diagnosis, admission_to_the_hospital,
                        arrival_date, approximate_growth, hair_type, room_number, full_name)

        # except:
        #     return "Ошбика"
    return redirect('/human_data_table')


@app.route('/human_data_table/delete_human', methods=["POST", "GET"])
def human_table_delete():
    human = Database(connection=connection, cursor=cursor)
    if request.method == "POST":
        human_id = request.form["human_id"]

        human.human_delete(human_id)

    return redirect('/human_data_table')


@app.route('/room_data_table')
def room_table():
    room = Database(connection=connection, cursor=cursor)
    all_rooms = room.get_all_rooms()
    context = {
        'all_rooms': all_rooms
    }
    return render_template("room_data_table.html", **context)


@app.route('/room_data_table/update', methods=["POST", "GET"])
def rooms_table_update():
    human = Database(connection=connection, cursor=cursor)
    if request.method == "POST":
        room_number = request.form["room_number"]
        room_id = request.form["room_id"]
        room_type = request.form["room_type"]
        full_name = request.form['full_name']
        room_phone = request.form['room_phone']

        human.room_data_upgrade(room_number, room_id, room_type, full_name, room_phone)

    return redirect('/room_data_table')


@app.route('/room_data_table/add', methods=["POST", "GET"])
def rooms_table_add():
    human = Database(connection=connection, cursor=cursor)
    if request.method == "POST":
        room_number = request.form["room_number"]
        room_id = request.form["room_id"]
        room_type = request.form["room_type"]
        full_name = request.form['full_name']
        room_phone = request.form['room_phone']

        human.room_add(room_number, room_id, room_type, full_name, room_phone)

    return redirect('/room_data_table')


@app.route('/room_data_table/add', methods=["POST", "GET"])
def room_delete():
    human = Database(connection=connection, cursor=cursor)
    if request.method == "POST":
        room_id = request.form["room_id"]
        human.room_delete(room_id)

    return redirect('/room_data_table')


@app.route('/arrival_human_check')
def arrival_human_check():
    arrival = Database(connection=connection, cursor=cursor)
    all_arrivals = arrival.arrival_date_check("2020-10-08")
    context = {
        'all_arrivals': all_arrivals
    }
    return render_template("human_arrival_table.html", **context)


@app.route('/female_age_check')
def female_age_check():
    females = Database(connection=connection, cursor=cursor)
    all_females = females.female_age_check(18)
    context = {
        'all_females': all_females
    }
    return render_template("female_age_table.html", **context)


if __name__ == '__main__':
    app.run()
