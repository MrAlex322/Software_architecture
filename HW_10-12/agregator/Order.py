class Order:
    def __init__(self, id):
        self.id = id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def delete_item(self, item):
        self.items.remove(item)

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.product.price * item.quantity
        return total_price

    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = items

    def get_id(self):
        return self.id

    @staticmethod
    def get_if_present(id2):
        return None
