from functools import partial
from tkinter import *
from tkinter import messagebox

from controller.food import add_new_food
from controller.register import costumer_register, add_address_to_costumer, calculate_report
from db.models.address import Address
from db.persist.persist import get_all_foods, create_bill, create_buy_bill, delete_table_from_db
from view.checkbar import CheckBar


class MainWindow:

    def __init__(self):
        self.vars = []
        self.main_window = None
        self.user_register_window = None
        self.address_window = None
        self.add_food_window = None
        self.addresses_list = []
        self.food_menu_window = None
        self.foods_check_bar = None
        self.buy_menu = None
        self.delete_table_menu = None

    def run(self):
        self.main_window = Tk()
        self.main_window.title("Welcome to Sitado app")
        # user register
        consumer_register_button = Button(self.main_window, text="Costumer Register", command=self.user_register)
        add_food_to_menu = Button(self.main_window, text="Add Food To Menu", command=self.add_food_to_menu)
        buy_menu = Button(self.main_window, text="Buy Menu", command=self.buy)
        report = Button(self.main_window, text="Report", command=self.show_report)
        delete_a_table = Button(self.main_window, text="Delete", command=self.show_delete_table_menu)
        consumer_register_button.grid(column=1, row=0)
        add_food_to_menu.grid(column=1, row=2)
        buy_menu.grid(column=1, row=4)
        report.grid(column=1, row=5)
        delete_a_table.grid(column=1, row=5)
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
        messagebox.showinfo('Success!', 'Costumer Added Your ID : {}'.format(costumer.id))
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

    def all_states(self, all_foods_list, costumer_id):
        print(list(self.foods_check_bar.state()))
        selected_foods = []
        for i, food in enumerate(list(self.foods_check_bar.state())):
            if food == 1:
                selected_foods.append(all_foods_list[i])
        create_bill(selected_foods=selected_foods, costumer_id=int(costumer_id.get()))


    def show_menu(self):
        self.food_menu_window = Tk()
        self.food_menu_window.title("Menu")
        costumer_id = Entry(self.food_menu_window, width=10)
        costumer_id.insert(0, "enter your id")
        costumer_id.pack(side=LEFT, anchor=W, expand=YES)
        all_foods_list = get_all_foods()
        self.foods_check_bar = CheckBar(self.food_menu_window, [food.name for food in all_foods_list], side=RIGHT)
        Button(self.food_menu_window, text='Quit', command=self.food_menu_window.quit).pack(side=BOTTOM)
        Button(self.food_menu_window, text='Peek',
               command=partial(self.all_states, all_foods_list, costumer_id)).pack(side=BOTTOM)
        self.food_menu_window.mainloop()


    def buy(self):
        self.buy_menu = Tk()
        self.buy_menu.title("Buy")
        store_id = Entry(self.buy_menu, width=10)
        store_id.insert(0, "enter store id")
        store_id.pack(side=LEFT, anchor=W, expand=YES)
        name = Entry(self.buy_menu, width=10)
        name.insert(0, "enter name")
        name.pack(side=LEFT, anchor=W, expand=YES)
        price = Entry(self.buy_menu, width=10)
        price.insert(0, "enter price")
        price.pack(side=LEFT, anchor=W, expand=YES)
        Button(self.buy_menu, text='Quit', command=self.buy_menu.quit).pack(side=BOTTOM)
        Button(self.buy_menu, text='Peek',
               command=partial(self.buy_bill, store_id, name, price)).pack(side=BOTTOM)
        # self.buy_menu.mainloop()


    def buy_bill(self, store_id, name, price):
        store_id = int(store_id.get())
        name = name.get()
        price = price.get()
        create_buy_bill(name=name, price=price, store_id=store_id)

    def show_report(self):
        sells, buy = calculate_report()
        messagebox.showinfo("Report", "Sells: {}\nBuy: {}\nfinally : {}".format(sells, -buy, sells + buy))

    def show_delete_table_menu(self):
        self.delete_table_menu = Tk()
        self.delete_table_menu.title("Delete Table")
        table_name = Entry(self.delete_table_menu, width=30)
        table_name.insert(0, "enter table name")
        table_name.pack(side=LEFT, anchor=W, expand=YES)
        Button(self.delete_table_menu, text='Quit', command=self.delete_table_menu.quit).pack(side=BOTTOM)
        Button(self.delete_table_menu, text='Peek',
               command=partial(self.delete_table, table_name)).pack(side=BOTTOM)

    def delete_table(self, table_name):
        table_name = table_name.get()
        success = delete_table_from_db(table_name=table_name)
        if success:
            messagebox.showinfo(title="Success", message="{} table dropped.".format(table_name))
        else:
            messagebox.showerror(title="Error", message="We have error!")

