# A local variable in a function is either a parameter or a variable which appears on the left
# hand side (LHS) of an assignment statement in the function. A variable in a function is global
# if it is not local, but if you want to assign something to a global variable, g, in a function,
# then you will need the statement global g. Without the global g statement, assignment, like,
# g = 5, would make g local. You shouldn't use global variables very often when writing
# functions, since global variables reduce readability. Occasionally they are useful, such as
# when you would like to count how often a function is called. Define a global variable,
# countcalls, and increment it inside the power(x, n) function that you wrote for Q4, so that it
# counts the number of times the power function is called. Show that it produces the
# expected number of calls for power(2, 10) and power(5, 10) and power(5, 0), each
# separately.

def power(x,n):
  global countcalls
  countcalls=countcalls+1
  if n==0:
    return 1
  else:
    return x*power(x,n-1)
  
countcalls=0
print("2^10=",power(2,10))
print("Number of times the power function is called=",countcalls)
countcalls=0
print("5^10=",power(5, 10))
print("Number of times the power function is called=",countcalls)
countcalls=0
print("5^0=",power(5,0))
print("Number of times the power function is called=",countcalls)

