from abc import ABC, abstractmethod

class ItemGenerator(ABC):
    def open_reward(self):
        game_item = self.create_item()
        game_item.open()

    @abstractmethod
    def create_item(self):
        pass

class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass

