class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None):
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


class Ranged_Weapons(Item):
    def __init__(self, name):
        super(Ranged_Weapons, self).__init__(name)
        self.Damage = 25


class Medic(Item):
    def __init__(self, name):
        super(Medic, self).__init__(name)
        self.heal = 50


class Armor(Item):
    def __init__(self, name):
        super(Armor, self).__init__(name)


class Motorcycle (Vehicle):
    def __init__(self, name):
        super(Motorcycle, self).__init__(name)
        self.engine = True
        self.handle = True
        self.pedal = True


class AirsoftGun(Ranged_Weapons):
    def __init__(self, name):
        super(AirsoftGun, self).__init__(name)
        self.trigger = True
        self.barrel = True
        self.ammo = True
        self.Damage = True


class Bow(Ranged_Weapons):
    def __init__(self, name):
        super(Bow, self).__init__(name)
        self.String = True
        self.Arrows = True
        self.Damage = True


class CrossBow(Ranged_Weapons):
    def __init__(self, name):
        super(CrossBow, self).__init__(name)
        self.Damage = True
        self.string = True
        self.Arrows = True
        self.trigger = True
        self.sight = True


class Player(object):
    def __init__(self, name, starting_location, weapon):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.name = name
        self.weapon = weapon

    def move(self, new_location):
        self.current_location = new_location

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

    def find_next_room(self, direction):
        """This method searches the current room so see if a room
        exists in that direction.
        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']


R19A = Room("Mr.Wiebe's room", "You Wake up and everything in here is destroyed,"
                               "last thing you remember is a bright Flash, Find out what happened",
            "Parking_lot", None, None, None)

player = Player("Sauron", R19A, Bow("Bow"))

Parking_lot = Room("A Parking Lot", "There are a few cars parked here.", 'Parking_lot_gate', 'R19A', None, None)

Parking_lot_gate = Room("The Front Gate", "The Gates are rusting, but the doors aren't locked", 'Middle_of_the_road',
                        'Parking_lot', None,)

Middle_of_the_road = Room("Road", 'The are puddles of green water and abandoned cars', 'Abandoned house',
                          'Abandoned Store', 'Barricade of cars', None)

Abandoned_House = Room("Old House", 'The house looks like it has not been kept in for years', 'Torn_up_room', None,
                       None)

Torn_up_room = Room("Torn up room", 'The room is burned, torn up, and abandoned.', 'Destroyed_Kitchen',
                    'Abandoned_House', None, None)

Destroyed_Kitchen = Room("Destroyed Kitchen", "The kitchen is the same as the house burned up",
                         "with a lot of trash around", None, "Torn up room")

Old_Bathroom = Room("Old Bathroom", "It's all torn up and Destroyed", 'Torn_up_room', None, None)

Abandoned_Store = Room("Abandoned store",
                       "It is old and broken down. Few parts of the store are breaking and look unstable.",
                       'Dairy_Aisle', 'Canned_Food', 'Fruits_and_Vegetables',)

Dairy_Aisle = Room("Dairy Aisle", "The Milks gone Bad, and it reeks. There's also some green thick liquid.", None,
                   "Abandoned_Store", None, None)

Canned_Food = Room("Canned Food", "Everything here looks slightly ok except the meat.", "Abandoned_Store",
                   "Security_Room", 'Barricade_of_Cars', None)

Barricade_of_Cars = Room("Barricade of Cars", "All of these cars seemed lock. Only if i had a metal pipe to break in.",
                         None, 'Outside', None, 'Canned_Food')

Outside = Room("Outside", "You are outside"
                          " There seems to be light inside.", 'Barricade_of_Cars', None, None, 'Basement')

Subway = Room('Subway', "As you entered the Subway that goes somewhere.", None, 'Outside', None, None)


while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            room_object = player.find_next_room(command)
            player.move(room_object)
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
