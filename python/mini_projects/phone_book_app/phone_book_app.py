# phonebook app using dictionary
def phonebook_app():
    phonebook={}

    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice=input("Enter your choice (1-5) : ")

        # Add Contact
        if choice=="1":
            name=input("Enter name : ")
            number=input("Enter phone number : ")
            phonebook[name]=number
            print(f"Contact {name} added successfully!")

        # Search Contact
        elif choice=="2":
            name=input("Enter name to search : ")
            if name in phonebook:
                print(f"{name} : {phonebook[name]}")
            else:
                print("Contact not found.")
        
        # Display all contacts
        elif choice=="3":
            if phonebook:
                print("Phonebook Contacts : ")
                for name,number in phonebook.items():
                    print(f"{name} : {number}")
            else:
                print("Phonebook is empty.")

        # Delete contact
        elif choice=="4":
            name=input("Enter name to delete : ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} deleted successfully!")
            else:
                print("Contact not found.")
        
        # Exit
        elif choice=="5":
            print("Exiting Phonebook. oodbye!")
            break

        else:
            print("Invalid choice. Try again.")

phonebook_app()