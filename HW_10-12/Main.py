class Order:
    def __init__(self, id, price):
        self.id = id
        self.price = price

    def __str__(self):
        return f"Order{{id={self.id}, price={self.price}}}"


class Main:
    def __init__(self):
        self.orders = []

    def main(self):
        self.orders = self.orders_from_database()
        self.list_orders()

    def orders_from_database(self):
        order_list = []
        order_list.append(Order(1, 3565.98))
        order_list.append(Order(2, 186.65))
        order_list.append(Order(3, 789.30))
        return order_list

    def list_orders(self):
        for order in self.orders:
            print(order)


if __name__ == "__main__":
    main = Main()
    main.main()
