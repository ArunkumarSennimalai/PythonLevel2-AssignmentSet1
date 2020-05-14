import re

'''def extractEmail(tempstr1):
     return re.search("[\w.]+@+[\w]+.com",tempstr1).group()
def extractDomainName(tempstr1):
     return re.search("@+[\w.]+",tempstr1).group()
def extractTime(tempstr1):
    return re.search("\d{2}:\d{2}:\d{2}",tempstr1).group()'''

class FilterString:
     def extractEmail(self,tempstr1):
          return re.findall("[\w.]+@+[\w]+.com",tempstr1)
     def extractDomainName(self,tempstr1):
         list1=[]
         for email in self.extractEmail(tempstr1):
             list1 += re.findall("@+[\w.]+",email)
         return list1
     def extractTime(self,tempstr1):
         return re.findall("\d{2}:\d{2}:\d{2}",tempstr1)


def printResult(result):
        for data in result:
             print (data)
        print()

if __name__ =="__main__":
    try:
          str1 = "From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016"
          str2 = "From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016 From def.mno@stuv.com Tue Dec 30 12:12:12 2016"

          obj1 = FilterString()
          printResult(obj1.extractEmail(str1))
          printResult(obj1.extractDomainName(str1))
          printResult(obj1.extractTime(str1))
          print("\n")
          
          printResult(obj1.extractEmail(str2))
          printResult(obj1.extractDomainName(str2))
          printResult(obj1.extractTime(str2))

        
    except Exception as e:
        print (e)

