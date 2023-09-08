from enum import Enum

class TypeCar(Enum):
    SEDAN = 1
    SUV = 2
    SPORTS_CAR = 3

class TypeFuel(Enum):
    GASOLINE = 1
    DIESEL = 2
    ELECTRIC = 3

class TypeGearbox(Enum):
    MANUAL = 1
    AUTOMATIC = 2

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

    def getMake(self):
        return self.make

    def setMake(self, make):
        self.make = make

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getBodyType(self):
        return self.bodyType

    def setBodyType(self, bodyType):
        self.bodyType = bodyType

    def getNumberWheels(self):
        return self.numberWheels

    def setNumberWheels(self, numberWheels):
        self.numberWheels = numberWheels

    def getFuel(self):
        return self.fuel

    def setFuel(self, fuel):
        self.fuel = fuel

    def getGearbox(self):
        return self.gearbox

    def setGearbox(self, gearbox):
        self.gearbox = gearbox

    def getEngineCap(self):
        return self.engineCap

    def setEngineCap(self, engineCap):
        self.engineCap = engineCap

    def movement(self):
        pass

    def maintenance(self):
        pass

    def gearShift(self, gear):
        pass

    def turnLights(self):
        return True

    def trnWprs(self):
        return True
