# class
class Vehicle:
    # constructor method
    def __init__(self, make, model):
        self._make = make
        self._model = model

    # instance method
    def moves(self):
        print("Moves along...")

    # getter and setter methods
    # def get_make(self):
    #     return self.make

    # def set_make(self, make):
    #     self.make = make

    # def get_model(self):
    #     return self.model

    # def set_model(self, model):
    #     self.model = model
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value


# creating an instance of the Vehicle class
my_car = Vehicle("Toyota", "Camry")
my_car1 = Vehicle("Tesla", "Model S")
my_car2 = Vehicle("Ford", "F-150")

# calling the instance method
my_car.moves()

# print(f"Make: {my_car.make}, Model: {my_car.model}")
# print(f"Make: {my_car1.make}, Model: {my_car1.model}")
# print(f"Make: {my_car2.make}, Model: {my_car2.model}")

# print(f"Make: {my_car.get_make()}, Model: {my_car.get_model()}")

# my_car.set_make("Honda")
# my_car.set_model("Civic")

# print(f"Make: {my_car.get_make()}, Model: {my_car.get_model()}")

print(f"Make: {my_car.make}, Model: {my_car.model}")

my_car.make = "Honda"
my_car.model = "Civic"

print(f"Make: {my_car.make}, Model: {my_car.model}")


class Airplane(Vehicle):
    def moves(self):
        print("Flies through the air...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along the road...")


class GolfCart(Vehicle):
    pass


golfcart = GolfCart("Club Car", "Precedent")
golfcart.moves()
