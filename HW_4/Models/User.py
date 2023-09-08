class User:
    def __init__(self, id, user_name, hash_password, card_number):
        self.id = id
        self.user_name = user_name
        self.hash_password = hash_password
        self.card_number = card_number

    def get_id(self):
        return self.id

    def get_user_name(self):
        return self.user_name

    def get_hash_password(self):
        return self.hash_password

    def get_card_number(self):
        return self.card_number

    def __str__(self):
        return f"Client {{ id= {self.id}, user_name= {self.user_name}, card_number= {str(self.card_number).zfill(16)} }}"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.equals(other)

    def equals(self, other):
        return (
            other
            and self.id == other.id
            and self.hash_password == other.hash_password
            and self.card_number == other.card_number
            and self.user_name == other.user_name
        )

    def __hash__(self):
        return hash((self.id, self.user_name, self.hash_password, self.card_number))
