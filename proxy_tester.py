from real_person import RealPerson
from own_proxy_person import OwnProxyPerson
from other_proxy_person import OtherProxyPerson

class ProxyTester:

    def run(self):
        real_person = RealPerson(25, 'Male')
        own_proxy = OwnProxyPerson(real_person)
        print(own_proxy.get_age())
        own_proxy.set_average_rating(5)
        print(own_proxy.get_average_rating())

        other_proxy = OtherProxyPerson(real_person)
        print(other_proxy.get_age())
        other_proxy.set_average_rating(4)
        print(other_proxy.get_average_rating())

        print(own_proxy.get_average_rating())



if __name__=="__main__":
    proxy_tester = ProxyTester()
    proxy_tester.run()
