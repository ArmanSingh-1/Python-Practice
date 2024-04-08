'''
Exercise 5
The geometric sequence is given with the following formula:
an = 8*2^n-1
Calculate the sum of the first six elements of this sequence. 
Print the result to the console as shown below.
Expected result:
The sum of the first 6 elements of the sequence is: 504.0
'''
a1 = 8
a2 = 16
n = 6
r = a2 / a1
sum = a1 * ((1 - r**n) / (1 - r))
print(f'The sum of the first {n} elements of the sequence is: {sum:.1f}')