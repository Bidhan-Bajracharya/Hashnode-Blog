class Inventory:
    def __init__(self):
        self.items = {}

    def seedItems(self):
        '''Default items'''
        defaultItemsSnacks = ['Oreo', 'Cheetos', 'Doritos']
        defaultItemsDrinks = ['Coke', 'Pepsi', 'Fanta']

        for item in defaultItemsSnacks:
            self.items[item] = {'quantity': 50, 'price': 15}

        for item in defaultItemsDrinks:
            self.items[item] = {'quantity': 30, 'price': 10}

    def browseItems(self):
        '''Display all items'''
        for item in self.items:
            print(f"Name: {item}, Quantity: {self.items[item]['quantity']}, Price: {self.items[item]['price']}")

    def createItem(self, name, quantity, price):
        '''Create new item'''
        if name not in self.items:
            self.items[name] = {'quantity': quantity, 'price': price}
            return "Item created successfully!\n"
        else:
            return f"Item with name '{name}' already exists!\n"

    def addItem(self, name, quantity):
        '''Update item stock quantity'''
        if name in self.items:
            self.items[name]['quantity'] += quantity
            return "Quantity updated successfully!\n"
        else:
            return f"No item with name '{name}' exists!\n"

    def findItem(self, name):
        '''Search item's detail'''
        if name in self.items:
            item = self.items[name]
            return f"Item name: {name}, Available Quantity: {item['quantity']}, Price: ${item['price']}\n"
        else:
            return f"No item with name '{name}' exists!\n"
    
    def findItemPOS(self, name: str):
        '''Returns item'''
        if name in self.items:
            item = self.items[name]
            return item
        else:
            return None

    def udpateItem(self, name, newQuantity):
        '''Update stock quantity'''
        if name in self.items:
            self.items[name]['quantity'] = newQuantity
        else:
            return f"No item with name '{name}' exists!\n"
        
    def deleteItem(self, name):
        '''Remove item'''
        if name in self.items:
            del self.items[name]
            return f"Item '{name}' removed successfully!\n"
        else:
            return f"No item with name '{name}' exists!\n"
    
    def totalStock(self):
        '''Total items in stock'''
        sum = 0
        for item in self.items:
            sum = sum + self.items[item]['quantity']
        return f"There are in total {sum} items in stock.\n"

class PointOfService:
    def __init__(self, inventory: Inventory, tillBalance=0):
        self.inventory = inventory
        self.tillBalance = tillBalance

    def purchaseItem(self, name, quantity):
        item = self.inventory.findItemPOS(name)
        if item:
            if(item['quantity'] >= quantity):
                totalCost = quantity * item['price']
                if(totalCost <= self.tillBalance):
                    self.tillBalance -= totalCost
                    self.inventory.udpateItem(name, item['quantity'] - quantity)
                    return f"Transaction successful. Total cost: ${totalCost}\n"
                else:
                    return 'Insufficient funds in the till!\n'
            else:
                return 'Insufficient quantity in stock!\n'
        else:
            return 'Item not found!\n'
        
    def returnItem(self, name, quantity):
        item = self.inventory.findItemPOS(name)
        if item:
            self.tillBalance += item['price'] * quantity
            self.inventory.udpateItem(name, item['quantity'] + quantity)
            return f"Return successful. Refund: ${item['price'] * quantity}\n"
        else:
            return "Item not found in inventory.\n"