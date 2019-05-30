# Implement a class to hold room information. This should have name and
# description attributes.

# The Room class should be extended with a list that holds the Items that are currently in that room.

class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to, item_list):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.item_list = []

    def list_items(self):
        # print(self.item_list[0].name)
        if len(self.item_list) > 0:
            self.item_names = [item.name for item in self.item_list]
            print(f"items available: {self.item_names} in {self.name}")
        else:
            print(f"No items in {self.name}")

    def check_item(self, item_chosen):
        result = None

        for item in self.item_list:
            if item.name == item_chosen:
                result = item
                self.item_list.remove(item)
                break
            result = None
            print(f"couldn't find {item_chosen}")

        return result

    def add_item(self, item):
        self.item_list.append(item)
