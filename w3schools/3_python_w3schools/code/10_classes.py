# ===============Class==============================

class Person2:
  pass

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"  
  
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1.name)
p1.name="youssef"
print(p1.name)
del p1.age 
print(p1.age)     
# print(p1)   
print(p1.myfunc())