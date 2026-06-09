def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b

for op in ["+", "-", "*", "/"]:
    print(f"10 {op} 5 = {calculator(10, 5, op)}")