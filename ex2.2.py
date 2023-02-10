import sys
import json
import timeit
from matplotlib import pyplot as plt

sys.setrecursionlimit(20000)

def main():
    input = json.load(open("input.json"))
    times = []
    
    for arr in input:
        time = timeit.timeit(lambda:func1(arr, 0, len(arr) - 1), number=1)
        times.append(time)

    x = [len(arr) for arr in input]
    
    plt.title("Timing of Quicksort Algorithm")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time in Seconds")
    plt.plot(x, times)
    plt.xticks(x)
    plt.show()

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

if __name__ == "__main__":
    main()