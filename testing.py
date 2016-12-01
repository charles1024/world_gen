from sql_strings import *


import sqlite3
from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_FILE = 'test.db'

#Create and engine and get the metadata
#Base = declarative_base()
#engine = create_engine('put your database connect string here')
#metadata = MetaData(bind=engine)


conn =sqlite3.connect(DATABASE_FILE)
c = conn.cursor()


########################################################
#   BASE VALUES
########################################################


c.execute(TBL_BUILDING_TYPES_CREATE)
c.execute(TBL_BUILDING_TYPES_POPULATE)

c.execute(TBL_SETTLEMENT_TYPE_CREATE)
c.execute(TBL_SETTLEMENT_TYPE_POPULATE)

c.execute(TBL_POP_DENSITY_CREATE)
c.execute(TBL_POP_DENSITY_POPULATE)

c.execute(TBL_OCCUPATION_TYPES_CREATE)
c.execute(TBL_OCCUPATION_TYPES_POPULATE)

c.execute(TBL_NOBEL_POSITION_TYPES_CREATE)
c.execute(TBL_NOBEL_POSITION_TYPES_POPULATE)

c.execute(TBL_THUG_ZEAL_CREATE)
c.execute(TBL_THUG_ZEAL_POPULATE)

c.execute(TBL_FORT_TYPES_CREATE)
c.execute(TBL_FORT_TYPES_POPULATE)

c.execute(TBL_OCCUPATIONS_CREATE)
c.execute(TBL_OCCUPATIONS_POPULATE)

c.execute(TBL_SETTLEMENT_FREQ_MAP_CREATE)
c.execute(TBL_SETTLEMENT_FREQ_POPULATE)

########################################################
#   DATA TABLES
########################################################

c.execute(TBL_WORLDS_CREATE)
c.execute(TBL_KINDOMS_CREATE)
c.execute(TBL_REGIONS_CREATE)
c.execute(TBL_SETTLEMENTS_CREATE)
c.execute(TBL_FORTS_CREATE)
c.execute(TBL_BUILDINGS_CREATE)
c.execute(TBL_SHOPS_CREATE)
c.execute(TBL_NOBELHOUSES_CREATE)
c.execute(TBL_FAMILY_CREATE)
c.execute(TBL_NPC_CREATE)
c.execute(TBL_SETTLEMENT_MULTIPLIER_MAP)
c.execute(TBL_MAP_NPC_OWNED_BUIDINGS_CREATE)