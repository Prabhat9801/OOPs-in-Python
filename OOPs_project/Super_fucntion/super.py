# Super function is used to call the parent class constructor and methods
# super() function is used to call the method from the Parent class.
# super() does not work with variables.
# super() does not work outside the class.
# super() function must the 1st statrement in the constructor of the child class.

class Parent:

    def __init__(self, num):
        self.num = num

    def get_num(self):
        return self.num
    
class Child(Parent):

    def __init__(self, num, val):
        super().__init__(num)  # calling the constructor of the Parent class
        self.val = val

    def get_val(self):
        return self.val
    
son = Child(10, 100)
print(son.get_num())
print(son.get_val())    