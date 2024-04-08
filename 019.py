'''
Exercise 9
Find the roots of the quadratic equation:
x^2 + 5x + 4 = 0
Print the result to the console as shown below.
Expected result:
x1 = -4.0
x2 = -1.0
'''
a = 1
b = 5
c = 4
d = b**2 - 4*a*c
x1 = (-b - d**0.5)/2*a
x2 = (-b + d**0.5)/2*a
print(f'x1 = {x1:.1f} \nx2 = {x2:.1f}')