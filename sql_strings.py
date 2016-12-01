

########################################################
#   BASE VALUES
########################################################



TBL_SETTLEMENT_TYPE_CREATE = '''CREATE TABLE settlement_type (id INT AUTO INCREMENT,
	  label TEXT,
	  size INT,
	 PRIMARY KEY (id ASC)
	 )'''

TBL_SETTLEMENT_TYPE_POPULATE = '''INSERT INTO settlement_type (label, size)
(throp_small',10),
(throp_avg',30),
(throp_large',50),
(village_small',100),
(village_avg',300),
(village_large',500),
(town_small',1000),
(town_avg',3000),
(town_large',5000),
(city_small',10000),
(city_avg',15000),
(city_large',50000),
(metropolis',100000)'''


TBL_SETTLEMENT_FREQ_MAP_CREATE = '''CREATE TABLE settlement_frequency (
      id_settelment_type INT,
      kindom_pop INT,
	  freq_mult INT,
	  FOREIGN KEY (id_settelment_type) REFERENCES settlement_type(id)
	 )'''
TBL_SETTLEMENT_FREQ_POPULATE = '''INSERT INTO settlement_frequency  VALUES (3,15000,0.294),
(4,15000,0.49),
(5,15000,0.196),
(6,15000,0),
(7,15000,0),
(8,15000,0),
(9,15000,0),
(10,15000,0),
(11,15000,0),
(12,15000,0),
(3,300000,0.267),
(4,300000,0.445),
(5,300000,0.178),
(6,300000,0.027),
(7,300000,0.045),
(8,300000,0.018),
(9,300000,0),
(10,300000,0),
(11,300000,0),
(12,300000,0),
(3,2400000,0.267),
(4,2400000,0.445),
(5,2400000,0.178),
(6,2400000,0.027),
(7,2400000,0.045),
(8,2400000,0.018),
(9,2400000,0.009),
(10,2400000,0.015),
(11,2400000,0.006),
(12,10000000,0.005)'''

TBL_POP_DENSITY_CREATE =  '''CREATE TABLE pop_density (id INT AUTO INCREMENT,
 density_multiplier INT,
    label TEXT,
	 PRIMARY KEY (id ASC)
	 )'''

TBL_POP_DENSITY_POPULATE = '''INSERT INTO pop_density (density_multiplier, label) VALUES (10,'inhospitable'),(20,'arid'),(40,'adaquate'),(60,'ample'),(80,'abundant'),(100,'fertile'),(120,'idyllic')'''


TBL_OCCUPATION_TYPES_CREATE =   '''CREATE TABLE occupation_types (id INT AUTO INCREMENT,
     label TEXT,
	 PRIMARY KEY (id ASC)
	 )'''

TBL_OCCUPATION_TYPES_POPULATE = '''INSERT INTO occupation_types (label) VALUES ('other'),('freeholder'),('clergy'),('officer')'''


TBL_OCCUPATIONS_CREATE = '''CREATE TABLE occupations (id INT AUTO INCREMENT,
    id_category INT,
    label TEXT,
     base_mult INT,
     is_industry INT,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY (id_category) REFERENCES occupation_types(id)
	 )'''

