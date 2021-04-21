from order import order
from SKU import SKU
from promotion import promotion

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