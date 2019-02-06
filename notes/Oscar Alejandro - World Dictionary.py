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
        'PATH': {
            'SOUTH': 'PARKING_LOT',
            'NORTH': 'MIDDLE_OF_THE_ROAD'
        }
    },
    'MIDDLE_OF_THE_ROAD': {
        'NAME': "Road",
        'DESCRIPTION': "There are puddles of green water and abandoned cars"
    }
}

# Other variables
current_node = world_map['R19A']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# Controller
while playing:
    print(current_node['NAME'])
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

