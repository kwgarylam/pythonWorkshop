import math
n = int(input ("n= "))
strP = input ("pattern= ")
for j in range (0, 2*n):
    if j<n:
        for i in range (0, j+1):
            print (strP," ",end="")
    else:
        for i in range (0, 2*n-j-1):
            print (strP," ",end="")
    print ("")
    
    

