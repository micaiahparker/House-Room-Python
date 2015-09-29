class House():
    def __init__(self, name):
        self.name = name
        self.rooms = {}
        self.first_room = None
    def __str__(self):
        return self.name
    def get_first_room(self):
        return self.first_room
    def add(self, room):
        if room not in self.rooms:
            print("{} added {}".format(self, room))
            self.rooms[room] = Room(room)
            self.first_room = self.rooms[room]
    def get(self, room):
        if room in self.rooms:
            return self.rooms[room]
        else:
            raise IndexError 
    def connect(self, room1, room2):
        self.get(room1).connect(self.get(room2))
        self.get(room2).connect(self.get(room1))
    def test(self): #only determines if a room has no connections, no that all rooms have at least one connection
        print("TEST")
        passes = True
        self.first_room.test()
        for room in self.rooms:
            if self.get(room).is_visited() == False:
                passes = False
                print("{} isn't properly connected to house".format(self.get(room)))
        self.reset_rooms()
        if (passes):
            print("TEST PASSED")
        else:
            print("TEST FAILED")
        print("TEST COMPLETE")
        return passes
    def reset_rooms(self):
        print("RESET ALL")
        for room in self.rooms:
            self.get(room).reset()
        print("RESET COMPLETE")
    