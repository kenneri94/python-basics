# circle


class Circle:
    def __init__(self, r):
        self.radius=r

        def area(self):
            return 22/7 * self.radius**2

        def perimeter(self):
            return 22/7 * self.radius*2

        def print_details(self):
            print("Radius:",self.radius)
            print("Perimeter:",self.perimeter())
            print("Area:",self.area())


c1= Circle(10)
c2= Circle(20)

c1.print_details()

print(c1.get_area())