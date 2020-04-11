import openpyxl
from logging import getLogger

logger = getLogger(__name__)

class TorikiMenu(object):

    def __init__(self, id=None, name=None, price=None, description=None, category=None):
        self._id = id
        self._name = name
        self._price = price
        self._description = description
        self._category = category
        self.__dict__ = ({
            "id": self._id,
            "category": self.category,
            "name": self.name,
            "price": self.price,
            "description": self.description
        })


    @property
    def id(self):
        return self._id

    @property
    def category(self):
        return self._category

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def description(self):
        return self._description




