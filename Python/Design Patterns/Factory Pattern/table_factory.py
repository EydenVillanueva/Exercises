from abc import ABCMeta, abstractstaticmethod

#Interface
class ITable(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_dimensions():
        """The Table Interface"""

#BigTable Class implements ITable interface
class BigTable(ITable):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80
    
    def get_dimensions(self):
        return { 'heigth' : self.height, 'width' : self.width, 'depth' : self.depth }

#MediumTable Class implements ITable interface
class MediumTable(ITable):

    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70
    
    def get_dimensions(self):
        return { 'heigth' : self.height, 'width' : self.width, 'depth' : self.depth }

#SmallTable Class implements ITable interface
class SmallTable(ITable):

    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 60
    
    def get_dimensions(self):
        return { 'heigth' : self.height, 'width' : self.width, 'depth' : self.depth }

#Factory Class
class TableFactory():
    
    @staticmethod
    def get_Table(Tabletype):
        try:

            if Tabletype == "BigTable":
                return BigTable()
            if Tabletype == "MediumTable":
                return MediumTable()
            if Tabletype == "SmallTable":
                return SmallTable()

            raise AssertionError("Table Not Found")

        except AssertionError as _a:
            print(_a)

if __name__ == "__main__":
    BTable = TableFactory.get_Table("BigTable")
    MTable = TableFactory.get_Table("MediumTable")
    STable = TableFactory.get_Table("SmallTable")

    print(BTable.get_dimensions())
    print(MTable.get_dimensions())
    print(STable.get_dimensions())