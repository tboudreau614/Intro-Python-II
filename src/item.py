class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __str__(self):
        return f"ITEM:{self.item_name} DESCRIPTION: {self.item_description} "


class Tool(Item):
    def __init__(self, item_name, item_description, item_level):
        super().__init__(item_name, item_description)
        self.item_level = item_level

    def __str__(self):
        return super().__str__() + f" Level: {self.item_level}"


class Weapon(Item):
    def __init__(self, item_name, item_description, item_attack_power):
        super().__init__(item_name, item_description)
        self.item_attack_power = item_attack_power

    def __str__(self):
        return super().__str__() + f" Maximum Attack Power: {self.item_attack_power}"