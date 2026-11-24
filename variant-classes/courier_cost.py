from delivery_cost import DeliveryCost

class CourierCost(DeliveryCost):
    def calculate(self, weight):
        return 500