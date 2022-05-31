from database.connection import get_connection
from database.user_dto import User
import psycopg2

def select_user_by_info_id(info_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM info_table WHERE info_id = '{info_id}';"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_info = User(record[0], record[1], record[2], record[3], record[4])
            return user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_user_by_user_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM info_table WHERE user_id={user_id};"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_info = User(record[0], record[1], record[2], record[3], record[4])
            return user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_user_by_superUser(superUser_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM info_table WHERE super_user_id={superUser_id};"

    try:
        cursor.execute(qry)

        while True:
            records = cursor.fetchall()
            if records is None:
                return None
            list_of_user_info = []
            for record in records:
                user_info = User(record[0], record[1], record[2], record[3], record[4])
                list_of_user_info.append(user_info)
            return list_of_user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def insert_user(user_id, superUser_id, f_name, l_name):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO info_table VALUES(default, %s, %s, %s, %s) RETURNING info_id;"

    try:
        cursor.execute(qry, (user_id, superUser_id, f_name, l_name))
        info_id = cursor.fetchone()[0]
        connection.commit()
        return info_id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
        return None
    finally:
        if connection is not None:
            connection.close()

def remove_user_info(varName, value):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"DELETE FROM info_table WHERE {varName}='{value}';"

    try:
        cursor.execute(qry)
        connection.commit()
        return True
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
        return False
    finally:
        if connection is not None:
            connection.close()