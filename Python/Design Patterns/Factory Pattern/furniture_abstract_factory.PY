from abc import  ABCMeta, abstractclassmethod
from chair_factory import ChairFactory
from table_factory import TableFactory

#Interface
class IFurnitureFactory(metaclass=ABCMeta):

    @abstractclassmethod
    def get_furniture():
        """The static furniture factory interface method"""

class FurnitureFactory(IFurnitureFactory):

    @staticmethod
    def get_furniture(furniture_type):
        try:

            if furniture_type in ["BigChair","MediumChair","SmallChair"]:
                return ChairFactory.get_chair(furniture_type)
            if furniture_type in ["SmallTable","MediumTable","BigTable"]:
                return TableFactory.get_Table(furniture_type)

            raise AssertionError("Cannot find furniture type")

        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":

    furniture = FurnitureFactory.get_furniture("BigChair")
    furniture2 = FurnitureFactory.get_furniture("SmallTable")

    print(f"{furniture.__class__} : {furniture.get_dimensions()}")
    print(f"{furniture2.__class__} : {furniture2.get_dimensions()}")
