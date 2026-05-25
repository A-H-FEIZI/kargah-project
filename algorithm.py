numbers = [6, 8, 12, 15, 16, 18]
target = 85
found = false
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"پیدا شد! خونه شماره {i}")
        found = true
        if not found:
    print("پیدا نشد!")