from Interfaces.ICarrierRepo import ICarrierRepo
from Interfaces.ICashRepo import ICashRepo
from Models.Carrier import Carrier
from Models.Ticket import Ticket
from Models.User import User
from Services.CarrierRepository import CarrierRepository
from Services.CashRepository import CashRepository

class CashProvider:
    def __init__(self):
        self.card_number = 0
        self.is_authorized = False
        self.carrier_repository = CarrierRepository.get_carrier_repository()
        self.cash_repository = CashRepository.get_cash_repository()

    def buy(self, ticket):
        if self.is_authorized:
            carrier = self.carrier_repository.read(1)
            return self.cash_repository.transaction(ticket.get_price(), self.card_number, carrier.get_card_number())
        return False

    def authorization(self, client):
        self.card_number = client.get_card_number()
        self.is_authorized = True
