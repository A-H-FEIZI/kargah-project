numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == target:
        print(f"پیدا شد! خونه شماره {mid}")
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1