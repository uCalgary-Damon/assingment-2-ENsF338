import timeit
import matplotlib.pyplot as plt

def bad_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return bad_fib(n-1) + bad_fib(n-2)
    
# good_fib was partially produced using ChatGPT
def good_fib(n, cache={}):
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = good_fib(n-1, cache) + good_fib(n-2, cache)
        return cache[n]
    
def main():

    bad_fib_list = []
    good_fib_list = []
    n = []

    #Gets timing for fib(0) to fib(35)
    for i in range(36):
        bad_fib_list.append(timeit.timeit(lambda: bad_fib(i), number=1))
        good_fib_list.append(timeit.timeit(lambda: good_fib(i), number=1))
        n.append(i)
    
    #Plots timing data
    plt.xlabel("nth Fibonacci Number")
    plt.ylabel("Seconds (s)")
    plt.title("Time to Calculate the nth Fibonacci Number")
    plt.scatter(n, bad_fib_list, label="Bad Fib", color="r")
    plt.scatter(n, good_fib_list, label="Good Fib", color="g")
    plt.figlegend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    main()