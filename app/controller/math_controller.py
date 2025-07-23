def power(base, exponent):
    try:
        base = float(base)
        exponent = float(exponent)
        import math
        result = math.pow(base, exponent)
        if not math.isfinite(result):
            return None, 'Rezultatul este prea mare sau invalid!'
        formatted = f"{base}^{exponent} = {result if result % 1 else int(result):,}"
        return formatted, None
    except Exception:
        return None, 'Eroare la calculul puterii!'
 
def fibonacci(n):
    try:
        n = int(n)
        if n < 0:
            return None, None, 'Număr invalid!'
        if n > 1000:
            return None, None, 'Numărul este prea mare! (max 1000)'
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        sequence = []
        x, y = 0, 1
        for i in range(min(n+1, 20)):
            sequence.append(x)
            x, y = y, x + y
        return f"Fibonacci({n}) = {a:,}", sequence, None
    except Exception:
        return None, None, 'Eroare la calculul Fibonacci!'

def factorial(n):
    try:
        n = int(n)
        if n < 0:
            return None, 'Număr invalid!'
        if n > 170:
            return None, 'Numărul este prea mare! (max 170)'
        import math
        result = math.factorial(n)
        formatted = f"{n}! = {result:,}"
        return formatted, None
    except Exception:
        return None, 'Eroare la calculul factorialului!'