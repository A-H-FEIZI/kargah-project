numbers = [8, 6, 12, 16, 18, 15]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)