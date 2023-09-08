from HW_2.Classes  import ItemGenerator, IGameItem
from HW_2.Classes.Rewards.Gem import Gem

class GemFabric(ItemGenerator):
    def create_item(self):
        return Gem()
