from enum import Enum

class TypeCar(Enum):
    SEDAN = 1
    SUV = 2
    PICKUP = 3

class TypeFuel(Enum):
    GASOLINE = 1
    DIESEL = 2
    ELECTRIC = 3

class TypeGearbox(Enum):
    MANUAL = 1
    AUTOMATIC = 2

class iRefueling:
    def fuel(self):
        pass

class Car:
    def __init__(self, make, model, color, bodyType, numberWheels, fuel, gearbox, engineCap):
        self.make = make
        self.model = model
        self.color = color
        self.bodyType = bodyType
        self.numberWheels = numberWheels
        self.fuel = fuel
        self.gearbox = gearbox
        self.engineCap = engineCap

    def gearShift(self, gear):
        return 0

class Pickup(Car, iRefueling):
    def __init__(self, make, model, color, bodyType, numberWheels, fuel, gearbox, engineCap, loadCapacity):
        super().__init__(make, model, color, bodyType, numberWheels, fuel, gearbox, engineCap)
        self.loadCapacity = loadCapacity

    def getLoadCapacity(self):
        return self.loadCapacity

    def setLoadCapacity(self, loadCapacity):
        self.loadCapacity = loadCapacity

    def fuel(self):
        pass
