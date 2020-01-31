from db.persist.persist import add_costumer, add_address_to_costumer_in_db, get_all_bills


def costumer_register(first_name, last_name, age):
    new_costumer = add_costumer(first_name=first_name, last_name=last_name, age=age)
    return new_costumer

def add_address_to_costumer(costumer, addresses_list):
    add_address_to_costumer_in_db(costumer=costumer, addresses_list=addresses_list)

def calculate_report():
    all_bills = get_all_bills()
    sells = 0
    buy = 0
    for bill in all_bills:
        if "@" in bill.food_price:
            prices = bill.food_price.split("@")
            for price in prices:
                sells += int(price)
        else:
            price = int(bill.food_price)
            if price > 0:
                sells += price
            else:
                buy += price

    return sells, buy