from Iperson import IPerson

class OwnProxyPerson(IPerson):

    def __init__(self, person):self.person = person

    def set_age(self, age):self.person.age = age
    
    def set_description(self, description):self.person.description = description
    
    def set_average_rating(self, average_rating):print("you cann't set your averag rate and you will die alone")
    
    def set_number_of_raters(self, number_of_raters):print("you cann't set your number of raters and you will die alone")

    def set_rate(self, rate):print("you cann't rate yourself and you will die alone")
    
    def get_age(self):return self.person.age
    
    def get_description(self):return self.person.description
    
    def get_average_rating(self):return self.person.average_rating
    
    def get_number_of_raters(self):return self.person.number_of_raters

    def get_rate(self):return self.person.rate
