class OrderCache:
    def __init__(self):
        self.cache = {}

    def get_order(self, id, order_list):
        if id in self.cache:
            return self.cache[id]
        else:
            for order in order_list:
                if order.get_id() == id:
                    self.cache[id] = order
                    return order
            return None

    def update_order(self, order, order_list):
        self.cache[order.get_id()] = order
        for i in range(len(order_list)):
            if order_list[i].get_id() == order.get_id():
                order_list[i] = order
                break
