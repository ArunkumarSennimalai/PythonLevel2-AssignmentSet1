class StringOperations:
     def __init__(self,data):
          self.data = data
     
     def __gt__(self,str2):
          if len(self.data)>len(str2.data):
               return self.data
          return str2.data
               
if __name__ =="__main__":
    try:
        str1 = StringOperations("ABCDE")
        str2 = StringOperations("XYZ")
        print (str1>str2)
    except Exception as e:
        print (e)
