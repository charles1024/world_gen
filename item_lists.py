import sqlite3
from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base
from wdb_classes import  *
# Create and engine and get the metadata
Base = declarative_base()
engine = create_engine('test.db')
metadata = MetaData(bind=engine)



class AutoTable(Base):
    def __init__(self, tablename):
        self.__table__ = Table(tablename,  metadata, autoload=True)

    def rows(self):
        return self.__table__

    def item(self, id):
        return self.__table__.select([self.__table__]).where(self.__table__.c.id == id)



########################################################
#   RO TABLES
########################################################
class TableSettlementType(AutoTable):
    def __init__(self):
        super(TableSettlementType, self).__init__('settlement_type')


class TableSettlementFreq(AutoTable):
    def __init__(self):
        super(TableSettlementFreq, self).__init__('settlement_frequency')


class TablePopDensity(AutoTable):
    def __init__(self):
        super(TablePopDensity, self).__init__('pop_density')


class TableOccupationTypes(AutoTable):
    def __init__(self):
        super(TableOccupationTypes, self).__init__('occupation_types')


class TableOccupations(AutoTable):
    def __init__(self):
        super(TableOccupations, self).__init__('occupations')


class TableNobelPositionTypes(AutoTable):
    def __init__(self):
        super(TableNobelPositionTypes, self).__init__('nobel_position_types')


class TableFortTypes(AutoTable):
    def __init__(self):
        super(TableFortTypes, self).__init__('fort_types')


class TableThugZeal(AutoTable):
    def __init__(self):
        super(TableThugZeal, self).__init__('thug_zeal')


class TableBuildingTypes(AutoTable):
    def __init__(self):
        super(TableBuildingTypes, self).__init__('builing_types')


class TableSettlementTypes(AutoTable):
    def __init__(self):
        super(TableSettlementTypes, self).__init__('settlement_type')


########################################################
#   Maps TABLES
########################################################




class TableSettlementMultiplierMap(AutoTable):
    def __init__(self):
        super(TableSettlementMultiplierMap, self).__init__('settlement_mult_map')

########################################################
#   Rw TABLES
########################################################
class TableWorlds(AutoTable):

    def __init__(self):
        super(TableWorlds, self).__init__('worlds')

    def add(self, name, notes=''):
        self.__table__.insert().values(name=name, notes='')

class TableKingdoms(AutoTable):

    def __init__(self, id_world):
        super(TableKingdoms, self).__init__('kingdoms')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_world == id_world)

    def add(self, name, id_world, notes=''):
        self.__table__.insert().values(name=name, id_world=id_world, notes='')




        
class TableRegions(AutoTable):

    def __init__(self,  id_kingdom):
        super(TableRegions, self).__init__('regions')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_kingdom == id_kingdom)


    def add(self, name, id_kingdom, notes=''):
        self.__table__.insert().values(name=name, id_kingdom=id_kingdom, notes='')

class TableSettlements(AutoTable):

    def __init__(self,  id_region):
        super(TableSettlements, self).__init__('settlements')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_region == id_region)


    def add(self, name, id_region, notes=''):
        self.__table__.insert().values(name=name, id_region=id_region, notes='')

class TableForts(AutoTable):

    def __init__(self,  id_region):
        super(TableForts, self).__init__('forts')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_region == id_region)


    def add(self, name, id_region, notes=''):
        self.__table__.insert().values(name=name, id_region=id_region, notes='')


class TableBuildings(AutoTable):
    def __init__(self, id_settlement):
        super(TableBuildings, self).__init__('buildings')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_settlement == id_settlement)

    def add(self, name, id_settlement, notes=''):
        self.__table__.insert().values(name=name, id_settlement=id_settlement, notes='')

class TableShops(AutoTable):

    def __init__(self,  id_building):
        super(TableShops, self).__init__('shops')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_building == id_building)


    def add(self, name, id_region, notes=''):
        self.__table__.insert().values(name=name, id_region=id_region, notes='')




class TableNobelHouses(AutoTable):
    def __init__(self,  id_kingdom):
        super(TableNobelHouses, self).__init__('nobelhouses')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_kingdom == id_kingdom)



class TableFamily(AutoTable):
    def __init__(self,  id_settlement):
        super(TableFamily, self).__init__('families')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_settlement == id_settlement)


class TableNpc(AutoTable):
    def __init__(self,  id_family):
        super(TableNpc, self).__init__('npcs')
        self.__table__ = self.__table__.select([self.__table__]).where(self.__table__.c.id_family == id_family)



        
class TableNpcOwnedBuildingsMap(AutoTable):
    def __init__(self):
        super(TableNpcOwnedBuildingsMap, self).__init__('map_npc_owned_buildings')
        
    def items(self):
        return self.__table__

