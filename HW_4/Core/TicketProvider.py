from Interfaces.ITicketRepo import ITicketRepo
from Models.Ticket import Ticket
from Services.TicketRepository import TicketRepository

class TicketProvider:
    def __init__(self):
        self.ticket_repo = TicketRepository.get_ticket_repository()

    def get_tickets(self, route_number):
        return self.ticket_repo.read_all(route_number)

    def update_ticket_status(self, ticket):
        ticket.set_valid(False)
        return self.ticket_repo.update(ticket)