TBL_OCCUPATIONS_POPULATE = '''INSERT INTO occupations (id_category, label, base_mult, is_industry) VALUES
(1,'adventurers',0.00033,0),(1,'apothecaries',0.00036,0),(1,'armourers',0.00067,0),(1,'artists',0.0005,0),(1,'butchers',0.00091,1),(1,'chandlers',0.00167,0),(1,'charcoalers',0.0025,0),(1,'cobblers',0.00667,0),(1,'entertainers',0.00083,0),(1,'foresters',0.00125,0),(1,'furriers',0.004,0),(1,'glassworkers',0.00105,0),(1,'innkeepers',0.0005,0),(1,'jewelers',0.0025,0),(1,'litigants',0.00125,0),(1,'locksmiths',0.00056,0),(1,'masons',0.002,0),(1,'metalsmiths',0.00333,1),(1,'millers',0.004,1),(1,'ostlers',0.00167,1),(1,'outfitters',0.00067,0),(1,'physicians',0.00167,0),(1,'potters',0.00222,0),(1,'roofers',0.00056,0),(1,'ropemakers',0.00056,0),(1,'sages',0.00056,0),(1,'salters',0.00167,1),(1,'scribes',0.0005,0),(1,'shipwrights',0.00042,1),(1,'tailors',0.004,0),(1,'tanners',0.00083,1),(1,'taverns',0.00222,0),(1,'teamsters',0.00071,0),(1,'timberwrights',0.00143,1),(1,'tinkers',0.00125,0),(1,'vintners',0.00111,0),(1,'weaponcrafters',0.001,1),(1,'weavers',0.00167,0),(1,'woodcrafters',0.00333,0),(1,'yeomen',0.00222,0),(2,'clergy',0.00833,0),(2,'priest',0.03333,0),(0,'hierling',0.00333,0),(3,'reeve',0.0125,0),(3,'messor',0.01333,0),(3,'woodward',0.01429,0),(3,'constable',0.01111,0),(0,'university',0.00000003663003663,0)'''



TBL_NOBEL_POSITION_TYPES_CREATE = '''CREATE TABLE nobel_position_types (id INT AUTO INCREMENT,
     label TEXT,
	 PRIMARY KEY (id ASC)
	 )'''

#TBL_OCCUPATION_TYPES_POPULATE = '''INSERT INTO occupation_types (label) VALUES ('Emperor'),('King'),('Grand Duke'),
#('Archduke'),('Duke'),('Elector'),
#('Prince'),('Viceroy'),('Marquess'),
#('Count'),('Viscount'),('Baron'),
#('Baronet'),('Knight'),('Esquire')'''
TBL_NOBEL_POSITION_TYPES_POPULATE = '''INSERT INTO nobel_position_types (label) VALUES ('Emperor'),('King'),('Prince'),('Duke'),('Earl/Count'),('Baron'),('Knight'),('Esquire')'''


TBL_FORT_TYPES_CREATE= '''CREATE TABLE fort_types (id INT AUTO INCREMENT,
     label TEXT,
     base_mult INT,
	 PRIMARY KEY (id ASC)
	 )'''
TBL_FORT_TYPES_POPULATE = '''INSERT INTO fort_types (label, base_mult) VALUES ('castles', 0.2),('keeps', 0.5),('tower', .03)'''

TBL_THUG_ZEAL_CREATE = '''CREATE TABLE thug_zeal (id INT AUTO INCREMENT,
     label TEXT,
     val INT,
	 PRIMARY KEY (id ASC)
	 )'''

TBL_THUG_ZEAL_POPULATE = '''INSERT INTO thug_zeal (label, val) VALUES
('none', 0),
('little to none', 0.52),
('indifferent', .5),
('undependable', .75),
('typical', 1),
('zealous', 1.5),
('oppressive', 2),
('tyrannical', 3)
'''
TBL_BUILDING_TYPES_CREATE = '''CREATE TABLE builing_types (id INT AUTO INCREMENT,
	  label TEXT ,
	 PRIMARY KEY (id ASC)
	 )'''
TBL_BUILDING_TYPES_POPULATE = '''INSERT INTO builing_types (label) VALUES ('other'),('freeholder'),('clergy'),('officer'),('industry'),('citizen')'''
########################################################
#   DATA TABLES
########################################################

TBL_WORLDS_CREATE = '''CREATE TABLE worlds ( id INT AUTO INCREMENT,
	  name TEXT ,
	  notes TEXT ,
	 PRIMARY KEY (id ASC))'''
