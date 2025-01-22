from Iperson import IPerson

class RealPerson(IPerson):
    def __init__(self, age, description):
        super().__init__(age, description, 0, 0, 0)

    def set_age(self, age):self.age = age
    
    def set_description(self, description):self.description = description
    
    def set_average_rating(self, average_rating):self.average_rating = average_rating
    
    def set_number_of_raters(self, number_of_raters):self.number_of_raters=number_of_raters

    def set_rate(self, rate):self.rate=rate

    def get_age(self):return self.age
    
    def get_description(self):return self.description
    
    def get_average_rating(self):return self.average_rating
    
    def get_number_of_raters(self):return self.number_of_raters

    def get_rate(self):return self.rate
