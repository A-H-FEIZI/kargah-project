import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_dp(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

start = time.time()
print(fib(35))
print(f"بدون DP: {time.time() - start:.4f} ثانیه")

start = time.time()
print(fib_dp(35))
print(f"با DP: {time.time() - start:.4f} ثانیه")