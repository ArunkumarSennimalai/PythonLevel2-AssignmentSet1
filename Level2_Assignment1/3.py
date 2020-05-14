class Mymath:
     def sqrt(self,tempval):
         return tempval**0.5
     def addition(self,tempval1,tempval2,*args):
         sumval = tempval1 + tempval2
         for value in args:
             sumval += value
         return sumval
     def subtraction(self,tempval1,tempval2,*args):
         subval = tempval1 - tempval2
         for value in args:
             subval -= value
         return subval
     def multiply(self,tempval1,tempval2,*args):
         mulval = tempval1 * tempval2
         for value in args:
             mulval *= value
         return mulval
     def divide(self,tempval1,tempval2):
         return tempval1/tempval2

if __name__ =="__main__":
    try:
        obj1 = Mymath()
        print (obj1.addition(1,2,3,4,5))
        print (obj1.subtraction(1,2,3,4))
        print (obj1.multiply(1,2,3,4,5,6))
        print (obj1.divide(1,2))
        print (obj1.sqrt(4))
        
    except Exception as e:
        print (e)

