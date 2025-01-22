class Robot:
    def __init__(self, type, price, warranty_years, head_type, body_type, legs_type):
        self.type = type
        self.price = price
        self.warranty_years = warranty_years
        self.head_type = head_type
        self.body_type = body_type
        self.legs_type = legs_type
    
    def __str__(self) -> str:
        return "type: {}, price: {}, warrant years: {}, head type: {}, bodt type: {}, legs type: {}".format(self.type, self.price, self.warranty_years, self.head_type, self.body_type, self.legs_type)