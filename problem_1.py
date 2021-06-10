def multiples_sum(n):
    s = 0
    for i in range(3, n, 3):
        s += i
    for i in range(5, n, 5):
        s += i
    for i in range(15, n, 15):
        s -= i
    return s


print("Enter value of n")
n = int(input())
print(multiples_sum(n))
