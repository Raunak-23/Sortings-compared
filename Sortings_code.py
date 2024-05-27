import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr, p, q):
    if p < q:
        m = partition(arr, p, q)
        quick_sort(arr, p, m-1)
        quick_sort(arr, m+1, q)

def partition(arr, p, q):
    x = arr[p]
    i = p
    for k in range(p+1, q, 1):
        if arr[k] < x:
            i += 1
            arr[k], arr[i] = arr[i], arr[k]
    arr[i], arr[p] = arr[p], arr[i]
    return i

arr=eval(input("Enter a List of numbers"))
arr1=arr

start_time = time.perf_counter()
bubble_sort(arr)
end_time = time.perf_counter()
print(arr)
print("Bubble sort execution time = {:.6f} s".format(end_time-start_time))
start_time=time.perf_counter()
quick_sort(arr1,0,len(arr1)-1)
end_time = time.perf_counter()
print(arr1)
print("Quick sort execution time = {:.6f} s".format(end_time-start_time))
