a = 1
b = 2
MAX_NUM = 4000000

def sum_fibonacci_even(max):
    a = 1
    b = 2
    if max<2:
        ans = 0
        return ans
    ans = 2
    while(True):
        c = a+b
        if c%2 == 0:
            ans += c
        if c>=max:
            return ans
        a,b = b,c

print(sum_fibonacci_even(MAX_NUM))