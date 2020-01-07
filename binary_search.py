"""
Binary search algorithm in Python 3.
Run time: O(log n)
"""

def binary_search(arr, target):
    high = len(arr)-1
    low = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return False


"""
With recursion
"""

def recur_binary_search(arr, target, low, high):

    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return recur_binary_search(arr, target, mid+1, high)
        else:
            return recur_binary_search(arr, target, low, mid-1)
    else:
        return False


arr = [10,21,32,43,54,65,76,87,98,109]

print(binary_search(arr,77))
print(recur_binary_search(arr,40,0,len(arr)-1))