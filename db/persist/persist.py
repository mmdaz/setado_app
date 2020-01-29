from sqlalchemy.exc import SQLAlchemyError

from db.connect import session
from db.models.address import Address
from db.models.costumer import Costumer


def add_costumer(first_name, last_name, age):
    try:
        new_costumer = Costumer(first_name=first_name, last_name=last_name, age=age)
        session.add(new_costumer)
        return new_costumer
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in add_costumer, {}".format(e))

def add_address_to_costumer_in_db(costumer, name, address, phone):
    try:
        new_address = Address(name=name, address=address, phone=phone)
        costumer.addresses.append(new_address)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("we have error in add_address_to_costumer, {}".format(e))
