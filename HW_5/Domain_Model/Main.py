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


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


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


if __name__ == "__main__":
    customer = Customer("1", "Иван Иванов")

    product1 = Product("1", "Телефон", 10000.0)
    product2 = Product("2", "Ноутбук", 50000.0)

    order = Order("1")
    order.add_product(product1)
    order.add_product(product2)

    customer.add_order(order)

    print("Клиент: " + customer.get_name())
    print("Заказы:")
    for customer_order in customer.get_orders():
        print("Заказ №" + customer_order.get_order_id())
        print("Товары:")
        for product in customer_order.get_products():
            print("- " + product.get_name() + " (" + str(product.get_price()) + " руб.)")
        print()
