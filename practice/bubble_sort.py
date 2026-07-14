def bubble_sort(numbers):
    for i in range(len(numbers)):
        swapped = False
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if not swapped:    
            break               
    return numbers
user_input = input("اعداد رو با فاصله وارد کن: ")
numbers = list(map(int, user_input.split()))
print(bubble_sort(numbers))