from HW_2.Classes import ItemGenerator, IGameItem
from HW_2.Classes.Rewards.Gold import Gold

class GoldFabric(ItemGenerator):
    def create_item(self):
        return Gold()
