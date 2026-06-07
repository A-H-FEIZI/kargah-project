def is_positive(n):
    if n > 0:
        return"مثبت"
    elif n < 0:
        return"منفی"
    else:
        return"صفر"

print(is_positive(5))
print(is_positive(-3))
print(is_positive(0))