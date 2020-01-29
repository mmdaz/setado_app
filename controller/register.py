from db.persist.persist import add_costumer, add_address_to_costumer_in_db


def costumer_register(first_name, last_name, age):
    new_costumer = add_costumer(first_name=first_name, last_name=last_name, age=age)
    return new_costumer

def add_address_to_costumer(costumer, addresses_list):
    print(addresses_list)
    add_address_to_costumer_in_db(costumer=costumer, addresses_list=addresses_list)
