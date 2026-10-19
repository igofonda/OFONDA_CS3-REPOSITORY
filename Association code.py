#Association
class Course:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"Student {self.name} enrolled in {course.name}.")

# --- Execution ---
if __name__ == "__main__":
    alice = Student("Alice")
    cs101 = Course("Computer Science 101")
    alice.enroll(cs101)
