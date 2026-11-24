def pickup(weight):
    return 0

def courier(weight):
    return 500

def post(weight):
    return 300 + 50 * weight

class OrderService:
    def __init__(self, cost):
        self.cost = cost

    def calculate(self, weight):
        return self.cost(weight)