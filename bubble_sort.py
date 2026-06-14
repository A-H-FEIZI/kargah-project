def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
user_input = input("اعداد رو وارد کن: ")
numbers = list(map(int, user_input.split()))
print(bubble_sort(numbers))