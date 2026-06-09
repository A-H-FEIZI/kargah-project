def grade(number) :
    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    elif number >= 60:
        return "D"
    else:
        return "F"

print(grade(95))
print(grade(85))
print(grade(75))
print(grade(65))
print(grade(45))