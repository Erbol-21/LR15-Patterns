from order_service import OrderService, pickup, courier, post

def test_pickup():
    service = OrderService(pickup)
    assert service.calculate(3) == 0

def test_courier():
    service = OrderService(courier)
    assert service.calculate(3) == 500

def test_post():
    service = OrderService(post)
    assert service.calculate(3) == 450