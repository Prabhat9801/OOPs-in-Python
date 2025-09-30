# Method Overriding in Python- A method in a child class can override a method with the same name in the parent class.
# Polymorphism - the ability to present the same interface for differing underlying data types.
# if Parent and Child class have the same method name, then the method in the child class is called overriding method.
# if Parent and Child class both have the cunstructor, then the constructor in the child class is called overriding constructor.
# Method overriding is used to provide specific implementation of a method that is already provided by its parent class.
# if the Child class does not have the method, then the method from the Parent class is called.
# if the child class doesn't have the constructor, then the constructor from the Parent class is called.
# super() function is used to call the method from the Parent class.
# super() does not work with variables.
# super() does not work outside the class.


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):
    def buy(self):
        print("Buying a smartphone")

s = Smartphone("Apple", "iPhone 14", 999)
s.buy()