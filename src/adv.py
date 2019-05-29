from room import Room
from player import Player

# Declare all the rooms

# Link rooms together

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     "foyer",
                     None,
                     None,
                     None,
                    ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east.""",
                    "overlook",
                    "outside",
                    "narrow",
                    None),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm.""",
                    None,
                    "foyer",
                    None,
                    None),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air.""",
                    "treasure",
                    None,
                    None,
                    "foyer"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south.""",
                    None,
                    "narrow",
                    None,
                    None),
}

# Main

# Make a new player object that is currently in the 'outside' room.

player = Player('outside')
room = room[player.room]

# helper function that gives you a list of directions available to you

# Write a loop that:
while True:
# Prints the current room name
    print(player.room)
# Prints the current description (the textwrap module might be useful here).
    # print(room.description)
# Waits for user input and decides what to do.
    cmd = input("Please input n/s/e/w: ")
    if cmd == "q":
        break
    elif cmd == "n":
        player.direction("n")
        if room.n_to:
            player.room = room.n_to
        pass
    elif cmd == "s":
        player.direction("s")
        if room.s_to:
            player.room = room.s_to
        pass
    elif cmd == "e":
        player.direction("e")
        if room.e_to:
            player.room = room.e_to
        pass
    elif cmd == "w":
        player.direction("w")
        if room.w_to:
            player.room = room.w_to
        pass
    else:
        print("Input n/s/e/w, or q to quit")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
