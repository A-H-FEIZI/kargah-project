def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = []
    right = []
    
    for num in arr[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [8, 3, 5, 1, 9, 2, 7, 4]
print(quick_sort(numbers))