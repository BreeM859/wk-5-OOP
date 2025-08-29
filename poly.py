# Base class (not strictly necessary, but good for structure)
class Vehicle:
    def move(self):
        pass  # to be overridden


class Car(Vehicle):
    def move(self):
        print("Driving")


class Plane(Vehicle):
    def move(self):
        print("Flying")


class Boat(Vehicle):
    def move(self):
        print("Sailing")


# Animal classes
class Animal:
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        print("Running")


class Bird(Animal):
    def move(self):
        print("Flying")


class Fish(Animal):
    def move(self):
        print("Swimming")


# --- Demonstrate Polymorphism ---
things = [Car(), Plane(), Boat(), Dog(), Bird(), Fish()]

for thing in things:
    thing.move()  # Same method call -> different output
