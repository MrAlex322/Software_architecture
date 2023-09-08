from HW_2.Classes import ItemGenerator, IGameItem
from HW_2.Classes.Rewards.Sapphire import Sapphire

class SapphireFabric(ItemGenerator):
    def create_item(self):
        return Sapphire()

