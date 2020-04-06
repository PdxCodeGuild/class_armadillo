
# colors are represented by RGB triplets
# each number goes from 0 to 255


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.colors = []
        for i in range(self.width):
            self.colors.append([])
            for j in range(self.height):
                self.colors[i].append(RGBColor(0, 0, 0))

class RGBColor:
    def __init__(self, r=0, g=0, b=0):
        self.R = RGBColor.clamp(r, 0, 255)
        self.G = RGBColor.clamp(g, 0, 255)
        self.B = RGBColor.clamp(b, 0, 255)

    def __str__(self):
        return f'({self.R},{self.G},{self.B})'

    def __add__(self, other):
        return RGBColor(self.R + other.R,
                        self.G + other.G,
                        self.B + other.B)

    def __sub__(self, other):
        return RGBColor(self.R - other.R,
                        self.G - other.G,
                        self.B - other.B)

    def __mul__(self, other):
        if type(other) is float or type(other) is int:
            return RGBColor(self.R*other, self.G*other, self.B*other)
        return RGBColor(self.R * other.R,
                        self.G * other.G,
                        self.B * other.B)

    @staticmethod
    def clamp(v, lower, upper):
        return lower if v < lower else upper if v > upper else v
        # if v < lower:
        #     return lower
        # elif v > upper:
        #     return upper
        # return v


red = RGBColor(255, 0, 0)
blue = RGBColor(0, 0, 255)
print(str(blue))





