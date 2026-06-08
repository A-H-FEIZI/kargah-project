def flatten_list(arr):
    result = []
    for sublist in arr:
        for number in sublist:
            result.append(number)
    return result
    
print(flatten_list([[1,2],[3,4],[5,6]]))
