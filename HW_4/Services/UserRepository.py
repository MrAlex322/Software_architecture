class User:
    def __init__(self, user_id, user_name, password_hash, card_number):
        self.user_id = user_id
        self.user_name = user_name
        self.password_hash = password_hash
        self.card_number = card_number

class UserRepository:
    _user_repository = None

    def __new__(cls):
        if cls._user_repository is None:
            cls._user_repository = super(UserRepository, cls).__new__(cls)
            cls._user_repository._clients = []
            cls._user_repository._initialize_clients()
        return cls._user_repository

    def _initialize_clients(self):
        # Simulating client database initialization
        self._clients.append(User(1, "Ivan", hash("1111"), 2))
        self._clients.append(User(2, "Vasiliy", hash("2222"), 3))
        self._clients.append(User(3, "Fedor", hash("3333"), 4))
        self._clients.append(User(4, "Grigoriy", hash("4444"), 5))

    def create(self, user_name, password_hash, card_number):
        user_id = len(self._clients) + 1
        new_user = User(user_id, user_name, password_hash, card_number)
        for existing_user in self._clients:
            if existing_user.user_id == new_user.user_id:
                raise RuntimeError("A client already exists")
        self._clients.append(new_user)
        return new_user.user_id

    def read(self, user_identifier):
        for client in self._clients:
            if isinstance(user_identifier, int) and client.user_id == user_identifier:
                return client
            elif isinstance(user_identifier, str) and client.user_name == user_identifier:
                return client
        raise RuntimeError("A client with this ID or username not found")

    def read_all(self):
        if not self._clients:
            raise RuntimeError("List of clients is empty")
        return self._clients

    def update(self, user):
        for i, existing_user in enumerate(self._clients):
            if existing_user.user_id == user.user_id:
                self._clients.pop(i)
                self._clients.append(user)
                return True
        return False

    def delete(self, user):
        for existing_user in self._clients:
            if existing_user == user:
                self._clients.remove(existing_user)
                return True
        return False
