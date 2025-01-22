from Iperson import IPerson

class OtherProxyPerson(IPerson):

    def __init__(self, person):self.person = person
 
    def set_age(self, age):pass
    
    def set_description(self, description):pass
    
    def set_average_rating(self, average_rating):self.person.average_rating = average_rating
    
    def set_number_of_raters(self, number_of_raters):self.person.number_of_raters = number_of_raters

    def set_rate(self, rate):self.person.rate = rate
    
    def get_age(self):return self.person.age
    
    def get_description(self):return self.person.description
    
    def get_average_rating(self):return self.person.average_rating
    
    def get_number_of_raters(self):return self.person.number_of_raters

    def get_rate(self):return self.person.rate
