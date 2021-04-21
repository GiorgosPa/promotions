from line import line
from promotion_observer import promotion_observer
from functools import reduce

class order:

    def __init__(self):
        self.lines = []
        self.promotions = []

    def add_line(self, SKU, quantity):
        self.lines.append(line(SKU, quantity))

    def calculate_total(self):
        total = 0

        observer = promotion_observer()
        for promotion in observer.promotions:
            self._apply_promotion(promotion)

        for line in self.lines:
            total += line.SKU.price * line.quantity

        for promotion in self.promotions:
            total += promotion.price

        return total

    def _apply_promotion(self, promotion):
        matched_all_lines = len(promotion.lines) > 0
        for line in promotion.lines:
            found_lines = [x for x in self.lines if x.SKU is line.SKU]
            if len(found_lines) > 1:
                total = reduce(lambda a,b: a.quantity + b.quantity, found_lines)
            else:
                total = found_lines[0].quantity
            quantity = line.quantity
            line_matched = quantity <= total
            matched_all_lines = matched_all_lines and line_matched

        if not matched_all_lines:
            return False
        
        for line in promotion.lines:
            self._apply_promotion_line(line)
        
        self.promotions.append(promotion)
            
        self.lines = [x for x in self.lines if x.quantity > 0]

        return True

    def _apply_promotion_line(self, line):
        remaining_quantity = line.quantity
        for order_line in self.lines:
            if order_line.SKU is line.SKU:
                if remaining_quantity <= order_line.quantity:
                    order_line.quantity -= remaining_quantity
                    remaining_quantity = 0
                else:
                    remaining_quantity -= order_line.quantity
                    order_line.quantity = 0
