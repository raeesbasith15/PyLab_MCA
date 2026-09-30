lim = int(input("Enter the Limit : "))
print(f"Fibonacci series upto {lim} : ")
a, b = 0, 1
print(a, b, end = " ")
for i in range(2, lim):
    c = a + b
    print(c, end=" ")
    a = b 
    b = c 

