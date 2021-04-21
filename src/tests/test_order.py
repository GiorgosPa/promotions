from order import order
from SKU import SKU
from promotion import promotion
from promotion_observer import promotion_observer

def test_calculate_total():
    a = SKU('A', 10)
    b = SKU('B', 30)

    o = order()
    o.add_line(a, 3)
    o.add_line(b, 2)

    assert o.calculate_total() == 90

def test_calculate_total_with_promotions():
    a = SKU('A', 10)
    b = SKU('B', 30)

    o = order()
    o.add_line(a, 3)
    o.add_line(b, 2)

    p = promotion(20)
    p.add_line(a, 3)

    assert o.calculate_total() == 80

    tear_down()

def test_scenario_A():
    setup()

    o = order()
    o.add_line(a, 1)
    o.add_line(b, 1)
    o.add_line(c, 1)

    assert o.calculate_total() == 100

    tear_down()

def test_scenario_B():
    setup()

    o = order()
    o.add_line(a, 5)
    o.add_line(b, 5)
    o.add_line(c, 1)

    assert o.calculate_total() == 370

    tear_down()

def test_scenario_C():
    setup()

    o = order()
    o.add_line(a, 3)
    o.add_line(b, 5)
    o.add_line(c, 1)
    o.add_line(d, 1)

    assert o.calculate_total() == 280

    tear_down()


def setup():
    global a,b,c,d
    a = SKU('A', 50)
    b = SKU('B', 30)
    c = SKU('C', 20)
    d = SKU('D', 15)

    p1 = promotion(130)
    p1.add_line(a, 3)

    p2 = promotion(45)
    p2.add_line(b, 2)

    p3 = promotion(30)
    p3.add_line(c, 1)
    p3.add_line(d, 1)

def tear_down():
    observer = promotion_observer()
    observer.promotions = []