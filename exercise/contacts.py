#!/usr/bin/python
# Filename: contacts.py

import pickle


class Contact:
    def __init__(self, name, phone_number="", address="", email="", group=""):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.group = group

    def __str__(self):
        return "[name={0},phone_number={1},address={2},email={3},group={4}]"\
            .format(self.name, self.phone_number, self.address, self.email, self.group)


class ContactManager:
    contact_dictionary = {}

    @staticmethod
    def help_info():
        print("This usage specification is about the Contact Manager.")
        print("\tadd          add contact to the contact manager")
        print("\tdelete       delete the specific contact from contact manager")
        print("\tclear        remove all existing contacts from contact manager")
        print("\tsearch       find the specific contact from contact manager")
        print("\tdisplay      show information about the specific contact")
        print("\tdisplay_all  show information about all existing contacts")
        print("\tstore        save all contacts to local disk file")
        print("\tquit         quit from this contact manager")

    @staticmethod
    def add():
        print("You can add a contact with the following steps:")

        try:
            name = input("Contact Name: ")
            phone_number = input("Contact Phone Number: ")
            address = input("Contact Address: ")
            email = input("Contact email: ")
            group = input("Contact group: ")
            contact = Contact(name, phone_number, address, email, group)
            ContactManager.contact_dictionary[name] = contact
        except KeyError:
            print("Input error! Make sure you input right information")
        else:
            print(contact)
            print("Add contact successfully!")

    @staticmethod
    def delete():
        print("You will delete contact.")
        try:
            name = input("Please input contact name being deleted: ")
        except (Exception, KeyError):
            print("Input error! Make sure you input right information")
        else:
            del ContactManager.contact_dictionary[name]
            print("Delete contact {0} successfully!".format(name))
            print("There are {0} contacts left.".format(len(ContactManager.contact_dictionary)))

    @staticmethod
    def clear():
        make_sure = input("Make sure you will clear all contacts(yes/no)? ")
        if make_sure == "yes":
            ContactManager.contact_dictionary.clear()
            print("Clear all contacts successfully!")
        else:
            print("Clear operation has been cancelled!")

    @staticmethod
    def search():
        name = input("Please input contact name you want to search: ")
        return ContactManager.contact_dictionary[name]

    @staticmethod
    def display():
        name = input("Please input name of the contact you want to display: ")
        contact = ContactManager.contact_dictionary[name]
        print(contact)

    @staticmethod
    def display_all():
        if len(ContactManager.contact_dictionary) == 0:
            print("There is no contact exist!")
            return
        for name in ContactManager.contact_dictionary:
            print(ContactManager.contact_dictionary[name])

    @staticmethod
    def store():
        filename = "contact.dat"
        try:
            file = open(filename, 'wb')
            pickle.dump(ContactManager.contact_dictionary, file)
            file.close()
            print("Store contacts data to file 'contact.dic' successfully!")
        except FileNotFoundError:
            print("File not Found!")

    @staticmethod
    def load():
        filename = "contact.dat"
        try:
            file = open(filename, 'rb')
            ContactManager.contact_dictionary = pickle.load(file)
            file.close()
            print("Load existing contacts successfully!")
        except (FileNotFoundError, EOFError):
            pass


def __main__():
    print("Welcome to Contact Manager!")
    ContactManager.load()
    print("Useful commands are as follows: add, delete, clear, search, display, display_all, store, quit")

    while True:
        cmd = input("Please input your command: ")
        cmd = cmd.lower()
        if cmd == "add":
            ContactManager.add()
        elif cmd == "delete":
            ContactManager.delete()
        elif cmd == "clear":
            ContactManager.clear()
        elif cmd == "search":
            ContactManager.search()
        elif cmd == "display":
            ContactManager.display()
        elif cmd == "display_all":
            ContactManager.display_all()
        elif cmd == "store":
            ContactManager.store()
        elif cmd == "help":
            ContactManager.help_info()
        elif cmd == "quit":
            break


if __name__ == "__main__":
    __main__()
