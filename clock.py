sum=int(input("please enter sum seconds: "))

h = sum//3600
mo = sum-3600*h
m = mo//60
s = mo-60*m

print("Time is: ",h,":",m,":",s)