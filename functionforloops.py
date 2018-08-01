def add(x,y):
    return x+y

def multiply(x,y):
    result=0
    for i in range (x):
       result = add(result,y)
    return result

def power (x,y):
    result=1
    for i in range(y):
        result = multiply(result,x)
    return result

def factorial(x):
    result=1
    for i in range (1,x+1):
        result = multiply (result,i)
    return result    

def fibonacci(n):
    fibo_list = [0,1,1]
    if n < 4:
       return fibo_list[n-1]
    else: 
       for i in range (3,n):
           fibo_list.append(add(fibo_list[i-2], fibo_list[i-1]))
       return(fibo_list[n-1])

print "Add - " ,add(5,6) 
print "Multiply - ", multiply(8,6)
print "Power - ", power(3,4)
print "Factorial - ", factorial(4)
print "Fibonacci - ", fibonacci(8)
