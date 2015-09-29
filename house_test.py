from house import House
from traverse import *

def test():
    print("SETUP")
    house = House('house')
    house.add('a')
    house.add('b')
    house.add('c')
    house.add('d')
    house.add('e')
    house.add('f')
    house.add('g')
    house.add('h')
    house.add('i')
    house.add('j')
    print("CONNECTIONS")
    house.connect('a','b')
    house.connect('c','d')
    house.connect('a','e')
    house.connect('b','e')
    house.connect('a','c')
    house.connect('f','c')
    house.connect('g','d')
    house.connect('h','b')
    house.connect('i','c')
    house.connect('j','a')
    house.connect('j','h')
    print("CONNECTIONS COMPLETE")
    print("SETUP COMPLETE")
    traverse_house(house)
    
if __name__ in "__main__":
    test()
