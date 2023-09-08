class CashRepository:
    _cash_repository = None

    def __init__(self):
        # Simulate bank accounts as a list of BankAccount objects
        self.clients = [BankAccount() for _ in range(5)]

    @classmethod
    def get_cash_repository(cls):
        if cls._cash_repository is None:
            cls._cash_repository = CashRepository()
        return cls._cash_repository

    def transaction(self, payment, card_from, carrier_card):
        # Validate accounts
        from_account = None
        to_account = None
        for client in self.clients:
            if client.get_card() == card_from:
                from_account = client
            if client.get_card() == carrier_card:
                to_account = client

        # Check the existence of the accounts
        if from_account is None:
            raise Exception("No withdrawal account.")
        if to_account is None:
            raise Exception("No money account.")

        # Check the balances
        if from_account.get_balance() - payment < 0:
            raise Exception("Insufficient funds.")
        if to_account.get_balance() > 2**31 - payment:
            raise Exception("Too much amount.")

        # Perform the transaction within a try-finally block to ensure it always executes
        try:
            pass  # You can add any additional logic here if needed
        finally:
            self.clients.remove(from_account)
            self.clients.remove(to_account)
            from_account.set_balance(from_account.get_balance() - payment)
            to_account.set_balance(to_account.get_balance() + payment)
            self.clients.append(from_account)
            self.clients.append(to_account)

        return True


class BankAccount:
    def __init__(self):
        self.card = self.generate_card_number()
        self.balance = 1000

    def generate_card_number(self):
        return int("".join(str(randint(0, 9)) for _ in range(16)))

    def get_card(self):
        return self.card

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance
