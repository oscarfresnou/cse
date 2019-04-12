class Item(object):
    def __init__(self, name):
        self.name = name


class Vehicle(Item):
    def __init__(self, name):
        super(Vehicle, self).__init__(name)
        self.engine = True
        self.steering_wheel = True


class Boat(Vehicle):
    def __init__(self, name):
        super(Boat, self).__init__(name)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        self.current_location = new_location


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while playing:
    print(Player.current_location.name)
    print(Player.current_location.description)

    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.insert(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            room_name = getattr(Player.current_location, command)
            room_object = globals()[room_name]

            Player.move(room_object)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")

R19A = Room("Mr. Wiebe's room", 'Parking_lot', None, None, None, "This is the room that you are in.")

player = Player(R19A)

Parking_lot = Room("A Parking Lot", 'R19A', 'PARKING_LOT_GATE', None, None, "There are a few cars parked here.")

Parking_lot_gate = Room("The Front Gate", 'PARKING_LOT', 'MIDDLE_OF_THE_ROAD', None, None,
                        "The Gates are rusting, but the doors aren't locked")

Middle_of_the_road = Room("Road", 'PARKING_LOT_GATE', 'ABANDONED_HOUSE', 'ABANDONED_STORE', 'BARRICADE_OF_CARS',
                          "There are puddles of green water and abandoned cars")

Abandoned_House = Room("Old House", 'MIDDLE_OF_THE_ROAD', 'TORN_UP_ROOM', None, None,
                       "The house looks like it hasn't been kept in for years",
                       "There are a few burn marks but a lot of trash.")

Torn_up_room = Room("Torn up room", 'ABANDONED_HOUSE', 'DESTROYED_KITCHEN', 'OLD_BATHROOM',
                    "The room is burned, torn up, and abandoned.")

Abandoned_Store = Room("Abandoned store", 'MIDDLE_OF_THE_ROAD', 'DAIRY_AISLE', 'CANNED_FOOD', 'FRUITS_AND_VEGETABLES',
                       "It is old and broken down. Few parts of the store are breaking and look unstable.")

Barricade_of_Cars = Room("Barricade of Cars", "MIDDLE_OF_THE_ROAD",
                         "All of these cars seemed lock. Only if i had a metal pipe to break in.")



