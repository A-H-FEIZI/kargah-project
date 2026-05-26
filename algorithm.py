numbers = [1, 2, 3, 2, 4, 3, 5]
seen = []

for number in numbers:
    if number in seen:
        print(number)
    else:
        seen.append(number)