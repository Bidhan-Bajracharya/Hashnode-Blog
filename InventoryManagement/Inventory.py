class Inventory:
    def __init__(self):
        self.items = {}

    def __str__(self):
        return f"Interesting, I forgot about this"

    def createItem(self, name, quantity, price):
        self.items[name] = {'quantity': quantity, 'price': price}

    def addItem(self, name, quantity):
        if name in self.items:
            self.items[name]['quantity'] += quantity
            print("Quantity updated successfully!")
        else:
            print(f"No item with name '{name}' exists!")

    def findItem(self, name):
        if name in self.items:
            print(self.items[name])
        else:
            print(f"No item with name '{name}' exists!")