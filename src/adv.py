from room import Room
from player import Player
from item import Tool
from item import Weapon

#Items in rooms

torch = Tool (
    "Torch", "An ever burning ember atop this log lights your way.", 1)

dagger = Weapon (
    "Broken Dagger", "A simple knife, weak but effective when used correctly.", 27)

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[torch]), 

    'overlook': Room("Grand Overlook", """A steep cliff appears before you to the north, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'overlook descent': Room("Grand Overlook Descent", """As you approach north, you notice a tattered rope descending
into the chasm that you did not see before."""),

    'chasm pit': Room("Chasm Pit", """After descending the worn rope, you find yourself in a pitch black pit
which smells of rotten flesh. When your eyes adjust you see that you are in an old graveyard, 
and all of the graves have been dug up. 
You notice an old dagger at your feet.""",[dagger]),

    'rat': Room("Domain Of The Rodent", """You travel east into a small cavemouth with a sign with 
    'Domain Of The Rodent' scratched into it. 
    You hear the scratch of claws from the east and know that you must find your way out! 
    There is the sound of trickling water from the south."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].n_to = room['overlook descent']
room['overlook descent'].s_to = room['overlook']
room['overlook descent'].n_to = room['chasm pit']
room['chasm pit'].s_to = room['overlook descent']
room['chasm pit'].e_to = room['rat']
room['rat'].w_to = room['chasm pit']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input("Halt! What is your name, traveler? "), room["outside"], [])

# Write a loop that:

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

welcome = input(
    f"Hello {player.player_name}, are you ready to embark on this adventure? (yes/no): "
)
if welcome.lower().strip() == "yes":
    welcome = input(
        f"Where would you like to go \n  N, S, E, W, Q (Only use single letters, press Q to quit. Enter 'commands' to show commands)"
    )
    while True:
        options = ["n", "s", "e", "w"]
        choice = input("-> ").lower()
        if choice in options:
            player.movement(choice)
        elif choice == "commands":
            print("q: quit, i: inventory, take: take items in room, clear: clear inventory")
        elif choice == "take":
            player.take_items()
        elif choice == 'i':
            player.show_items()
        elif choice == 'clear':
            player.drop_items()
        elif choice == "q":
            print("Gone so soon?")
            exit()
        else:
            print("Invalid input.")
