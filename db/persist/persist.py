from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError

from db.connect import session, engine
from db.models.address import Address
from db.models.bill import Bill
from db.models.costumer import Costumer
from db.models.courier import Courier
from db.models.food import Food
from db.models.store import Store


def add_costumer(first_name, last_name, age):
    try:
        new_costumer = Costumer(first_name=first_name, last_name=last_name, age=age)
        session.add(new_costumer)
        return new_costumer
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in add_costumer, {}".format(e))


def add_address_to_costumer_in_db(costumer, addresses_list: list):
    try:
        for address in addresses_list:
            costumer.addresses.append(address)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in add_address_to_costumer, {}".format(e))


def add_food(name, price):
    try:
        new_food = Food(name=name, price=int(price), created_at=datetime.now())
        session.add(new_food)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in add_food, {}".format(e))


def get_all_foods():
    try:
        return session.query(Food).all()
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in get_all_foods, {}".format(e))


def create_bill(selected_foods, costumer_id):
    try:
        selected_foods_name = "@".join([food.name for food in selected_foods])
        selected_foods_prices = "@".join([str(food.price) for food in selected_foods])
        bill = Bill(food_name=selected_foods_name, food_price=selected_foods_prices, created_at=datetime.now(),
                    costumer_id=costumer_id)
        session.add(bill)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in create bill, {}".format(e))

def create_buy_bill(name, price, store_id):
    try:
        bill = Bill(food_name=name, food_price=str(-int(price)), store_id=store_id, created_at=datetime.now())
        session.add(bill)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in create_buy_bill, {}".format(e))

def get_all_bills():
    try:
        return session.query(Bill).all()
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in get_all_bills, {}".format(e))

def delete_table_from_db(table_name):
    try:
        if table_name == "costumer":
            Address.__table__.drop(engine)
            Bill.__table__.drop(engine)
            Costumer.__table__.drop(engine)
        elif table_name == "store":
            Address.__table__.drop(engine)
            Bill.__table__.drop(engine)
            Store.__table__.drop(engine)
        elif table_name == "courier":
            Courier.__table__.drop(engine)
        elif table_name == "food":
            Food.__table__.drop(engine)

        return True
    except Exception as e:
        session.rollback()
        print("we have error in delete_table_from_db, {}".format(e))
        return False

def delete_food_from_db(food_name):
    try:
        session.query(Food).filter(Food.name == food_name).delete()
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print("we have error in delete_food, {}".format(e))
        return False
