# function to test prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# function to test even number
def is_even(n):
    if n % 2 == 0:
        return True
    return False
