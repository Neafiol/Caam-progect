
import sqlite3
from datetime import date
from peewee import *

db = SqliteDatabase('../db.sqlite3')

class Logs(Model):
    date=DateField()
    h=IntegerField()
    t=IntegerField()
    ah=IntegerField()
    at=IntegerField()
    l=IntegerField()

    class Meta:
        database = db
        db_table='Logs'


Logs.create_table()
# uncle_bob = Subs(name='Bob', tel_id=121212)
# uncle_bob.save()