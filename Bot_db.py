import psycopg2

with psycopg2.connect(database="Bot_db", user="postgres", password="postgres") as conn:

def create_table_users():
    with conn.cursor() as cur:
        cur.execute(
            """CREATE TABLE IF NOT EXISTS users(
                id serial,
                first_name varchar(50) NOT NULL,
                last_name varchar(25) NOT NULL,
                user_id varchar(20) NOT NULL PRIMARY KEY,"""
        )
    print("[INFO] Table USERS was created.")

def add_data_users(first_name, last_name, user_id):
    with conn.cursor() as cur:
        cur.execute(
            f"""INSERT INTO users (first_name, last_name, user_id) 
            VALUES ('{first_name}', '{last_name}', '{user_id}');"""
        )