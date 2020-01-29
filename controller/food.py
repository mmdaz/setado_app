from db.persist.persist import add_food


def add_new_food(name, price):
    add_food(name=name, price=price)
