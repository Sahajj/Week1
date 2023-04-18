def binary_search(arr, x):
    """
    Binary search algorithm to search for an element x in a sorted list arr.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1   # x not found in arr

# Example usage
arr = [1, 3, 5, 7, 9]
x = 7
index = binary_search(arr, x)
if index != -1:
    print(f"{x} found at index {index} in {arr}")
else:
    print(f"{x} not found in {arr}")
