def print_menu():
    print('1, Display a contact')
    print('2, Add a contact')
    print('3, Delete a contact')
    print('4, View a contact')
    print('5, Quit')
    print()


numbers = {}
choice = 0
print_menu()
while choice != 5:
    choice = int(input("Enter a number between 1 and 5: "))
    if choice == 1: #viewing a contact already saved 
        print("Contacts: ")
        for name in numbers.keys():
            print("Name: ", name, "\t Number: ", numbers[name])

        print()
    elif choice == 2: #adding a new contact
        print("Add name and number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif choice == 3:#deleting or removing a contact
        print("Delete a contact")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif choice == 4:#search for a contact
        print("Search number")
        name = input("Name: ")
        if name in numbers:
            print("The contact is, ", numbers[name])
        else:
            print(name, "was not found ")
    elif choice != 5:
        print_menu()
    elif choice == 5: #quit program
        print("Thank u for using this application")
        print("hope to see you again")
        print("next time")
