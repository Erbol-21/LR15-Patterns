from abc import ABC, abstractmethod

class DeliveryCost(ABC):
    @abstractmethod
    def calculate(self, weight):
        pass