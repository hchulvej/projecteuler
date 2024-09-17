def is_increasing(n):
    if n < 10:
        return True
    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True

def is_decreasing(n):
    if n < 10:
        return True
    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 1):
        if digits[i] < digits[i + 1]:
            return False
    return True

limit = 100

increasing_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
inc_digits = 1
no_non_bouncy_numbers = 9

def add_digit_inc(increasing_numbers):
    res = []
    for n in increasing_numbers:
        for i in range(10):
            if i >= n % 10 and is_increasing(n * 10 + i):
                res.append(n * 10 + i)
    return res

while inc_digits < limit:
    increasing_numbers = add_digit_inc(increasing_numbers)
    inc_digits += 1
    no_non_bouncy_numbers += len(increasing_numbers)
    
decreasing_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dec_digits = 1

def add_digit_dec(decreasing_numbers):
    res = []
    for n in decreasing_numbers:
        for i in range(10):
            if i <= n % 10 and is_decreasing(n * 10 + i):
                res.append(n * 10 + i)
    return res

while dec_digits < limit:
    decreasing_numbers = add_digit_dec(decreasing_numbers)
    dec_digits += 1
    no_non_bouncy_numbers += len(decreasing_numbers)

no_non_bouncy_numbers -= 9*(limit - 1)

print(no_non_bouncy_numbers)