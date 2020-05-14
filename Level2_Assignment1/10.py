class First:
     def method1(self):
          print ("First")
class Second(First):
     def method1(self):
          print ("Second")
class Third(First):
     def method1(self):
          print ("Third")
class Fourth(Second,Third):
     def method1(self):
          print ("Fourth")
if __name__ =="__main__":
     try:
       Fourth().method1()
       print (Fourth.mro())
     except Exception as e:
        print (e)
