#Realization (Implementation)
from abc import ABC, abstractmethod

class Shape(ABC):  # Interface contract
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):  # Realizes Shape
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

# --- Execution ---
if __name__ == "__main__":
    my_circle = Circle(5)
    print(f"Circle Area: {my_circle.get_area()}")

