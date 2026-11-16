class Person:  #Exercise 1
    def __init__(self, name, age):
        self.name = name
        self.__age = age  

    def get_age(self):
        return self.__age

   
    def set_age(self, new_age):
        self.__age = new_age

#Exercise 2
person1 = Person("OB", "15")
print(f"Name: {person1.name}")       
print(f"Age: {person1.get_age()}\n")  # so that it cannot be accessed by the public, as well as being more secure

#Exercise 3
class Student(Person):
    def study(self):
        print(f"{self.name} is studying.\n")


student1 = Student("Rocco", 14)


print(f"Name: {student1.name}")     
print(f"Age: {student1.get_age()}")  

student1.study()           

#Exercise 4
class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching\n")

teacher1 = Teacher("Mona", 30)
print(f"Name: {teacher1.name}")
print(f"Age: {teacher1.get_age()}")

teacher1.teach()