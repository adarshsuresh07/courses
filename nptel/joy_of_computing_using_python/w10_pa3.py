'''
Calculate 

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Input Format:   A sequence of values for D with each value separated by a comma.

Output Format:  Print the sequence of Q values with each value separated by a comma.

Example:    Input:  100,150,180
            Output: 18,22,24

Solution:   

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))

'''


from math import sqrt
output_list = []
input_list = list(map(int, input().split(',')))
C = 50
H = 30
for D in input_list:
    Q = int(round(sqrt( (2*C*D) / H)))
    Q = str(Q)
    output_list.append(Q)
print(','.join(output_list), end='')