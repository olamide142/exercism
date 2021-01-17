import string
import random

class Robot:
    __robots = []

    def __init__(self):
        self.name = self.random_name()

    def reset(self):
        self.__robots.remove(self.name)
        self.name = self.random_name()
        
    def random_name(self):
        random.seed(None)
        while 1:
            a = "".join([random.choice(list(string.ascii_uppercase)) for i in range(2)])
            b = "".join([random.choice(list(string.digits)) for i in range(3)])
            if a+b not in self.__robots:
                self.__robots.append(a+b)
                break
            else:
                continue
        return a+b