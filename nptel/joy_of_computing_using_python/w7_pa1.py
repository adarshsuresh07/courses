'''
Lower Triangular Matrix 
A Lower triangular matrix is a square matrix (where the number of rows and columns are equal)  where all the elements above the diagonal are zero.
For example, the following is an upper triangular matrix with the number of rows and columns equal to 3.

1 0 0
4 5 0
7 8 9

Write a program to convert a square matrix into a lower triangular matrix.

Input Format:   The first line of the input contains an integer number n which represents the number of rows and the number of columns.
                From the second line, take n lines input with each line containing n integer elements. Elements are separated by space.

Output format:  Print the elements of the matrix with each row in a new line and each element separated by a space.

Example 1:  Input:  3
                    1 2 3
                    4 5 6
                    7 8 9

            Output: 1 0 0
                    4 5 0
                    7 8 9

Example 2:  Input:  4
                    12 2 5 6
                    10 11 4 1
                    32 1 4 10
                    1 2 10 9

            Output: 12 0 0 0
                    10 11 0 0
                    32 1 4 0
                    1 2 10 9

Explanation:    In both the examples, elements which are above the diagonal are zero.

Solution:   

a = int(input())
m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)

for i in range(a):
    for j in range(a):
        if(i>=j):
            if(j==a-1):
                print(m[i][j], end="")
            else:
                print(m[i][j], end=" ")
        else:
            if(j==a-1):
                print(0, end="")
            else:
                print(0, end=" ")
    if(i!=a-1):
        print()
'''



n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
for i in range(n): 
    for j in range(n): 
        if (i < j and j < n):
            print(" 0", end ='')
            if j == n-1:
                print("", end ='\n')
        else: 
            if j > 0:
                print(" ", end='')
                print(a[i][j],  end="")
            else:
                print(a[i][j],  end="")