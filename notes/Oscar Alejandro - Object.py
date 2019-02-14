class LoveGun(object):
    def __init__(self, capacity, distance, stock):
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.stock = stock
        self.bullets_that_spread = 5

    def shoot(self, ammo):
        if self.trigger:
            if self.bullets_that_spread <= 0:
                print("There's no pressure")
            elif self.bullets_that_spread< ammo:
                print("You run out of pressure after firing for %s seconds", self.bullets_that_spread)
                self.bullets_that_spread = 0
            else:
                print("You shoot for %s seconds"
                      % ammo)
                self.bullets_that_spread -= ammo

        def load_it_up(self):
            self.duration_of_pressure = 5
            print("You pump the tank up to full pressure")


my_love_gun = LoveGun(99999999999999999999999999999999999
                        , 999999999999999999999999999999999999999999999999999999999999999999999999999999999999, True)
