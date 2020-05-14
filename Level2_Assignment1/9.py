class Circle:
     def __init__(self,radius):
          self.radius = radius
     def area(self):
          return 3.14*self.radius*self.radius    
     def circumference(self):
          return 2*3.14*self.radius
     
if __name__ =="__main__":
     try:
        radius = float(input("Enter the radius of circle"))
        c1 = Circle(radius)
        area = c1.area()
        print ("Area of circle is",area)
        circumference = c1.circumference()
        print ("Circumference of circle is",circumference)
     except ValueError:
         print ("Enter only numeric values")
     except Exception as e:
        print (e)
