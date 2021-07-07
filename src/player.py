# Write a class to hold player information, e.g. what room they are in
#  currently.

class Player:
    def __init__(self, player_name, current_room, player_items=[]):
        self.player_name = player_name
        self.current_room = current_room
        self.player_items = player_items

    def movement(self, cardinal):
        next_room = getattr(self.current_room, f"{cardinal}_to")
        if next_room is not None:
            self.current_room = next_room

            print(self.current_room)
        elif next_room == None:
            print("A wall blocks your way. ")

    def take_secret_passage(self):
        next_room = getattr(self.current_room)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)

    def take_items(self):
        if self.current_room.room_items is not None:
            for item in self.current_room.room_items:
                self.player_items.append(item)
            self.current_room.room_items.clear()

            output = f'{self.player_name} has found: '
            for item in self.player_items:
                output += f'\n - {item}'
            print(output)

    def show_items(self):
        output = f"{self.player_name} Inventory: "
        for item in self.player_items:
            str(item)
            output += f"\n - {item}"
        print(f'{output}')

    def drop_items(self):
        if self.player_items is not None:
            for item in self.player_items:
                self.current_room.room_items.append(item)
            self.player_items.clear()
            print(
                f'You have emptied your inventory.')
        else:
            print('Inventory empty... perhaps it is time to explore.')

    def __str__(self):
        return f"You are in {self.current_room}"