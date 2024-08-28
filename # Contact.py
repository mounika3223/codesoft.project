# Contact Management System

# List to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully.\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    
    print("Contact List:")
    for idx, contact in enumerate(contacts):
        print(f"{idx + 1}. {contact['name']} - {contact['phone']}")
    print()

# Function to search for a contact by name or phone
def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    else:
        print("No matching contacts found.\n")

# Function to update a contact's details
def update_contact():
    search_term = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print("Updating contact details...")
            contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']
            print("Contact updated successfully.\n")
            return
    print("No matching contact found to update.\n")

# Function to delete a contact
def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully.\n")
            return
    print("No matching contact found to delete.\n")

# Main menu for user interaction
def main_menu():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the main menu
if __name__ == "__main__":
    main_menu()
