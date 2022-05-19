n= int(input("please enter a positive number: "))

def fib(n):
    a = 0
    b = 1
    if n==0:
        return a

    elif n==1:
        return b

    elif n>1:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
    
    else:
        print("Number is negative.")

print("Fibonacci is: ",fib(n))
                    
    