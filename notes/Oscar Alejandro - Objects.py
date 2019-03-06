class Laptop(object):
    def __init__(self, mouse, keys, power_off, sound_high_low):
        self.battery = 100
        self.charger = True
        self.mouse = mouse
        self.key_board = keys
        self.power_button = power_off
        self.volume_button = sound_high_low
        self.screen = True
        self.desktop = True
        self.computer_uses = False

    def laptop_used(self):
         if self.computer_uses:
             if self.battery <=0:
                print("Computer is shutting down...")
             elif self.battery < 100
                print("You run out of battery after %s uses" % computer_uses)



class Stapler(object):
    def __init__(self, capacity, stock):
            self.capacity = capacity
            self.press_down = True
            self.stock = stock
            self.staples = 5
            self.refill = True

    def shoot(self, staples_left):
                   if self.press_down:
                        if self.staples <= 0:
                            print("There's no staples")
                        elif self.staples < staples_left:
                            print("You run out of staples after using #s staples", self.staples)
                            self.staples = 0
                        else:
                            print("You used the stapler for #s staples" % staples_left)
                            self.staples -= staples_left

    def refill(self):
            self.duration_of_staples = 5
            print("You filled the stapler")