class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
