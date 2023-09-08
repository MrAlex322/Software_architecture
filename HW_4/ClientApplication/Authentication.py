from Core.UserProvider import UserProvider
from Models.User import User

class Authentication:
    @staticmethod
    def authentication(user_provider, login, pass_hash):
        client = user_provider.get_client_by_name(login)
        if client.get_hash_password() == pass_hash:
            return client
        else:
            raise RuntimeError("Authentication fail")