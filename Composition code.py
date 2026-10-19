#Composition
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.room = Room("Living Room") 
        print(f"House built with a {self.room.name}.")

    def __del__(self):
        print("House is destroyed! The room is gone too.")

# --- Execution ---
if __name__ == "__main__":
    my_house = House()
    del my_house  #Testing composition
