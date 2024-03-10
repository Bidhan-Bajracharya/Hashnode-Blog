from Inventory import Inventory

inventory = Inventory()
inventory.createItem('Oreo', 50, 10)
inventory.createItem('Cookie', 20, 10)

print(inventory.findItem('Oreo'))
print(inventory.totalStock())