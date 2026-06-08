def sum_of_evens(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0 :
             total += number
    return total
numbers = [1, 2, 3, 4, 5, 6]
print(sum_of_evens(numbers))        