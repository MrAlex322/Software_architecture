from HW_2.Classes import IGameItem, ItemGenerator
from HW_2.Classes.Rewards.Bronze import Bronze

class BronzeFabric(ItemGenerator):
    def create_item(self):
        return Bronze()

