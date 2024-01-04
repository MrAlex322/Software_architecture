class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.products = []

    def get_order_id(self):
        return self.order_id

    def get_products(self):
        return self.products

    def add_product(self, product):
        self.products.append(product)
