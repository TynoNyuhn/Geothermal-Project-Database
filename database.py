import psycopg2
import psycopg2.extras
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


hostname = os.environ.get("DB_HOST")
database = os.environ.get("DB_NAME")
username = os.environ.get("DB_USERNAME")
pwd = os.environ.get("DB_PASSWORD")
port_id = os.environ.get("DB_PORT")

conn = None
cur = None

def select_all_wells():
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
        cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        script = '''SELECT * FROM wells'''
        cur.execute(script)
        test = cur.fetchall()
        
        return test

    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    



