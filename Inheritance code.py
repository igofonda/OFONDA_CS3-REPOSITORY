#Inheritance
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof!")
if __name__ == "__main__":
    my_dog = Dog()
    my_dog.eat()   
    my_dog.bark()
