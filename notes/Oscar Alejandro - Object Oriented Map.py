class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=''):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        '''This method moves a character to a new location

        :param new_location: The variable containing a room object
        :return:
        '''
        self.current_location = new_location


# Option 2
# Put Them Away
R19A = Room("Mr. Wiebe's room", 'PARKING_LOT', None, None, None, "This is the room that you are in.")

player = Player(R19A)

Parking_lot = ("A Parking Lot", 'R19A', 'PARKING_LOT_GATE', None, None, "There are a few cars parked here.")

Parking_lot_gate = ("The Front Gate", 'PARKING_LOT', 'MIDDLE_OF_THE_ROAD', None, None,
                    "The Gates are rusting, but the doors aren't locked.")

Middle_of_the_road = ("Road", 'PARKING_LOT_GATE', 'ABANDONED_HOUSE', 'ABANDONED_STORE', 'BARRICADE_OF_CARS',
                      "There are puddles of green water and abandoned cars")

Abandoned_House = ("Old House", 'MIDDLE_OF_THE_ROAD', 'TORN_UP_ROOM', None, None,
                   "The house looks like it hasn't been kept in for years",
                   "There are a few burn marks but a lot of trash.")

Torn_up_room = ("Torn up room", 'ABANDONED_HOUSE', 'DESTROYED_KITCHEN', 'OLD_BATHROOM',
                "The room is burned, torn up, and abandoned.")

Abandoned_Store = ("Abandoned store", 'MIDDLE_OF_THE_ROAD', 'DAIRY_AISLE', 'CANNED_FOOD', 'FRUITS_AND_VEGETABLES',
                   "It is old and broken down. Few parts of the store are breaking and look unstable.")

Barricade_of_Cars = ("Barricade of Cars", "MIDDLE_OF_THE_ROAD",
                     "All of these cars seemed lock. Only if i had a metal pipe to break in.")


playing = True

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("command not recognized")
