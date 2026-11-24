from pickup_cost import PickupCost
from courier_cost import CourierCost
from post_cost import PostCost

class OrderService:
    def __init__(self, cost):
        self.cost = cost

    def calculate(self, weight):
        return self.cost.calculate(weight)

pickup = PickupCost()
courier = CourierCost()
post = PostCost()