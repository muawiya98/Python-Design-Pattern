
class MenuItem:

    def __init__(self, name:str, description:str, vegetarian:bool, price:float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    def is_vegetarian(self):
        return self.vegetarian