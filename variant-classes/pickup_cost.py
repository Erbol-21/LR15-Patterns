from delivery_cost import DeliveryCost

class PickupCost(DeliveryCost):
    def calculate(self, weight):
        return 0