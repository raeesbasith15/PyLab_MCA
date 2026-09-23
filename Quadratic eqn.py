from math import sqrt
a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: ")) 

discriminant = (b**2) - (4*a*c) 

if discriminant < 0:
	print("The equation has no real roots.")
else:
	pos = (-b + sqrt(discriminant)) / (2*a)
	neg = (-b - sqrt(discriminant)) / (2*a)

	print(f"Roots are : {pos} and {neg}")

