# 如何完成作業
先理解老師教材中的fibonacci_lookup.py程式碼如下，在修改過後完成作業。
```python
from datetime import datetime
fib = [None]*10000
fib[0] = 0
fib[1] = 1

def fibonacci(n):
    if n < 0: raise
    if not fib[n] is None: return fib[n]
    fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib[n]

# n = 35
n = 60
startTime = datetime.now()
print(f'fibonacci({n})={fibonacci(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
```
