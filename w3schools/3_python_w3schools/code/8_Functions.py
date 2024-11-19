#===================function=========================
def my_function(fname, lname):
  print(fname + " " + lname)

def my_function2(*kids):
  print("The youngest child is " + kids[1])

def my_function3(child3, child2, child1):
  print("The youngest child is " + child3)

def my_function4(**kid):
  print("His last name is " + kid["lname"])  

def my_function5(country = "Norway"):
  print("I am from " + country)

def my_function6(food):
  for x in food:
    print(x)  

def myfunction11():
  pass

#ONLY positional arguments, or ONLY keyword arguments.
def my_function7(x, /):
  print(x)
def my_function8(x):
  print(x)

#only keyword arguments,
def my_function9(*, x):
  print(x)

def my_function10(a, b, /, *, c, d):
  print(a + b + c + d)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
# =====================


my_function2("Emil", "Refsnes") 
my_function3(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 
my_function4(fname = "Tobias", lname = "Refsnes") 

my_function5("India")
my_function5()

fruits = ["apple", "banana", "cherry"]
my_function6(fruits)

my_function7(5)
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
my_function8(x = 3) 
# only keyword arguments,
my_function9(x = 3) 
# Combine Positional-Only and Keyword-Only
my_function10(5, 6, c = 7, d = 8) 


tri_recursion(6)

