#!/bin/env python3

import os

def fibonacci_recursive(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fibonacci_dp(n-1) + fibonacci_dp(n-2)
    memo[n]=f

def main():
    for n in range(1,10):
        print(fibonacci_dp(n))

if __name__ == "__main__":

    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    