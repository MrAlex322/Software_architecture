import sqlite3
from agregator import Order, OrderItem, Product
from repository import OrderRepository
from typing import List

class OrderRepositoryImpl(OrderRepository):
    def __init__(self):
        # Инициализация соединения с базой данных
        self.connection = sqlite3.connect('database.db')

    def save(self, order: Order):
        # Сохранение заказа в базу данных
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO orders (id) VALUES (?)", (order.get_id(),))
            self.connection.commit()

            for item in order.get_items():
                cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                               (order.get_id(), item.get_product().get_id(), item.get_quantity()))
                self.connection.commit()
        except sqlite3.Error as e:
            print("SQLite error:", e)

    def get_by_id(self, order_id: int) -> Order:
        # Загрузка заказа по ID из базы данных
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
            order_row = cursor.fetchone()

            if order_row:
                order = Order(order_row[0])

                cursor.execute("SELECT * FROM order_items WHERE order_id = ?", (order_id,))
                items_rows = cursor.fetchall()

                for item_row in items_rows:
                    product_id = item_row[1]
                    quantity = item_row[2]

                    # Загрузка продукта из базы данных
                    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
                    product_row = cursor.fetchone()

                    if product_row:
                        product = Product(product_row[0], product_row[1], product_row[2])
                        order.add_item(OrderItem(product, quantity))

                return order
        except sqlite3.Error as e:
            print("SQLite error:", e)

        return None

    def get_all(self) -> List[Order]:
        # Загрузка всех заказов из базы данных
        orders = []

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM orders")
            order_rows = cursor.fetchall()

            for order_row in order_rows:
                order_id = order_row[0]
                order = self.get_by_id(order_id)

                if order:
                    orders.append(order)
        except sqlite3.Error as e:
            print("SQLite error:", e)

        return orders
