def countdown(n):
    if n == 0:
        print("تموم شد!")
        return
    print(n)
    countdown(n - 1)

countdown(5)