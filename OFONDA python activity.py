class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  

    def get_age(self):
        return self.__age

   
    def set_age(self, new_age):
        self.__age = new_age

person1 = Person("Rocco", "14")
print(person1.name)       
print(person1.get_age())  # so that it cannot be accessed by the public, as well as being more secure
