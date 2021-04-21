from line import line
from promotion_observer import promotion_observer

class promotion:

    def __init__(self, price):
        self.lines = []
        self.price = price
        observer = promotion_observer()
        observer.update(self)
    
    def add_line(self, SKU, quantity):
        self.lines.append(line(SKU, quantity))