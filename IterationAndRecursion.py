## Andrew Nally
## CIS 261 - OOP1
## LAB: Iteration and Resursion 
## 10/04/2023

def iteration(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
print("Factorial results using an iterative function:")
numbers = [0, 5, 10, 25, 50, 100]
for num in numbers: 
#calculates and prints iterative factorials for each number
    print(f"{num}! = {iteration(num)}")
    
def recursive(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * recursive(n - 1)

print("Factorial results using a recursive function:")
numbers = [0, 5, 10, 25, 50, 100]
for num in numbers: 
#calculates and prints recursive factorials for each number
    print(f"{num}! = {recursive(num)}")
