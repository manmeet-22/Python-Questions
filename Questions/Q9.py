import math

n=int(input("Enter the number till which to print the sequence"))
sum = 0
for i in range(1,n):
    print(pow(i,i),"/",math.factorial(i),"+ ",end="")
    sum += pow(i, i) / math.factorial(i)
i+=1
sum += pow(i, i) / math.factorial(i)
print(pow(i, i), "/", math.factorial(i))
print(sum)
