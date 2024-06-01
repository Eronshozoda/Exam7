class Circle:
    PI = 3.14 

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        
        return 2 * Circle.PI * self.radius * self.radius

    def get_diameter(self):
   
        return 2 * self.radius

    def get_circumference(self):
  
        return 2 * Circle.PI * self.radius

    def get_radius(self):
        
        return self.radius

circle = Circle(5)
print("Masohat = ", circle.get_area())
print("Diametr = ", circle.get_diameter())
print("Darozi = ", circle.get_circumference())
print("Radius = ", circle.get_radius())
