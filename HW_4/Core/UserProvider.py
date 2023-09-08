from Interfaces.IUserRepo import IUserRepo
from Models.User import User
from Services.UserRepository import UserRepository

class UserProvider:
    def __init__(self):
        self.client_repository = UserRepository.get_client_repository()

    def create_client(self, user_name, password_hash, card_number):
        return self.client_repository.create(user_name, password_hash, card_number)

    def get_client_by_name(self, user_name):
        client = self.client_repository.read(user_name)
        return client

    def get_all_clients(self):
        clients = self.client_repository.read_all()
        return clients
