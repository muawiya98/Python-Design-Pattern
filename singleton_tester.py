from singleton_class import Singleton
import threading
class SingeletonTester:

    def create_singleton(self):
        instance = Singleton()
        print(instance)
    
    def run(self):

        thread1 = threading.Thread(target=self.create_singleton)#, args=())
        thread2 = threading.Thread(target=self.create_singleton)#, args=())

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        # Check if both references are the same instance
        singleton1 = Singleton()
        singleton2 = Singleton()
        print(singleton1 is singleton2)  # Output: True (both are the same instance)


if __name__=="__main__":
    singleton_tester = SingeletonTester()
    singleton_tester.run()