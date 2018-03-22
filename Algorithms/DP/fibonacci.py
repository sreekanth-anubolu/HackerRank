

def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a+b, a
    return a

# Solves the problem,but very soon we will run into issue,func becomes slow & slow as the input value is larger & larger
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n - 2)


# Improved performance with Memoization
fibonacci_cache = {}
def fib_cache(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 0 or n == 1:
        fibonacci_cache[n] = n
        return n
    val = fib_cache(n-1) + fib_cache(n - 2)
    fibonacci_cache[n] = val
    return val


from functools import lru_cache

# lru cache meaning - l - Least, r - Recently, u - Used cache, max size is 128 by default, which means
# it can store up to 128 most recently used values, we can increase for it to store more.

# Improved performance with Memoization
@lru_cache(maxsize=1000)
def lru_fib_cache(n):
    if n == 0 or n == 1:
        return n
    return fib_cache(n-1) + fib_cache(n - 2)


robust_fibonacci_cache = {}
# Improved performance, but it fails when there are non positive numbers or non integer numbers
def robust_fib_cache(n):

    if type(n) != int:
        raise TypeError("N Should be Integer")
    if n < 0:
        raise ValueError("N Should be a Positive Number")

    if n in robust_fibonacci_cache:
        return robust_fibonacci_cache[n]

    if n == 0 or n == 1:
        robust_fibonacci_cache[n] = n
        return n
    val = robust_fib_cache(n-1) + robust_fib_cache(n - 2)
    robust_fibonacci_cache[n] = val
    return val



# Improved performance with Memoization and print all the fibonacci sequence
fibonacci_cache = {}
def fib_cache_print(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 0 or n == 1:
        fibonacci_cache[n] = n
        return n
    val = fib_cache(n-1) + fib_cache(n - 2)
    fibonacci_cache[n] = val
    return val

for i in range(100000):
    # print("Fibonacci sequence of ", i, "is",  fib(i)) # performace will become slow once it reaches to 30 and more
    print("Fibonacci sequence after implementing cache for ", i, "is", fib_cache(i)) # Impressively Fast
    # print("Fibonacci sequence after implementing lru cache for ", i, "is", lru_fib_cache(i)) # Impressively Fast
    # print("Robust Fibonacci sequence after implementing cache for ", i, "is", robust_fib_cache(i)) # Impressively Fast
    # print("Fibonacci sequence after implementing cache for ", i, "is", fib_loop(i)) # Impressively Fast

