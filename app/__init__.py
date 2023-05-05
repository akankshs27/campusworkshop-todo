"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaagme7avj5o48sq5o0-a.oregon-postgres.render.com",
        database="task_8dd9",
        user="task_8dd9_user",
        password="uWUeegzamiUDVgeIjWKfOk8K650mLhKp")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
