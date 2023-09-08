class BankAccount:
    old_card = 0

    def __init__(self):
        self.card = BankAccount.old_card + 1
        BankAccount.old_card = self.card
        self.balance = 1000

    def set_balance(self, balance):
        self.balance = balance

    def get_card(self):
        return self.card

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount {{ card= {str(self.card).zfill(16)}, balance= {self.balance} }}"
