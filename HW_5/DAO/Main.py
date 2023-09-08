class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserDao:
    def add_user(self, user):
        pass  

    def get_user(self, name):
        pass  

    def update_user(self, user):
        pass  

    def delete_user(self, user):
        pass  

class UserDaoImpl(UserDao):
    def add_user(self, user):
        pass

    def get_user(self, name):
        pass

    def update_user(self, user):
        pass

    def delete_user(self, user):
        pass

if __name__ == "__main__":
    user_dao = UserDaoImpl()

    user1 = User("Иван", 25)
    user_dao.add_user(user1)

    user2 = user_dao.get_user("Николай")
    user2.age = 30
    user_dao.update_user(user2)

    user_dao.delete_user(user2)
