#!/bin/python3
"""
    Problem Statement:
        Print all  integers in  in reverse order as a single line of space-separated integers.

        Sample Input

            4
            1 4 3 2

        Sample Output

            2 3 4 1

"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

string = " ".join(str(x) for x in arr[::-1])

print(string)

'''
Instantiated StartupServiceInstantiated App Module
# Several Other Pythonic Solutions
for x in reversed(arr):
    print(x, end=" ")

# Several Other Pythonic Solutions
for x in arr[::-1]:
    print(x, end=" ")
    
In both of the above examples, there is added Space Complexity, because we are creating new arrays by reversing an existing array.

'''



