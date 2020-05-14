class Mymath:
     
     def __init__(self,tempval1=10,tempval2=2,*args):
          self.tempval1 = tempval1
          self.tempval2 = tempval2
          self.args = args
     def sqrt(self):
         return self.tempval1**0.5
     def addition(self):
         sumval = self.tempval1 + self.tempval2
         for value in self.args:
             sumval += value
         return sumval
     def subtraction(self):
         subval = self.tempval1 - self.tempval2
         for value in self.args:
             subval -= value
         return subval
     def multiply(self,):
         mulval = self.tempval1 * self.tempval2
         for value in self.args:
             mulval *= value
         return mulval
     def divide(self):
         return self.tempval1/self.tempval2

if __name__ =="__main__":
    try:
        obj1 = Mymath()
        print (obj1.addition())
        print (obj1.subtraction())
        print (obj1.multiply())
        print (obj1.divide())
        print (obj1.sqrt())
        print ("\n")
        
        obj1 = Mymath(12,4,3,5)
        print (obj1.addition())
        print (obj1.subtraction())
        print (obj1.multiply())
        print (obj1.divide())
        print (obj1.sqrt())
        
    except Exception as e:
        print (e)

