def multiplay_list(numbers):
    total=1
    for number in numbers:
        total *= number
    return total

numbers = [6, 4, 8, 5, 9, 1]
print(multiplay_list(numbers))