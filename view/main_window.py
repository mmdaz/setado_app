from functools import partial
from tkinter import *
from tkinter import messagebox

from controller.food import add_new_food
from controller.register import costumer_register, add_address_to_costumer
from db.models.address import Address


class MainWindow:

    def __init__(self):
        self.main_window = Tk()
        self.user_register_window = None
        self.address_window = None
        self.add_food_window = None
        self.addresses_list = []

    def run(self):
        self.main_window.title("Welcome to Sitado app")
        # user register
        consumer_register_button = Button(self.main_window, text="Costumer Register", command=self.user_register)
        add_food_to_menu = Button(self.main_window, text="Add Food To Menu", command=self.add_food_to_menu)
        consumer_register_button.grid(column=1, row=0)
        add_food_to_menu.grid(column=1, row=2)
        self.main_window.mainloop()

    def user_register(self):
        self.user_register_window = Tk()
        self.user_register_window.title("Costumer Registration")
        first_name = Entry(self.user_register_window, width=10)
        last_name = Entry(self.user_register_window, width=10)
        age = Entry(self.user_register_window, width=10)
        first_name.insert(0, "first_name")
        last_name.insert(0, "last_name")
        age.insert(0, "age")
        save_costumer_information = Button(self.user_register_window, text="Save and Continue",
                                           command=partial(self.get_costumer_address, first_name, last_name, age))
        cancel = Button(self.user_register_window, text="Cancel")
        first_name.grid(column=1, row=0)
        last_name.grid(column=2, row=0)
        age.grid(column=3, row=0)
        save_costumer_information.grid(column=1, row=2)
        cancel.grid(column=2, row=2)
        self.user_register_window.mainloop()

    def get_costumer_address(self, first_name, last_name, age):
        first_name = first_name.get()
        last_name = last_name.get()
        age = int(age.get())
        costumer = costumer_register(first_name=first_name, last_name=last_name, age=age)
        self.address_window = Tk()
        self.address_window.title("Getting Address")
        name = Entry(self.address_window, width=10)
        address = Entry(self.address_window, width=10)
        phone = Entry(self.address_window, width=10)
        name.insert(0, "name")
        address.insert(0, "address")
        phone.insert(0, "phone")
        name.grid(column=1, row=0)
        address.grid(column=2, row=0)
        phone.grid(column=3, row=0)
        add_another_address_button = Button(self.address_window, text="Save this and add new one",
                                            command=partial(self.add_address, name, address, phone))
        save_and_exit = Button(self.address_window, text="save and exit", command=partial(self.save_address,
                                                                                          name, address, phone,
                                                                                          costumer))
        add_another_address_button.grid(column=1, row=2)
        save_and_exit.grid(column=2, row=2)
        self.address_window.mainloop()

    def save_address(self, name, address, phone, costumer):
        name = name.get()
        address = address.get()
        phone = phone.get()
        self.addresses_list.append(Address(name=name, address=address, phone=phone))
        add_address_to_costumer(costumer=costumer, addresses_list=self.addresses_list)
        messagebox.showinfo('Success!', 'Costumer Added.')
        self.addresses_list.clear()
        self.user_register_window.destroy()
        self.address_window.destroy()

    def add_address(self, name, address, phone):
        self.addresses_list.append(Address(name=name.get(), address=address.get(), phone=phone.get()))
        name.delete(0, 'end')
        address.delete(0, 'end')
        phone.delete(0, 'end')

    def add_food_to_menu(self):
        self.add_food_window = Tk()
        self.add_food_window.title("Add Food")
        name = Entry(self.add_food_window, width=10)
        price = Entry(self.add_food_window, width=10)
        name.insert(0, "name")
        price.insert(0, 'price')
        name.grid(column=1, row=0)
        price.grid(column=2, row=0)
        save_and_exit = Button(self.add_food_window, text="save and exit", command=partial(self.save_food, name, price))
        save_and_exit.grid(column=1, row=2)

    def save_food(self, name, price):
        add_new_food(name=name.get(), price=price.get())
        messagebox.showinfo('Success!', 'Food Added.')
        self.add_food_window.destroy()
