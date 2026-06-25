def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

### Testes na branch 'tests'
def average(values):
    return sum(values) / len(values)
