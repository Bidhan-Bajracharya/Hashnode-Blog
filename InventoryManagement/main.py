from Inventory import Inventory
from Inventory import PointOfService
from util import capitalizeFirstLetter

inventory = Inventory()
inventory.seedItems()

pos = PointOfService(inventory, 1000)

userLoggedIn = True

print('Welcome to Inventory Management System!')

while(userLoggedIn):
    userPrompt = input("What would you like to do?\n1. View items\n2. Create an item\n3. Add item to inventory\n4. Find item\n5. Delete item\n6. Get total stock\n7. Purchase item\n8. Return item\n9. Exit the program\nEnter: ")
    
    if(userPrompt == '1'):
        inventory.browseItems()
        print('')
    elif(userPrompt == '2'):
        itemName = input('Enter item name: ')
        itemQuantity = input('Enter item quantity: ')
        itemPrice = input('Enter item price: ')
        print(inventory.createItem(capitalizeFirstLetter(itemName), int(itemQuantity), float(itemPrice)))
    elif(userPrompt == '3'):
        itemName = input('Enter item name: ')
        itemQuantity = input('Enter additional item quantity: ')
        print(inventory.addItem(capitalizeFirstLetter(itemName), int(itemQuantity)))
    elif(userPrompt == '4'):
        itemName = input('Enter item name: ')
        print(inventory.findItem(capitalizeFirstLetter(itemName)))
    elif(userPrompt == '5'):
        itemName = input('Enter item name to delete: ')
        inventory.deleteItem(capitalizeFirstLetter(itemName))
    elif(userPrompt == '6'):
        print(inventory.totalStock())
    elif(userPrompt == '7'):
        itemName = input('Enter item name: ')
        itemQuantity = input('Enter item quantity: ')
        print(pos.purchaseItem(capitalizeFirstLetter(itemName), int(itemQuantity)))
    elif(userPrompt == '8'):
        itemName = input('Enter item name: ')
        itemQuantity = input('Enter item quantity: ')
        pos.returnItem(capitalizeFirstLetter(itemName), int(itemQuantity))
    elif(userPrompt == '9'):
        userLoggedIn = False
