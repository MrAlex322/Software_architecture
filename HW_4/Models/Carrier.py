class Carrier:
    def __init__(self, id, card_number):
        self.id = id
        self.card_number = card_number
        self.zones = [0, 1]

    def get_card_number(self):
        return self.card_number

    def get_id(self):
        return self.id
