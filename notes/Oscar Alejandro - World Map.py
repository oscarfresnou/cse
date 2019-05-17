class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=''):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


class Item(object):
    def __init__(self, name):
        self.name = name


class Vehicle(Item):
    def __init__(self, name):
        super(Vehicle, self).__init__(name)
        self.engine = True
        self.steering_wheel = True


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.Damage = number


class Medic(Item):
    def __init__(self, name):
        super(Medic, self).__init__(name)
        self.heal = number


class Armor(Item):
    def __init__(self):
        super(Armor, self).__init__()


class Motorcycle (Vehicle):
    def __init__(self, name):
        super(Motorcycle, self).__init__(name)
        self.engine = True
        self.handle = True
        self.pedal = True


class AirsoftGun(Weapon):
    def __init__(self, name):
        super(AirsoftGun, self).__init__(name)
        self.trigger = True
        self.barrel = True
        self.ammo = True


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


R19A = Room("Mr. Wiebe's room", 'Parking_lot', None, None, None, "This is the room that you are in.")

player = Player(R19A)

Parking_lot = Room("A Parking Lot", 'R19A', 'PARKING_LOT_GATE', None, None, "There are a few cars parked here.")

Parking_lot_gate = Room("The Front Gate", 'PARKING_LOT', 'MIDDLE_OF_THE_ROAD', None, None,
                        "The Gates are rusting, but the doors aren't locked")

Middle_of_the_road = Room("Road", 'Parking lot Gate', 'Abandoned house', 'Abandoned Store', 'Barricade of cars',
                          "There are puddles of green water and abandoned cars")

Abandoned_House = Room("Old House", 'Middle_of_the_Road', 'TORN_UP_ROOM', None,
                       "The house looks like it hasn't been kept in for years",
                       "There are a few burn marks but a lot of trash.")

Torn_up_room = Room("Torn up room", 'ABANDONED_HOUSE', 'DESTROYED_KITCHEN', 'OLD_BATHROOM',
                    "The room is burned, torn up, and abandoned.")

Destroyed_Kitchen = Room(None, None, None, "Torn up room", "The kitchen is the same as the house burned up",
                         "with a lot of trash around")

Old_Bathroom = Room(None, None, 'Torn_up_room', None,)

Abandoned_Store = Room("Abandoned store", 'MIDDLE_OF_THE_ROAD', 'DAIRY_AISLE', 'CANNED_FOOD', 'FRUITS_AND_VEGETABLES',
                       "It is old and broken down. Few parts of the store are breaking and look unstable.")

Dairy_Aisle = Room(None, None, None, "Abandoned_Store",
                   "The Milks gone Bad, and it reeks.",
                   "There's also a lot of stuff on the floor and some green thick liquid.")

Canned_Food = Room(None, None, "Abandoned_Store", "Security_Room", "Everything here looks slightly ok except the meat.")

Barricade_of_Cars = Room("Barricade of Cars", "MIDDLE_OF_THE_ROAD",
                         "All of these cars seemed lock. Only if i had a metal pipe to break in.")


while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
        playing = False
    elif command.lower() in directions:
        try:
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")

if command.lower() in ['q', 'quit', 'exit']:
    playing = False
elif command.lower() in directions:
    try:
        room_name = getattr(player.current_location, command)
        if room_name is None:
            raise AttributeError
        player.move(room_name)
    except AttributeError:
        print("This path does not exist")
    except KeyError:
        print("I can't go that way.")
elif command.lower() in ["search"]:
    if len(player.current_location.items) > 0:
        print()
        print("The following items are in the room: ")
        for num, item in enumerate(player.current_location.items):
            print(str(num + 1) + ": " + item.name)
    else:
        print("There are no items in the room.")
elif command.lower() in ["inventory", "I"]:
    Item = 0
    for i in player.inventory:
        print(player.inventory[Item].name)
        Item += 1
elif "take" in command:
    choice = input("what will you pick up: ")

    number = int(choice)
    if len(player.current_location.items) >= number > 0:
        player.inventory.append(player.current_location.items[number - 1])
        player.current_location.items.pop(number - 1)

    print("The item is in your inventory")
    print()
elif "drop" in command:
    choice = input("What will you drop:")

    number = int(choice)
    if len(player.current_location.items) > 0:
        player.current_location.items.append((player.inventory[number - 1]))
        player.inventory.pop(number - 1)
else:
    print("Command Not Recognized")
print()
