from abc import ABC, abstractmethod

class iRefueling(ABC):
    @abstractmethod
    def fuel(self):
        pass


