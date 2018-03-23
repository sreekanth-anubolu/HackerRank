"""
Output
*
* *
* * *
* * * *
* * * * *
"""
for i in range(6):
    print("* " * i)

# Or

'''for i in range(6):
    for j in range(i):
        print("* ", end="")
    print()'''


print()
print("======================")
print()

"""
Output
* * * * *
* * * * 
* * * 
* * 
* 
"""
for i in range(5, 0, -1):
    print("* " * i)

'''for i in range(5, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()'''


print()
print("======================")
print()

"""
Output
        *
      * *
    * * * 
  * * * *
* * * * *
"""
index = 1
for i in range(5, 0, -1):
    print("  " * (i-1) + "* " * index)
    index += 1

print()
print("======================")
print()

"""
Output
* * * * *
  * * * * 
    * * * 
      * * 
        * 
"""

start = 5
for i in range(start, 0, -1):
    print("  " * (start - i) + "* " * i)

print()
print("======================")
print()


"""
Output
    *
   * *
  * * *
 * * * *
* * * * *
"""

_range = 5
_index = 0
for i in range(_range + 1):
    _spaces = _range - _index
    print(" " * _spaces, end="")
    print("* " * i)
    _index += 1

print()
print("======================")
print()

"""
Output
* * * * *
 * * * *
  * * * 
   * *
    *
"""


_range = 5
_index = 0
for i in range(_range, 0, -1):
    print(" " * _index, end="")
    print("* " * i)
    _index += 1

print()
print("======================")
print()


"""
Output:
* * * * * 
  * * * * * 
    * * * * * 
      * * * * * 
        * * * * * 
"""

start = 5
for i in range(start, 0, -1):
    print("  " * (start - i) + "* " * start)


print()
print("======================")
print()


"""
Output
* * * * * 
* * * * *
* * * * * 
* * * * * 
* * * * *
"""
_range = 5
for i in range(_range):
    print("* " * _range)

print()
print("======================")
print()