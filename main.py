from db.models.bill import Bill
from db.models.address import Address
from db.models.costumer import Costumer
from db.models.store import Store
from db.connect import Base, engine


if __name__ == '__main__':
    Base.metadata.create_all(engine)
