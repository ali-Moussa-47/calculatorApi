def calculate(a:int , b:int, op: str):
    if op == 'add':
        return a+b
    if op == 'sub':
        return a-b
    if op == 'mul':
        return a*b
    if op == 'div':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a//b
    else:
        raise ValueError("Operation not supported")
