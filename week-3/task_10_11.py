import math


class Color:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        self._red = red
        self._green = green
        self._blue = blue

    def __lt__(self, other):
        return self.red < other.red and self.green < other.green and self.blue < other.blue

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __str__(self):
        return f'“red”: {self.red}, “green”: {self.green}, “blue”: {self.blue}'

    def add_red(self, value):
        self.red += value

    def add_green(self, value):
        self.green += value

    def add_blue(self, value):
        self.blue += value

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        if 0 <= value <= 255:
            self._red = value

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value):
        if 0 <= value <= 255:
            self._green = value

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, value):
        if 0 <= value <= 255:
            self._blue = value

c = Color()
c.add_red(-10)
print(c.red)

c1 = Color()
c2 = Color(1, 1, 1)
print(c1 < c2)
print(c1 == c2)
print(c2)


class AlphaColor(Color):
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, alpha: float = 0):
        super().__init__(red, green, blue, )
        self._alpha = alpha

    def __str__(self):
        return super().__str__() + f', “alpha”:{self.alpha}'

    def update_color_by_alpha(self):
        self.red -= math.floor(self.red * self.alpha)
        self.green -= math.floor(self.green * self.alpha)
        self.blue -= math.floor(self.blue * self.alpha)

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if 0 <= value <= 1:
            self._alpha = value


a1 = AlphaColor(255, 255, 255, 0.9)
a2 = AlphaColor(100, 100, 100, 0.2)
print(a1 > a2)
print(a1, '\n' + str(a2))
a1.update_color_by_alpha()
print(a1)
print(a1 > a2)