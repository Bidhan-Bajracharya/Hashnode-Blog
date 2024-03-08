import os

filePath = 'data/contactData.txt'

# view all contacts
def viewContacts():
    folderExist = os.path.isdir('data')
    fileExist = os.path.exists(filePath)

    if(folderExist and fileExist):
        with open(filePath, "r") as fileContent:
            print(fileContent.read())
    else:
        print('No contact details available!\n')

def userCreateContactPrompt():
    contactName = input("Enter contact name: ")
    contactNumber = input("Enter contact number: ")
    contactEmail = input("Enter contact email: ")
    contactData = f"{contactName}, {contactNumber}, {contactEmail}\n"
    
    with open(filePath, "a") as file:
        file.write(contactData)

    print("Contact created successfully!\n")

# create a contact
def createContact():
    # if folder doesnt exists
    # create the folder
    folderExist = os.path.isdir('data')

    if not folderExist:
        os.makedirs('data')
        userCreateContactPrompt()
        return

    else:
        # append the details provided by the user
        # also creates the file, if does not exists
        userCreateContactPrompt()
        return

# find/search a contact
def searchContact(contactName):
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(contactName) != -1:
                print(line)
                return
        print('No such contact exists!\n')   

# update existing contact
def updateContactDetail(contactNumber, updatedName, updatedNumber, updatedEmail):
    updated_contact = f"{updatedName}, {updatedNumber}, {updatedEmail}\n"
    contactFound = False

    with open(filePath, "r+") as file:
        lines = file.readlines()
        file.seek(0) # file pointer at the beginning
        
        for index, line in enumerate(lines):
            if contactNumber in line:
                lines[index] = updated_contact
                contactFound = True

        file.writelines(lines)
        file.truncate()

    if contactFound:
        print('Contact detail updated successfully!\n')
    else:
        print('Contact detail not found!\n')

# delete existing contact
def deleteContact(contactNumber):
    with open(filePath, "r") as file:
        lines = file.readlines()
    
    with open(filePath, "w") as file:
        for line in lines:
            if contactNumber not in line:
                file.write(line)

    print('Contact deleted successfully!\n')
