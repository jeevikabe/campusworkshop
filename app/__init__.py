"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13ed33cv203buk2bp0-a.oregon-postgres.render.com",
        database="to_do_nryf",
        user="to_do_nryf_user",
        password="i9WrQxINiPGT377PAkoiUNKjGCHzEGSD")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
