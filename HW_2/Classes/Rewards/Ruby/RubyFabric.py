from HW_2.Classes import ItemGenerator, IGameItem
from HW_2.Classes.Rewards.Ruby import Ruby

class RubyFabric(ItemGenerator):
    def create_item(self):
        return Ruby()

