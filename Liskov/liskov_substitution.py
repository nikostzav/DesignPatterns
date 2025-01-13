
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move method")


class Car(Vehicle):
    def __init__(self, fuel):
        self.fuel = fuel

    def move(self):
        if self.fuel > 0:
            print("The car is driving!")
            self.fuel -= 1
        else:
            print("The car is out of fuel and cannot move.")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling forward!")


class VehicleController:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)

    def move_all_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.move()


if __name__ == "__main__":
  
    car = Car(fuel=2)
    bicycle = Bicycle()

  
    controller = VehicleController()

 
    controller.add_vehicle(car)
    controller.add_vehicle(bicycle)


    print("Moving all vehicles:")
    controller.move_all_vehicles()
    controller.move_all_vehicles()  
    controller.move_all_vehicles()
