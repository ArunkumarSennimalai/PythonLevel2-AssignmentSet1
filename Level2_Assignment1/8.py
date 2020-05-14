class Circle:
     def area(self,radius):
          return 3.14*radius*radius    
     def circumference(self,radius):
          return 2*3.14*radius
     
if __name__ =="__main__":
     try:
        radius = float(input("Enter the radius of circle"))
        c1 = Circle()
        area = c1.area(radius)
        print ("Area of circle is",area)
        circumference = c1.circumference(radius)
        print ("Circumference of circle is",circumference)
     except ValueError:
         print ("Enter only numeric values")
     except Exception as e:
        print (e)
