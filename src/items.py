class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def pick_up(self):
        print(f"you picked up the {self.name}")
    def drop(self):
        print(f"You dropped the {self.name}")


sword = Item("Broadsword", "sharp sword")
torch = Item( "Torch","burning torch")