# 1. is_prime(n) function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test is_prime function
print(is_prime(4))   # False
print(is_prime(7))   # True


# 2. digit_sum(k) function
def digit_sum(k):
    return sum(int(d) for d in str(k))

# Test digit_sum function
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7


# 3. Power of two up to N
def print_powers_of_two(n):
    power = 1
    result = []
    while (power := power * 2) <= n:
        result.append(power)
    print(" ".join(map(str, result)))

# Test power of two function
print_powers_of_two(10)  # 2 4 8
