class MatrixOperations:
     def __init__(self,tempmatrix):
          self.matrixValue = tempmatrix
     
     def __add__(self,temp2):
             resultMatrix = MatrixOperations([ [0 for column in range(2)] for row in range(2)]) 
             for row in range(len(self.matrixValue)):
                 for column in range(len(self.matrixValue[row])):
                      resultMatrix.matrixValue[row][column] = self.matrixValue[row][column]+temp2.matrixValue[row][column]
             return resultMatrix

     def printmatrix(self):
          for row in self.matrixValue:
               for value in row:
                    print (value ,"\t",end=" ")
               print ()
if __name__ =="__main__":
    try:
        matrix1 = MatrixOperations([[4,5],[5,6]])
        matrix2 = MatrixOperations([[8,9],[3,4]])
        
        resultMatrix = matrix1 + matrix2       
        resultMatrix.printmatrix()
        
    except ArithmeticError:
        print ("Arithmetic Exception Occurred")
    except Exception as e:
        print (e)
