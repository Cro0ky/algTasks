class Rectagle:
    def __init__(self, wight, height):
        self.height = height
        self.wight = wight

    def S(self):
        print(self.wight * self.height)

    def P(self):
        print((self.wight + self.height) * 2)

rec1 = Rectagle(5, 6)
rec1.S()
rec1.P()