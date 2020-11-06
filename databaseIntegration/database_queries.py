from typing import List, Dict


class Database:
    COLUMNS_HUMAN = [
        'human_id', 'gender', 'age', 'preliminary_diagnosis',
        'admission_to_the_hospital', 'arrival_date', 'approximate_growth', 'hair_type',
        'room_number', 'full_name'
    ]
    COLUMNS_ROOM = ['room_number', 'room_id', 'room_type', 'full_name',
                    'room_phone']
    COLUMNS_ARRIVAL = ['arrival_date', 'room_number', 'full_name', 'age']

    COLUMNS_FEMALE = ['arrival_date', 'full_name', 'age']

    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def human_add(self, human_id: int, gender: str, age: int, preliminary_diagnosis: str,
                  admission_to_the_hospital: str, arrival_date: str, approximate_growth: int,
                  hair_type: str, room_number: int, full_name: str):
        add_human_query = """
        INSERT INTO table_human_data (human_id, gender, age, preliminary_diagnosis,admission_to_the_hospital , 
        arrival_date,approximate_growth, hair_type ,room_number, full_name)
        VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = [human_id, gender, age, preliminary_diagnosis, admission_to_the_hospital,
               arrival_date, approximate_growth, hair_type, room_number, full_name]
        self.cursor.execute(add_human_query, val)
        self.connection.commit()

        human_id = self.cursor.lastrowid

    def human_data_upgrade(self, human_id: int, gender: str, age: int, preliminary_diagnosis: str,
                           admission_to_the_hospital: str, arrival_date: str, approximate_growth: int,
                           hair_type: str, room_number: int, full_name: str):
        change_human_query = """
            UPDATE table_human_data
            SET human_id=%s, gender = %s, age = %s, preliminary_diagnosis = %s, admission_to_the_hospital = %s,
               arrival_date = %s, approximate_growth = %s, hair_type = %s, room_number = %s, 
               full_name = %s
            WHERE table_human_data.human_id = %s;
            """
        val = [human_id, gender, age, preliminary_diagnosis, admission_to_the_hospital,
               arrival_date, approximate_growth, hair_type, room_number, full_name, human_id]
        self.cursor.execute(change_human_query, val)
        self.connection.commit()

    def get_all_humans(self) -> List[Dict]:
        get_all_humans_query = """
            SELECT *
            FROM table_human_data
         """

        self.cursor.execute(get_all_humans_query)
        all_humans = self.cursor.fetchall()

        all_humans = [dict(zip(self.COLUMNS_HUMAN, curr_human)) for curr_human in all_humans]
        return all_humans

    def human_delete(self, human_id: int):
        delete_human_query = """
            DELETE FROM table_human_data
            WHERE human_id = %s;
            """
        val = [human_id]
        self.cursor.execute(delete_human_query, val)
        self.connection.commit()

    def room_add(self, room_number: int, room_id: str, room_type: str, full_name: str,
                 room_phone: int):
        add_room_query = """
            INSERT INTO table_room_data (room_number, room_id, room_type, full_name,
                      room_phone)
            VALUES (%s,%s, %s, %s, %s)
            """
        val = [room_id, room_number, room_type, full_name,
               room_phone]
        self.cursor.execute(add_room_query, val)
        self.connection.commit()

    def room_data_upgrade(self, room_number: int, room_id: str, room_type: str, full_name: str,
                          room_phone: int):
        change_room_query = """
            UPDATE table_room_data
            SET room_number=%s, room_id=%s, room_type=%s, full_name=%s,
                      room_phone=%s
            WHERE table_room_data.room_id = %s;
            """
        val = [room_number, room_id, room_type, full_name,
               room_phone, room_id]
        self.cursor.execute(change_room_query, val)
        self.connection.commit()

    def room_delete(self, room_id: int):
        delete_room_query = """
            DELETE FROM table_room_data
            WHERE room_id = %s;
            """
        val = [room_id]
        self.cursor.execute(delete_room_query, val)
        self.connection.commit()

    def get_all_rooms(self) -> List[Dict]:
        get_all_rooms_query = """
            SELECT *
            FROM table_room_data
         """

        self.cursor.execute(get_all_rooms_query)
        all_rooms = self.cursor.fetchall()

        all_rooms = [dict(zip(self.COLUMNS_ROOM, curr_room)) for curr_room in all_rooms]
        return all_rooms

    def phone_and_room_check(self, full_name: str):
        phone_and_room_check_query = """
        SELECT room_number,room_phone
        FROM table_room_data WHERE table_room_data.full_name=%s
        """
        val = [full_name]
        self.cursor.execute(phone_and_room_check_query, val)
        self.connection.commit()

    def arrival_date_check(self, arrival_date: str) -> List[Dict]:
        arrival_date_check_query = """
        SELECT arrival_date, room_number, full_name, age
        FROM table_human_data WHERE table_human_data.arrival_date=%s
        """
        val = [arrival_date]
        self.cursor.execute(arrival_date_check_query, val)
        all_arrivals = self.cursor.fetchall()
        all_arrivals = [dict(zip(self.COLUMNS_ARRIVAL, curr_arrival)) for curr_arrival in all_arrivals]
        return all_arrivals

    def female_age_check(self, age: int) -> List[Dict]:
        female_age_check_query = """
        SELECT arrival_date, full_name, age
        FROM table_human_data WHERE table_human_data.gender='F' and age<=%s;
        """
        val = [age]
        self.cursor.execute(female_age_check_query, val)
        all_females = self.cursor.fetchall()
        all_females = [dict(zip(self.COLUMNS_FEMALE, curr_female)) for curr_female in all_females]
        return all_females
