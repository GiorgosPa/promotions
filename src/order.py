import line
import SKU

class order:

    def __init__(self):
        self.lines = []

    def add_line(self, SKU, quantity):
        self.lines.append(line(SKU, quantity))