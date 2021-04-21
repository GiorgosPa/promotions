class promotion_observer:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(promotion_observer, cls).__new__(cls)
            cls.instance.promotions = []
        return cls.instance

    def update(self, promotion):
        self.instance.promotions.append(promotion)
