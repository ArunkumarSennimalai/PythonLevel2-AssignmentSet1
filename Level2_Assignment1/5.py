class Squareroot:
     def sqrt(self,tempval):
         return tempval**0.5

class Addition:
     def addition(self,tempval1,tempval2,*args):
         sumval = tempval1 + tempval2
         for value in args:
             sumval += value
         return sumval
 
class Subtraction:
     def subtraction(self,tempval1,tempval2,*args):
         subval = tempval1 - tempval2
         for value in args:
             subval -= value
         return subval
class Multiplication:
     def multiply(self,tempval1,tempval2,*args):
         mulval = tempval1 * tempval2
         for value in args:
             mulval *= value
         return mulval
class Division:
     def divide(self,tempval1,tempval2):
         return tempval1/tempval2

class Mathnew(Squareroot,Addition,Subtraction,Multiplication,Division):
     def sqrt(self,tempval):
          return super().sqrt(tempval)
     def addition(self,tempval1,tempval2,*args):
          return super().addition(tempval1,tempval2,*args)
     def subtraction(self,tempval1,tempval2,*args):
          return super().subtraction(tempval1,tempval2,*args)
     def multiply(self,tempval1,tempval2,*args):
          return super().multiply(tempval1,tempval2,*args)

if __name__ =="__main__":
    try:
        obj1 = Mathnew()
        print (obj1.addition(1,2,3,4,5))
        print (obj1.subtraction(1,2,3,4))
        print (obj1.multiply(1,2,3,4,5,6))
        print (obj1.divide(1,2))
        print (obj1.sqrt(8))
    except ArithmeticError:
        print ("Arithmetic Exception Occurred")
    except Exception as e:
        print(e)
