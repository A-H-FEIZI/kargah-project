def second_largest(number):
    largest = max(number)
    number.remove(largest)
    return max(number)

print(second_largest([3, 5, 6, 8, 2]))
