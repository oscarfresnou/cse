class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self).__init__(name, engine_type)
        self.body_type = body_type
        self.steering_wheel = True
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car starts")

    def move_forward(self):
        self.fuel -= 1
        print("You turn forward")

    def turn_left(self):
        self.fuel -= 1
        print("You turned left")

    def turn_off(self):
        self.engine_status = False
        print("You turn off the engine")


class Corvette(Car):
    def __init__(self):
        super(Corvette, self).__init__("Corvette", "Gas", "Slim")


Julianna_Car = Corvette()
Julianna_Car.start_engine()
Julianna_Car.move_forward()
