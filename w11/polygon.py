#from polygon import Polygon
#from triangle import Triangle

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)


class Rectangle(Polygon):
  def __init__(self):
        Polygon.__init__(self,2)
    
  def findArea(self):
        a, b = self.sides
        # calculate the semi-perimeter
        area = a*b
        print('The area of the rectangle is %0.2f' %area)

class Square(Polygon):
  def __init__(self):
        Polygon.__init__(self,1)
    
  def findArea(self):
        (a,) = self.sides
        area = a**2
        #area = a*a
        print('The area of the square is %0.2f' %area)
      
t = Square()
t.inputSides()

t.dispSides()
t.findArea()