from db.models.bill import Bill
from db.models.address import Address
from db.models.costumer import Costumer
from db.models.store import Store
from db.models.food import Food
from db.models.logs import Log
from db.connect import Base, engine
from view.main_window import MainWindow

if __name__ == '__main__':
    import logging

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
    Base.metadata.create_all(engine)
    view = MainWindow()
    # view.show_menu() # for reserve
    view.run() # for add and update
