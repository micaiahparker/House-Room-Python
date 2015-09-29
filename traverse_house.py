def traverse_house(house):
    print("TRAVERSE")
    if (house.test()):
        traverse_room(house.get_first_room(),[house.get_first_room()])
    print("TRAVERSE COMPLETE")
    
def traverse_room(room, queue=[]):
    room.visit()
    links = room.get_links()
    for link in links:
        if links[link].is_visited() == False and links[link] not in queue:
            print("{} added {} to the queue".format(room, links[link]))
            queue.append(links[link])
    queue.remove(room)
    print("{} was remove from the queue".format(room))
    try:
        traverse_room(queue[0], queue) #recurse using the first object in the queue
    except IndexError:
        pass
    