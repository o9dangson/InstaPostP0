import psycopg2

def get_connection():
        connection = psycopg2.connect(
                database="postgres",
                user="postgres",
                password="password123",
                host="database-python.cbilxsioybab.us-east-2.rds.amazonaws.com",
                port="5432"
        )

        return connection

def teardown():
    qry = "drop table user_table, info_table, post_table;"
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(qry)
        return True
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
        return False
    finally:
        if connection is not None:
            connection.close()

def setup():
    #reset database
    qry_create = ["create table user_table(user_id serial primary key, username varchar(50) not null unique, password varchar(50) not null );","CREATE TABLE info_table(info_id serial PRIMARY KEY,user_id INT NOT NULL,super_user_id INT not null,first_name varchar(50) NOT NULL,last_name varchar(50) NOT NULL,FOREIGN KEY (user_id) REFERENCES user_table(user_id),foreign key (super_user_id) references user_table(user_id));","create table post_table(post_id serial primary key,user_id INT not null,post_title varchar(50) not null,post_desc varchar(200) not null,post_date date not null,foreign key (user_id) references user_table(user_id));"]
    #qry_create.append("create table user_table(user_id serial primary key, username varchar(50) not null unique, password varchar(50) not null );")
    #qry_create.append("CREATE TABLE info_table(info_id serial PRIMARY KEY,user_id INT NOT NULL,super_user_id INT not null,first_name varchar(50) NOT NULL,last_name varchar(50) NOT NULL,FOREIGN KEY (user_id) REFERENCES user_table(user_id),foreign key (super_user_id) references user_table(user_id));")
    #qry_create.append("create table post_table(post_id serial primary key,user_id INT not null,post_title varchar(50) not null,post_desc varchar(200) not null,post_date date not null,foreign key (user_id) references user_table(user_id));")

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(qry_create[0])
        cursor.execute(qry_create[1])
        cursor.execute(qry_create[2])
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
        return False
    finally:
        if connection is not None:
            connection.close()
    return True