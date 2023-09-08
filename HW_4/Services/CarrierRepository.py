class CarrierRepository:
    _carrier_repository = None

    def __init__(self):
        # Initialize the list of carriers as an empty list
        self.carriers = []
        # Add some initial carriers to simulate database records
        self.carriers.append(Carrier(1, 1))

    @classmethod
    def get_carrier_repository(cls):
        if cls._carrier_repository is None:
            cls._carrier_repository = CarrierRepository()
        return cls._carrier_repository

    def read(self, id):
        for carrier in self.carriers:
            if carrier.get_id() == id:
                return carrier
        raise Exception("A carrier with this ID not found")


class Carrier:
    def __init__(self, id, card_number):
        self.id = id
        self.card_number = card_number

    def get_id(self):
        return self.id

    def get_card_number(self):
        return self.card_number
