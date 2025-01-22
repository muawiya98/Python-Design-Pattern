from Ipizza import IPizza
class PlainPizza(IPizza):

    def __init__(self):
        self.description = "3agena 5afefa"
        self.cost = 10

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost