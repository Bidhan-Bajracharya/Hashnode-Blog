class Inventory:
    def __init__(self):
        self.items = {}

    def __str__(self):
        return f"Interesting, I forgot about this"

    def createItem(self, name, quantity, price):
        if name not in self.items:
            self.items[name] = {'quantity': quantity, 'price': price}
            return "Item created successfully!"
        else:
            return f"Item with name '{name}' already exists!"

    def addItem(self, name, quantity):
        if name in self.items:
            self.items[name]['quantity'] += quantity
            return "Quantity updated successfully!"
        else:
            return f"No item with name '{name}' exists!"

    def findItem(self, name):
        if name in self.items:
            item = self.items[name]
            return f"Item name: {name}, Available Quantity: {item['quantity']}, Price: ${item['price']}"
        else:
            return f"No item with name '{name}' exists!"

    def udpateItem(self, name, newQuantity):
        if name in self.items:
            self.items[name]['quantity'] = newQuantity
        else:
            return f"No item with name '{name}' exists!"
        
    def deleteItem(self, name):
        if name in self.items:
            del self.items[name]
            return f"Item '{name}' removed successfully!"
        else:
            return f"No item with name '{name}' exists!"
    
    def totalStock(self):
        sum = 0
        for item in self.items:
            sum = sum + self.items[item]['quantity']
        return f"There are in total {sum} items in stock."
    