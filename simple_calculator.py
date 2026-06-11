"""Simple calculator CLI with history

Features:
- add, subtract, multiply, divide
- handles division by zero
- keeps in-memory session history
"""
def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
    raise ValueError("Unknown operator")


def main():
    print("Simple Calculator — enter expressions like: 2 + 2")
    history = []
    while True:
        line = input("calc> ").strip()
        if not line:
            continue
        if line.lower() in ("q", "quit", "exit"):
            break
        if line.lower() == "history":
            for i, entry in enumerate(history, 1):
                print(f"{i}: {entry}")
            continue
        try:
            parts = line.split()
            if len(parts) != 3:
                print("Enter in format: <num> <op> <num>")
                continue
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            res = calculate(a, op, b)
            out = f"{a} {op} {b} = {res}"
            print(out)
            history.append(out)
        except ZeroDivisionError:
            print("Error: division by zero")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
