from Models.Ticket import Ticket
from typing import List

class ITicketRepo:
    def create(self, ticket: Ticket) -> bool:
        pass

    def read_all(self, route_number: int) -> List[Ticket]:
        pass

    def update(self, ticket: Ticket) -> bool:
        pass

    def delete(self, ticket: Ticket) -> bool:
        pass
