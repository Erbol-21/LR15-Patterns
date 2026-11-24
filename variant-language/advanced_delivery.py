tariffs = {"base": 300, "kg": 50}
count = 0

def post_delivery(weight):
    global count
    count += 1
    return tariffs["base"] + tariffs["kg"] * weight


class PostDelivery:
    def __init__(self, tariffs):
        self.tariffs = tariffs
        self.count = 0

    def calculate(self, weight):
        self.count += 1
        return self.tariffs["base"] + self.tariffs["kg"] * weight


print("Вариант с функцией")
print("Стоимость:", post_delivery(3))
print("Стоимость:", post_delivery(5))
print("Количество заказов:", count)

print("\nВариант с классом")
delivery = PostDelivery(tariffs)
print("Стоимость:", delivery.calculate(3))
print("Стоимость:", delivery.calculate(5))
print("Количество заказов:", delivery.count)