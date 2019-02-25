world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the room that you are in.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "There are a few cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A',
            'NORTH': "PARKING_LOT_GATE"
        }
    },
    'PARKING_LOT_GATE': {
        'NAME': "The Front Gate",
        'DESCRIPTION': "The Gates are rusting, but the doors aren't locked.",
        'PATHS': {
            'SOUTH': 'PARKING_LOT',
            'NORTH': 'MIDDLE_OF_THE_ROAD'
        }
    },
    'MIDDLE_OF_THE_ROAD': {
        'NAME': "Road",
        'DESCRIPTION': "There are puddles of green water and abandoned cars",
        'PATHS': {
            'SOUTH': 'PARKING_LOT_GATE',
            'NORTH': 'ABANDONED_HOUSE',
            'WEST': 'ABANDONED_STORE',
            'EAST': 'BARRICADE_OF_CARS'
        }
    },
    'ABANDONED_HOUSE': {
        'NAME': "Old House",
        'DESCRIPTION': "The house looks like it hasn't been kept in for years."
                       " There are a few burn marks but a lot of trash.",
        'PATHS': {
            'SOUTH': 'MIDDLE_OF_THE_ROAD',
            'NORTH': 'TORN_UP_ROOM',
        }
    },
    'TORN_UP_ROOM': {
        'NAME': "Torn up room",
        'DESCRIPTION': "The room is burned, torn up, and abandoned.",
        'PATHS': {
            'SOUTH': 'ABANDONED_HOUSE',
            'WEST': 'DESTROYED_KITCHEN',
            'EAST': 'OLD_BATHROOM'
        }
    },

    'ABANDONED_STORE': {
        'NAME': "Abandoned store",
        'DESCRIPTION': "It is old and broken down. Few parts of the store are breaking and look unstable.",
        'PATHS': {
            'EAST': 'MIDDLE_OF_THE_ROAD',
            'WEST': 'DAIRY_AISLE',
            'SOUTH': 'CANNED_FOOD',
            'NORTH': 'FRUITS_AND_VEGETABLES'
        }
    },
    'BARRICADE_OF_CARS': {
        'NAME': "Barricade of Cars",
        'DESCRIPTION': "All of these cars seemed lock. Only if i had a metal pipe to break in.",
        'PATHS': {
            'WEST': "MIDDLE_OF_THE_ROAD"
        }
    },
}

# Other variables
current_node = world_map['R19A']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# Controller
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_").strip()
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
