from line import line

class promotion:

    def __init__(self, price):
        self.lines = []
        self.price = price
    
    def add_line(self, SKU, quantity):
        self.lines.append(line(SKU, quantity))