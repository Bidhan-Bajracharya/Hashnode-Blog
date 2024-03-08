from contactManager import viewContacts, createContact, searchContact, updateContactDetail, deleteContact

print("Hello, Welcome to Contact Management System! \n")

userLoggedIn = True

while(userLoggedIn):
    userChoice = input("What would you like to do?\n1. View contacts\n2. Create new contact\n3. Find a contact\n4. Update existing contact\n5. Delete a contact\n6. Exit the program\nEnter: ")
    if userChoice == '1':
        viewContacts()
    elif userChoice == '2':
        createContact()
    elif userChoice == '3':
        userNamePrompt = input('Enter contact owner name: ')
        searchContact(userNamePrompt)
    elif userChoice == '4':
        userNumberPrompt = input('Enter the contact number: ')
        contactName = input("Enter new contact name: ")
        contactNumber = input("Enter new contact number: ")
        contactEmail = input("Enter new contact email: ")
        updateContactDetail(userNumberPrompt, contactName, contactNumber, contactEmail)
    elif userChoice == '5':
        userNumberPrompt = input('Enter contact number: ')
        deleteContact(userNumberPrompt)
    elif userChoice == '6':
        userLoggedIn = False
        print("Program ended successfully!\n")