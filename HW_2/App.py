from random import randint, choice

class ItemGenerator:
    def open_reward(self):
        pass

class GoldFabric(ItemGenerator):
    def open_reward(self):
        print("Opening Gold reward")

class GemFabric(ItemGenerator):
    def open_reward(self):
        print("Opening Gem reward")

class SilverFabric(ItemGenerator):
    def open_reward(self):
        print("Opening Silver reward")

class BronzeFabric(ItemGenerator):
    def open_reward(self):
        print("Opening Bronze reward")

class PlatinumFabric(ItemGenerator):
    def open_reward(self):
        print("Opening Platinum reward")

class RubyFabric(ItemGenerator):
    def open_reward(self):
        print("Opening Ruby reward")

class SapphireFabric(ItemGenerator):
    def open_reward(self):
        print("Opening Sapphire reward")

def main():
    fab1 = GoldFabric()
    fab1.open_reward()
    fab2 = GemFabric()
    fab2.open_reward()
    fab3 = SilverFabric()
    fab3.open_reward()
    fab4 = BronzeFabric()
    fab4.open_reward()
    fab5 = PlatinumFabric()
    fab5.open_reward()
    fab6 = RubyFabric()
    fab6.open_reward()
    fab7 = SapphireFabric()
    fab7.open_reward()

    fabric_list = [fab1, fab2, fab3, fab4, fab5, fab6, fab7]

    for _ in range(20):
        index = randint(0, len(fabric_list) - 1)
        fabric_list[index].open_reward()

if __name__ == "__main__":
    main()
