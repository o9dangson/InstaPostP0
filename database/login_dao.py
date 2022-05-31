from database.connection import get_connection
from database.login_dto import Login
import psycopg2

def select_login_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE user_id = '{user_id}';"

    try:
        cursor.execute(qry)

        record = cursor.fetchone()
        if record is None:
            return None
        else:
            return Login(record[0], record[1], record[2])
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_login(user, pw):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE username ='{user}' AND password ='{pw}';"

    try:
        cursor.execute(qry)

        record = cursor.fetchone()
        if record is None:
            return None
        else:
            return Login(record[0], record[1], record[2])
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_login_by_user(user):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE username ='{user}';"

    try:
        cursor.execute(qry)

        record = cursor.fetchone()
        if record is None:
            return None
        else:
            return Login(record[0], record[1], record[2])
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_login(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO user_table VALUES(default, %s, %s) RETURNING user_id;"

    try:
        cursor.execute(qry, (username, password))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
        return None
    finally:
        if connection is not None:
            connection.close()

def remove_login(varName, value):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"DELETE FROM user_table WHERE {varName} = '{value}';"
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