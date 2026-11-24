from delivery_cost import DeliveryCost

class PostCost(DeliveryCost):
    def calculate(self, weight):
        return 300 + 50 * weight