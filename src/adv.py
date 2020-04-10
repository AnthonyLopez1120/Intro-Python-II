from room import Room
from player import Player
from items import torch, sword

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     f"North of you, the cave mount beckons. A {torch.description} is here", torch),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", f"""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. You see a {sword.description}"""),

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
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input("What's your name? "), room["outside"])

print(f"Hello, {player.name} the brave!")

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

print(player.current_room)
while True:
    direction = input("Enter a direction ").lower()
    if direction in ["n", "s", "e", "w"]:
        player.move(direction)
    elif direction == "p":
        player.pickup_item(room.items)
        print("You picked up an item")
        print(player.inventory)
    elif direction == "d":
        player.drop_item(player.inventory)
        print("you dropped an item")
    elif direction == "i":
            if len(player.inventory) < 1:
                print("you have no items")
            else:
                print(f"You are holding {player.inventory}")
        
        
    elif direction == "q":
        print("Adios Amigo!")
        exit()
else:
    print("Please enter a direction, n, s, e, or w")
