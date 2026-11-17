from abc import ABC , abstractmethod

class absclass(ABC):
    def print(self,x):
        print("Value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside the abstract class")

class test_class(absclass):
    def task(self):
        print("We are inside test_class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)