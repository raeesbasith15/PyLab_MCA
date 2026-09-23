a = 2
b = 5 

print("Before swapping")
print(f"a : {a} & b : {b}")

a, b = b, a 

print("Before swapping")
print(f"a : {a} & b : {b}")

c = 7 
d = 9

print("Before swapping")
print(f"c : {c} & d : {d}")

temp = c 
c = d
d = temp 

print("After swapping")
print(f"c : {c} & d : {d}") 

x, y = 4, 8

print("Before swapping")
print(f"x : {x} & y : {y}")

x = x + y 
y = x - y 
x = x - y 

print("After swapping")
print(f"x : {x} & y : {y}")
