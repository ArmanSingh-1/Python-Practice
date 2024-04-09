'''
Exercise 11
An infinite geometric sequence is given with the following formula:
1,1/2,1/4,1/8,...
Calculate the sum of this sequence. Print the result to the console as shown below.
Expected result:
The sum of the sequence: 2.0
'''
a1 = 1
a2 = 0.5
r = a2/a1
sum = a1/(1-r)
print(f'The sum of the sequence: {sum}')