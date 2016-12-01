import sqlite3
from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base


from item_lists import  *
from wdb_classes import *
class things:
    def __init__(self):
        self.worlds = TableWorlds()

    def new_world(self, name):
        self.worlds.items().insert().values(name=name, notes='')
        return World(self.worlds.items().select([self.worlds.c.id]).order_by(self.worlds.c.id.desc()).limit(1))

def do_stuff():
    world_name = 'myworld'
    kingdom_name = 'mykingdom'
    region_name = 'myregion'
    area_name = 'testarea'
    pop_density = 120
    physical_area = 1000
    area_age = 300

    village_count =




conn =sqlite3.connect('test.db')
c = conn.cursor()


class tbl_worlds(Base):
    __table__ = Table('worlds',
	 metadata,
	 autoload=True)

session = create_session(bind=engine)




class world():

    def __init__(self,
	 id):
        if

    def id(self):
        return self._id

    def name(self):
        return self._name

    def name(self,
	 new_name):
        self._name = new_name

    def notes(self):
        return self._notes

    def notes(self,
	 new_notes):
        self._notes = new_notes




