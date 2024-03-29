'''
Cab and walk 
Arun is working in an office which is N blocks away from his house. He wants to minimize the time it takes him to go from his house to the office.
He can either take the office cab or he can walk to the office.
Arun's velocity is V1 m/s when he is walking. The cab moves with velocity V2 m/s but whenever he calls for the cab, it always starts from the office, covers N blocks, collects Arun and goes back to the office.
The cab crosses a total distance of N meters when going from office to Arun's house and vice versa, whereas Arun covers a distance of (2–√∗N) while walking.
Help Arun to find whether he should walk or take a cab to minimize the time.

Input Format:   A single line containing three integer numbers N, V1, and V2 separated by a space.

Output Format:  Print 'Walk' or 'Cab' accordingly

Constraints:    1<=V1, V2 <=100, 1<=N<=200

Example-1:  Input:  5 10 15
            Output: Cab

Example-2:  Input:  2 10 14
            Output:
            Walk

Solution:   

n,v1,v2 = input().split()
n = int(n)
v1 = int(v1)
v2 = int(v2)

st_d = pow(2,1/2)*n
st_t = st_d/v1

el_d = 2*n
el_t = el_d/v2

if(st_t<el_t):
    print("Walk")
else:
    print("Cab")
'''

import math  
n, v1, v2 = [int(x) for x in input().split()]
cab = (2*n)/v2
walk = (math.sqrt(2)*n)/v1
if walk < cab:
    print("Walk", end = "")
else:
    print("Cab", end = "")