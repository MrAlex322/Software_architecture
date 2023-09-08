from Models.Ticket import Ticket
from Models.User import User
from Core.UserProvider import UserProvider
from abc import ABC, abstractmethod
from typing import List
from datetime import date

class ICustomer(ABC):
    @abstractmethod
    def get_selected_tickets(self) -> List[Ticket]:
        pass

    @abstractmethod
    def set_selected_tickets(self, selected_tickets: List[Ticket]) -> None:
        pass

    @abstractmethod
    def get_user(self) -> User:
        pass

    @abstractmethod
    def set_user(self, client: User) -> None:
        pass

    @abstractmethod
    def get_user_provider(self) -> UserProvider:
        pass

    @abstractmethod
    def buy_ticket(self, ticket: Ticket) -> bool:
        pass

    @abstractmethod
    def search_ticket(self, date: date, route: int) -> List[Ticket]:
        pass
