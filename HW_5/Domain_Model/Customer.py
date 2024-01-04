class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.orders = []

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_orders(self):
        return self.orders

    def add_order(self, order):
        self.orders.append(order)
