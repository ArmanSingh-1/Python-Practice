'''
Exercise 12
Calculate the standard deviation (biased) of the following set of data:
10, 11, 9.
Print the result to the console as shown below.
Expected result:
The standard deviation: 0.82
'''
x1,x2,x3 = 10,11,9
mean = (x1 + x2 + x3)/3
var = ((mean - x1)**2 + (mean - x2)**2 + (mean - x3)**2)/3
std = var **0.5
print(f'The standard deviation: {std:.2f}')