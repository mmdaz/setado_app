from functools import partial
from tkinter import *
from tkinter import messagebox

from controller.register import costumer_register, add_address_to_costumer


class MainWindow:

    def __init__(self):
        self.main_window = Tk()
        self.user_register_window = None
        self.address_window = None

    def run(self):
        self.main_window.title("Welcome to Sitado app")
        # user register
        consumer_register_button = Button(self.main_window, text="Costumer Register", command=self.user_register)
        consumer_register_button.grid(column=1, row=0)
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
        self.user_register_window.title("Getting Address")
        name = Entry(self.address_window, width=10)
        address = Entry(self.address_window, width=10)
        phone = Entry(self.address_window, width=10)
        name.insert(0, "name")
        address.insert(0, "address")
        phone.insert(0, "phone")
        name.grid(column=1, row=0)
        address.grid(column=2, row=0)
        phone.grid(column=3, row=0)
        add_another_address_button = Button(self.address_window, text="Save this and add new one")
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
        add_address_to_costumer(costumer=costumer, name=name, address=address, phone=phone)
        messagebox.showinfo('Success!', 'Costumer Added.')
        self.user_register_window.destroy()
        self.address_window.destroy()


