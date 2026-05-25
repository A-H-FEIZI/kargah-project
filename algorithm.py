numbers = [8, 6, 12, 16, 18, 15]

for j in range(len(numbers)):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)