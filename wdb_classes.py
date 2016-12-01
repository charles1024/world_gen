

from item_lists import  *


tblWrld = TableWorlds()

class generic_item:
    def __init__(self, tableClass, id):
        self.data = tableClass.rows().select([tableClass.__table__]).where(tableClass.__table__.c.id == id)


class World(generic_item):

    def __init__(self, id):
        super(World, self).__init__(tblWrld, id)
        self.tbl_kingdoms = TableKingdoms(id_world=id).rows()

    def get_kingdoms(self):
        return self.tbl_kingdoms


class Kingdom(generic_item):
    def __init__(self, id, id_world):
        super(Kingdom, self).__init__(TableKingdoms(id_world), id)
        self.tbl_regions = TableRegions(id).rows()

    def get_regions(self):
        return self.tbl_kingdoms

class Region(generic_item):
    def __init__(self, id, id_kingdom):
        super(Region, self).__init__(TableRegions(id_kingdom), id)
        self.tbl_settlements = TableRegions(id).rows()
        self.tbl_settlements = TableForts(id).rows()

    def get_settlements(self):
        return self.tbl_settlements

    def get_forts(self):
        return self.tbl_kingdoms


class Settlement(generic_item):
    def __init__(self, id, id_region):
        super(Settlement, self).__init__(TableSettlements(id_region), id)



class Fort(generic_item):
    def __init__(self, id, id_region):
        super(Fort, self).__init__(TableForts(id_region), id)