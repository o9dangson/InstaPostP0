from database.connection import get_connection
from database.post_dto import Post
import psycopg2

def insert_post(user_id, title, desc, date):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO post_table VALUES(default, %s, %s, %s, %s) RETURNING post_id;"

    try:
        cursor.execute(qry, (user_id, title, desc, date))
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

def select_post_by_post_id(post_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM post_table WHERE post_id = '{post_id}';"

    try:
        cursor.execute(qry)

        record = cursor.fetchone()
        if record is None:
            return None
        else:
            return Post(record[0], record[1], record[2], record[3], record[4])
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_post_list_by_user_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM post_table WHERE user_id = '{user_id}';"

    try:
        cursor.execute(qry)
        list_of_posts = []
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            else:
                list_of_posts.append( Post(record[0], record[1], record[2], record[3], record[4]) )
        return list_of_posts
    except(psycopg2.DatabaseError) as error:
        print(error)
        return None
    finally:
        if connection is not None:
            connection.close()

def update_post(post_obj):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"UPDATE post_table SET post_title='{post_obj.post_title}', post_desc='{post_obj.post_desc}' WHERE post_id = '{post_obj.post_id}';"

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

def remove_post(varName, value):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"DELETE FROM post_table WHERE {varName} = '{value}';"
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