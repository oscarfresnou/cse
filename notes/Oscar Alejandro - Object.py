class Stapler(object):
    def __init__(self, capacity, stock):
        self.capacity = capacity
        self.press_down = True
        self.stock = stock
        self.staples = 5

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

        def refill():
            self.duration_of_staples = 5
            print("You filled the stapler")

