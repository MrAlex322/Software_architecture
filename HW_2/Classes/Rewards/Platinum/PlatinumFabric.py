from HW_2.Classes import ItemGenerator, IGameItem
from HW_2.Classes.Rewards.Platinum import Platinum

class PlatinumFabric(ItemGenerator):
    def create_item(self):
        return Platinum()

