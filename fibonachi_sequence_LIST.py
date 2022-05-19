n= int(input("please enter a positive number: "))
list=[]
a = 0
b = 1
count = 0
if n==0:
    print(a)

elif n==1:
    print(b)

elif n>1:
    print("Fibonacci sequence: ")
    while count<n:
        list.append(a)
        c = a + b
        a = b
        b = c
        count+=1
    
    print(list)

else:
    print("Number is negative.")
