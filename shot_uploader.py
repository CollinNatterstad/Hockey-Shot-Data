import psycopg2 as pg
import os
from dotenv import load_dotenv
load_dotenv()

def read_and_upload():
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_USER_PASS = os.getenv("DB_USER_PASS")
    DB_PORT = os.getenv("DB_PORT")
    
    conn = pg.connect(database = DB_NAME, user= DB_USER, password= DB_USER_PASS, host= DB_HOST, port= DB_PORT)
    cur =  conn.cursor()
    print('\nCreated Cursor object: ', cur)
    with open('d:/Coding Projects/Hockey Shot Data/Cleaned_Data/clean_shot_data_2007-2020.csv','r') as f:
        next(f)
        cur.copy_from(f,'shots',',')
    conn.commit()

    cur.close()
    print('\nClosed Cursor Object', cur)


if __name__ == '__main__':
    read_and_upload()

