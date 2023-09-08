from Interfaces.ICustomer import ICustomer
from Models.Ticket import Ticket
from Models.User import User
from Core.CashProvider import CashProvider
from Core.TicketProvider import TicketProvider
from Core.UserProvider import UserProvider

class Customer(ICustomer):
    def __init__(self):
        self.ticket_provider = TicketProvider()
        self.cash_provider = CashProvider()
        self.user_provider = UserProvider()
        self.client = None
        self.selected_tickets = []

    def get_selected_tickets(self):
        return self.selected_tickets

    def set_selected_tickets(self, selected_tickets):
        self.selected_tickets = selected_tickets

    def get_user_provider(self):
        return self.user_provider

    def get_user(self):
        return self.client

    def set_user(self, client):
        self.client = client

    def buy_ticket(self, ticket):
        flag = False
        self.cash_provider.authorization(self.client)
        flag = self.cash_provider.buy(ticket)
        if flag:
            flag = self.ticket_provider.update_ticket_status(ticket)
        return flag

    def search_ticket(self, date, route):
        result = []
        ticket_list = self.ticket_provider.get_tickets(route)
        for ticket in ticket_list:
            if ticket.get_date() == date:
                result.append(ticket)
        if not result:
            raise RuntimeError("There are no tickets for this date")
        return result
