class Room():
    def __init__(self, name):
        self.name = name
        self.links = {}
        self.visited = False 
        self.connect(self)
    def __str__(self):
        return self.name 
    def connect(self, room):
        if room.name not in self.links:
            self.links[room.name] = room
            if room.name == self.name:
                print("{} adds itself".format(self))
            else:
                print("{} connected to {}".format(self, room))
            room.connect(self)
    def test(self):
        self.visit()
        print("{} is tested".format(self))
        for room in self.links:
            if self.links[room].is_visited() == False:
                self.links[room].test()
    def get_size(self):
        return len(self.links)
    def get_links(self):
        return self.links
    def visit(self):
        print("{} was visited".format(self))
        self.visited = True 
    def is_visited(self):
        return self.visited 
    def reset(self):
        print("{} was reset".format(self))
        self.visited = False 
        
