import datetime
import os

import pytz
import psycopg2
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get("DATABASE_URI "))

user_timezone = pytz.timezone("US/Eastern")

new_post_content = input("Enter what you learned today: ")

new_post_date = user_timezone.locallize(datetime.datetime.now())
utc_post_date = new_post_date.astimezone(pytz.utc)

with connection:
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO posts (content, date) VALUES (%s, %s);",
            (new_post_content, utc_post_date.timestamp()))

with connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM posts;")
        for post in cursor:
            _id, content, timestamp = post
            naive_datetime = datetime.datetime.utcfromtimestamp(timestamp)
            utc_date = pytz.utc.localize(naive_datetime)
            local_date = utc_date.astimezone(user_timezone)
            print(local_date)
            print(content)
