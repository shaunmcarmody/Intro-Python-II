# Write a class to hold player information, e.g. what room they are in
# currently.

# The player class should be around/no more than 5 lines of code

class Player:
    def __init__(self, room):
        self.room = room
        self.item_list = []

    def direction(self, d):
        print(d)

    def add_item(self, item):
        self.item_list.append(item)

    def drop_item(self, item_chosen):
        result = None

        for item in self.item_list:
            if item.name == item_chosen:
                result = item
                self.item_list.remove(item)
                break
            result = None
            print(f"couldn't find {item_chosen}")

        return result

    def list_items(self):
        # print(self.item_list[0].name)
        if len(self.item_list) > 0:
            self.item_names = [item.name for item in self.item_list]
            print(f"items in your inventory: {self.item_names}")
        else:
            print(f"No items in your inventory")
        