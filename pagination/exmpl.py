class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        result = self.radius*2
        result = result * self.pi



        return result
    def perimeter(self):
        return 2 * self.radius * self.pi

mycircle = Circle(radius=20)
print(mycircle.radius)
