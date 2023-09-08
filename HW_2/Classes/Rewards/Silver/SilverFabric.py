from HW_2.Classes import ItemGenerator, IGameItem
from HW_2.Classes.Rewards.Silver import Silver

class SilverFabric(ItemGenerator):
    def create_item(self):
        return Silver()

