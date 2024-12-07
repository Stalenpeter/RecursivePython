def openRussianDoll(doll):
    print(doll, "more dolls to open")
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)
        

#openRussianDoll(2)  

def firstMethod():
    secondMethod()
    print("Im the first method")

def secondMethod():
    thirdMethod()
    print("I m the second method")

def thirdMethod():
    fourthMethod()
    print("I m the third method")

def fourthMethod():
    print("I m the forth method")

#firstMethod()

def recursiveMethod(n):
    if n < 1 :
        print("n is less than 1 ")
    else:
        recursiveMethod(n-1)
        print(n)

#recursiveMethod(5)

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(-4))


#Fibonacci Numbers 

def fibonacci(n):
    if n in [1,0]:
        return 1
    else:
        fibonacci(n-1) + fibonacci(n-1)


print(fibonacci(10))