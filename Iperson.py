from abc import ABC

class IPerson(ABC):
    
    def __init__(self, age, description, average_rating, number_of_raters, rate):
        self.age = age
        self.description = description
        self.average_rating = average_rating
        self.number_of_raters = number_of_raters
        self.rate = rate
    
    def set_age(self, age):pass
    def set_description(self, description):pass
    def set_average_rating(self, average_rating):pass
    def set_number_of_raters(self, number_of_raters):pass
    def set_rate(self, number_of_raters):pass

    def get_age(self):pass
    def get_description(self):pass
    def get_average_rating(self):pass
    def get_number_of_raters(self):pass
    def get_rate(self):pass


