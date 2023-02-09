# good_fib was produced using ChatGPT
def good_fib(n, cache={}):
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = good_fib(n-1, cache) + good_fib(n-2, cache)
        return cache[n]
    

