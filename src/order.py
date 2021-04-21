from line import line

class order:

    def __init__(self):
        self.lines = []

    def add_line(self, SKU, quantity):
        self.lines.append(line(SKU, quantity))

    def calculate_total(self):
        total = 0
        for line in self.lines:
            total += line.SKU.price * line.quantity
        return total