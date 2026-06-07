def reverse_list (numbers):
    result = []
    for number in reversed (numbers):
        result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6]
print (reverse_list(numbers))