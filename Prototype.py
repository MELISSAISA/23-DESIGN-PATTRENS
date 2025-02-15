class Python():   
   # Class for Python language  
   def Type(self):   
      return "Python basics and advance"  
  
   def __str__(self):   
      return "Python"  
  
  
# concrete course   
class Java():   
   #Class for Java langauge"""  
  
   def Type(self):   
      return "Java Basics and Hibernate"  
  
   def __str__(self):   
      return "Java"  
  
  
# concrete course   
class R():   
   # class for R tutorial"""  
  
   def Type(self):   
      return "R programming language classes"  
  
   def __str__(self):   
      return "R"  
  
  
# main method   
if __name__ == "__main__":   
   p = Python() # object for Python   
   j = Java() # object for java   
   r = R() # object for R  
  
   print(f'Name of Course: {r} and its type: {r.Type()}')   
   print(f'Name of Course: {j} and its type: {j.Type()}')   
   print(f'Name of Course: {p} and its type: {p.Type()}')   
