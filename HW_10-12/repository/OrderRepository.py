from abc import ABC, abstractmethod
from agregator import Order
from typing import List

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order):
        pass

    @abstractmethod
    def get_by_id(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def get_all(self) -> List[Order]:
        pass
