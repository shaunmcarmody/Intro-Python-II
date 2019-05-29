# Write a class to hold player information, e.g. what room they are in
# currently.

# The player class should be around/no more than 5 lines of code

class Player:
    def __init__(self, room):
        self.room = room

    def direction(self, d):
        print(d)
