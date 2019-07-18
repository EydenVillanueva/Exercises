from abc import ABCMeta, abstractstaticmethod

#Interface
class IChair(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_dimensions():
        """The Chair Interface"""

#BigChair Class implements IChair interface
class BigChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80
    
    def get_dimensions(self):
        return { 'heigth' : self.height, 'width' : self.width, 'depth' : self.depth }

#MediumChair Class implements IChair interface
class MediumChair(IChair):

    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70
    
    def get_dimensions(self):
        return { 'heigth' : self.height, 'width' : self.width, 'depth' : self.depth }

#SmallChair Class implements IChair interface
class SmallChair(IChair):

    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 60
    
    def get_dimensions(self):
        return { 'heigth' : self.height, 'width' : self.width, 'depth' : self.depth }

#Factory Class
class ChairFactory():
    
    @staticmethod
    def get_chair(chairtype):
        try:

            if chairtype == "BigChair":
                return BigChair()
            if chairtype == "MediumChair":
                return MediumChair()
            if chairtype == "SmallChair":
                return SmallChair()

            raise AssertionError("Chair Not Found")

        except AssertionError as _a:
            print(_a)

if __name__ == "__main__":
    Bchair = ChairFactory.get_chair("BigChair")
    Mchair = ChairFactory.get_chair("MediumChair")
    Schair = ChairFactory.get_chair("SmallChair")

    print(Bchair.get_dimensions())
    print(Mchair.get_dimensions())
    print(Schair.get_dimensions())