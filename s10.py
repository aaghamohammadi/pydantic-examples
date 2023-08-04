from pydantic import validate_call


@validate_call(validate_return=True)
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(is_prime(2))
print(is_prime(-1))
print(is_prime(5))
print(is_prime(12))
