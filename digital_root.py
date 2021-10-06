def digital_root(n):
    def add_digit(n):
        total = 0
        length = len(str(abs(n)))
        for i in range(length):
            total += n%10
            n = n//10
        return total
    while n >= 10:
        n = add_digit(n)
    return n
n = int(input())
print(digital_root(n))