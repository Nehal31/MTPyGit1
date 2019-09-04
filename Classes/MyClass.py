
class Vehicle:
    def __init__(self, model, color, wheels):
        self.model = model
        self.registration_no = None
        self.color = color
        self.wheels = wheels

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_registration(self):
        return self.registration_no

    def set_registrations(self, registration_no):
        self.registration_no = registration_no

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_wheels(self):
        return self.wheels

    def set_wheels(self, wheels):
        self.wheels = wheels


class GoodsVehicle(Vehicle):
    def __init__(self, load_cap, model, color, wheels):
        super(GoodsVehicle, self).__init__(model, color, wheels)
        self.load_cap = load_cap

    def get_capacity(self):
        return self.load_cap

    def set_capacity(self, load_cap):
        self.load_cap = load_cap


class PassengerVehicle(Vehicle):
    def __init__(self, passenger_cap, model, color, wheels):
        super(PassengerVehicle, self).__init__(model, color, wheels)
        self.passenger_cap = passenger_cap

    def get_passenger_cap(self):
        return self.passenger_cap

    def set_passenger_cap(self, passenger_cap):
        self.passenger_cap = passenger_cap


class Car(PassengerVehicle):
    pass


class Bus(PassengerVehicle):
    pass


class Trucks(GoodsVehicle):
    pass



def main():

    pass


if __name__ == '__main__':
    main()
