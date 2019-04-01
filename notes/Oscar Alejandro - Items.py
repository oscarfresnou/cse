class Item(object):
    def __init__(self, name):
        self.name = name


class Vehicle(Item):
    def __init__(self, name):
        super(Vehicle, self).__init__(name)
        self.engine = True
        self.steering_wheel = True


class Boat(Vehicle):
    def __init__(self, name):
        super(Boat, self).__init__(name)
