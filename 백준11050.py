a, b = map(int, input().split())

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(factorial(a)//(factorial(a-b)*factorial(b)))
