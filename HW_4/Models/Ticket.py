class Ticket:
    def __init__(self, route_number, place, price, date, is_valid):
        self.route_number = route_number
        self.place = place
        self.price = price
        self.date = date
        self.is_valid = is_valid
        self.zone_start = None
        self.zone_stop = None

    def get_route_number(self):
        return self.route_number

    def get_place(self):
        return self.place

    def get_price(self):
        return self.price

    def get_date(self):
        return self.date

    def is_valid(self):
        return self.is_valid

    def set_zone_start(self, zone_start):
        self.zone_start = zone_start

    def set_zone_stop(self, zone_stop):
        self.zone_stop = zone_stop

    def to_string(self):
        return f"Ticket\nRoute Number {self.route_number}\nPlace {self.place}\nPrice {self.price} rub.\nDate {self.date}\n{'Free' if self.is_valid else 'Busy'}"

    def to_print(self):
        return f"Ticket\nRoute Number {self.route_number}\nPlace {self.place}\nPrice {self.price} rub.\nDate {self.date}"

    def __hash__(self):
        return hash(self.date) ^ (self.route_number + self.place + self.price)

    def __eq__(self, other):
        if not isinstance(other, Ticket):
            return False
        return self.equals(other)

    def equals(self, other):
        return (
            other
            and other.get_route_number() == self.route_number
            and other.get_place() == self.place
            and other.get_price() == self.price
            and other.get_date() == self.date
            and hash(other) == hash(self)
        )
