from room import Room
from player import Player
from item import Item

# Declare all the rooms

# Link rooms together

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     "foyer",
                     None,
                     None,
                     None,
                     []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east.""",
                    "overlook",
                    "outside",
                    "narrow",
                    None,
                    []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm.""",
                    None,
                    "foyer",
                    None,
                    None,
                    []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air.""",
                    "treasure",
                    None,
                    None,
                    "foyer",
                    []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south.""",
                    None,
                    "narrow",
                    None,
                    None,
                    []),
}

# Main

# Make a new player object that is currently in the 'outside' room.
player = Player('outside')

# Make a new item object
rock = Item("rock", "This is a rock")

room[player.room].item_list.append(rock)
# for item in room[player.room].item_list:
#     if item.name == "rock":
#         print("found rock")
#     else:
#         print("couldn't find rock")
# helper function that gives you a list of directions available to you

# Write a loop that:
while True:
    current_room = room[player.room]
# Prints the current room name
    print(current_room.name)
# Prints the current description (the textwrap module might be useful here).
    print(current_room.description)
# Prints the current list of items available (the textwrap module might be useful here).
    room[player.room].list_items()
# Waits for user input and decides what to do.
    cmd = input("Enter command: ")
    # print(cmd)
    if " " in cmd:
        cmd_arr = cmd.split(" ")
        if cmd_arr[0] == "take":
            taken = room[player.room].check_item(cmd_arr[1])
            player.add_item(taken)
            taken.on_take()
            pass
        elif cmd_arr[0] == "drop":
            dropped = player.drop_item(cmd_arr[1])
            if dropped:
                room[player.room].add_item(taken)
                dropped.on_drop()
            pass
    elif cmd == "q":
        break
    elif cmd == "n":
        player.direction("n")
        if current_room.n_to:
            player.room = current_room.n_to
        else:
            print("You cannot go in that direction")
        pass
    elif cmd == "s":
        player.direction("s")
        if current_room.s_to:
            player.room = current_room.s_to
        else:
            print("You cannot go in that direction")
        pass
    elif cmd == "e":
        player.direction("e")
        if current_room.e_to:
            player.room = current_room.e_to
        else:
            print("You cannot go in that direction")
        pass
    elif cmd == "w":
        player.direction("w")
        if current_room.w_to:
            player.room = current_room.w_to
        else:
            print("You cannot go in that direction")
        pass
    elif cmd == "i":
        player.list_items()
        pass
    else:
        print("Incorrect command input help for a list of commands")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
