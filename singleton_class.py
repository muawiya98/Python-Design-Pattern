# # Simple Singleton
# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance

#     def __init__(self):
#         if not hasattr(self, 'initialized'):
#             self.initialized = True


# # Singleton for multi threading, with take care about the main&cache memory problem
import threading

class Singleton:
    _instance = None  # Class variable to hold the single instance
    _lock = threading.Lock()  # Lock for thread-safe instantiation

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Check if instance is already created
            with cls._lock:  # Ensure that only one thread can enter this block
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Ensure init is only called once
            self.initialized = True