TBL_KINDOMS_CREATE = '''CREATE TABLE kingdoms (id INT AUTO INCREMENT,
	  id_world INT,
	 name TEXT ,
	 age INT  ,
	 size INT  ,
	  notes TEXT ,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY(id_world) REFERENCES worlds(id)
	 )'''
TBL_REGIONS_CREATE = '''CREATE TABLE regions (id INT AUTO INCREMENT,
	  id_kingdom INT ,
	 name TEXT ,
	  density INT ,
	  size INT ,
	  notes TEXT ,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY(id_kingdom) REFERENCES kingdoms(id)
	 )'''
TBL_SETTLEMENTS_CREATE = '''CREATE TABLE settlements (id INT AUTO INCREMENT,
	  id_region INT ,
	 name TEXT ,
	  type INT ,
	  population INT ,
	   notes TEXT ,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY(id_region) REFERENCES regions(id)
	 )'''
TBL_FORTS_CREATE = '''CREATE TABLE forts (id INT AUTO INCREMENT,
	  id_region INT ,
	  id_settlement INT ,
	 name TEXT ,
	  type INT ,
	  population INT , 
	  notes TEXT ,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY(id_region) REFERENCES regions(id) ,
	 FOREIGN KEY(id_settlement) REFERENCES settlements(id)
	 )'''



TBL_BUILDINGS_CREATE= '''CREATE TABLE buildings (id INT AUTO INCREMENT,
	  id_settlement INT ,
	  id_type INT ,
	 name TEXT ,
	  notes TEXT ,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY(id_settlement) REFERENCES settlements(id) ,
	FOREIGN KEY(id_type) REFERENCES builing_types(id)
	 )'''
TBL_SHOPS_CREATE = '''CREATE TABLE shops (id INT AUTO INCREMENT,
	  id_building INT ,
	 name TEXT ,
	   type INT ,
	  sell_variation INT ,
	  notes TEXT ,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY(id_building) REFERENCES buildings(id)
	 )'''
TBL_NOBELHOUSES_CREATE = '''CREATE TABLE nobelhouses (id INT AUTO INCREMENT,
	  id_kingdom INT ,
	   level INT ,
	  size INT ,
	  name INT ,
	  notes TEXT ,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY(id_kingdom) REFERENCES kingdoms(id)
	 )'''


TBL_FAMILY_CREATE =  '''CREATE TABLE families (id INT AUTO INCREMENT,
	   id_house INT ,
	    id_settlement INT ,
	   id_shop INT ,
	  name INT ,
	  notes TEXT ,
	 PRIMARY KEY (id ASC) ,
	 FOREIGN KEY(id_house) REFERENCES buildings(id) ,
	  FOREIGN KEY(id_shop) REFERENCES shops(id),
	    FOREIGN KEY(id_settlement) REFERENCES settlements(id)
	 )'''

TBL_NPC_CREATE = '''CREATE TABLE npcs (id INT AUTO INCREMENT,
	  firstname TEXT ,
	 id_family INT ,
	   title TEXT ,
	   race TEXT
	   gender TEXT ,
	   class TEXT,
	   level INT,
	  id_profession INT,
	  description TEXT,
	  notes TEXT,
	 PRIMARY KEY (id) ,
	 FOREIGN KEY(id_family) REFERENCES families(id)
	 )'''



########################################################
#   MAP TABLES
########################################################

TBL_SETTLEMENT_MULTIPLIER_MAP = '''CREATE TABLE settlement_mult_map ( id_settelment INT,
     min_pop INT,
	  max_pop INT,
    base_mult INT,
	 FOREIGN KEY (id_settelment) REFERENCES settlement_type(id)
	 )'''
TBL_MAP_NPC_OWNED_BUIDINGS_CREATE = '''CREATE TABLE map_npc_owned_buildings (
     id_npc INT,
      id_building INT,
	 	FOREIGN KEY(id_npc) REFERENCES npcs(id) ,
	 	FOREIGN KEY(id_building) REFERENCES buildings(id)
	 )'''