import sys
import json
import timeit

sys.setrecursionlimit(20000)

def main():
    input = json.load(open("input.json"))
    times = []
    times2 = []
    
    for arr in input:
        time = timeit.timeit(lambda:func1(arr, 0, len(arr) - 1), number=1)
        times.append(time)

    
    input2 = input = json.load(open("input.json"))
    for arr in input2:
        time = timeit.timeit(lambda:altfunc1(arr, 0, len(arr) - 1), number=1)
        times2.append(time)

    print('Timing for Pivot at first element: \n', times)
    print(input[0])
    print('Sorted =',checkAsc(input[0]))
    print('Timing for Pivot at second element: \n', times2)
    print(input2[0])
    print('Sorted =',checkAsc(input2[0]))
    

    """
    plt.title("Timing of Quicksort Algorithm")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time in Seconds")
    plt.plot(x, times, label="Original JSON")
    plt.plot(x, times2, label="Adjusted JSON")
    plt.legend(loc="best")
    plt.xticks(x)
    plt.show()
    """

def checkAsc(a):
    j = 0
    i = 1
    while i < len(a):
        if(a[j] > a[i]):
            return False
        j+=1
        i+=1
    return True

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

def altfunc2(array, start, end):
    p = array[(start + end) // 2]
    low = start - 1
    high = end + 1
    while True:
        while True:
            low += 1
            if array[low] >= p:
                break
        while True:
            high -= 1
            if array[high] <= p:
                break
        if low >= high:
            break
        array[low], array[high] = array[high], array[low]
    return high

def altfunc1(arr, low, high):
    if low < high:
        pi = altfunc2(arr, low, high)
        altfunc1(arr, low, pi)
        altfunc1(arr, pi + 1, high)

if __name__ == "__main__":
    main()