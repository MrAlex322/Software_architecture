from datetime import date

class Ticket:
    def __init__(self, route_number, seat_number, price, valid_until, is_valid):
        self.route_number = route_number
        self.seat_number = seat_number
        self.price = price
        self.valid_until = valid_until
        self.is_valid = is_valid

class TicketRepository:
    _ticket_repository = None

    def __new__(cls):
        if cls._ticket_repository is None:
            cls._ticket_repository = super(TicketRepository, cls).__new__(cls)
            cls._ticket_repository._tickets = []
            str_date = "2022-10-27"
            date_format = "%Y-%m-%d"
            try:
                date_obj = date.fromisoformat(str_date)
            except ValueError:
                date_obj = None
            cls._ticket_repository._generate_tickets(1, 6, 10, date_obj)
            cls._ticket_repository._generate_tickets(2, 4, 15, date_obj)
        return cls._ticket_repository

    def create(self, ticket):
        # Functionality not used
        self._tickets.append(ticket)
        return True

    def read_all(self, route_number):
        route_tickets = []
        for ticket in self._tickets:
            if ticket.route_number == route_number and ticket.is_valid:
                route_tickets.append(ticket)
        if not route_tickets:
            raise RuntimeError("There are no tickets for this bus.")
        return route_tickets

    def update(self, ticket):
        for i, tick in enumerate(self._tickets):
            if tick == ticket:
                self._tickets.pop(i)
                self._tickets.append(ticket)
                return True
        return False

    def delete(self, ticket):
        # Functionality not used
        if ticket in self._tickets:
            self._tickets.remove(ticket)
            return True
        return False

    def _generate_tickets(self, route_number, count_places, price, date):
        for i in range(1, count_places + 1):
            self._tickets.append(Ticket(route_number, i, price, date, True))

