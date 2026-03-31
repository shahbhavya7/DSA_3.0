class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def bark(self):        # it overrides the speak method of the Animal class
        return "Woof"



# inheriting the Dog and Cat classes from the Animal class
dog = Dog()
print(dog.speak())  # Output: Woof

class bank:
    def __init__(self, name):
        self.__name = name # private variable

    def get_name(self):
        return self.__name # getter method to access the private variable
