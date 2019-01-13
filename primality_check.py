import timeit


def is_prime(value):
    return all(value % x for x in range(2, int(value ** 0.5) + 1))


def is_prime2(value):
    return any(value % x == 0 for x in range(2, int(value ** 0.5) + 1))


value = 15_485_863
print(timeit.timeit(f"is_prime({value})", number=1000, globals=globals()))
print(timeit.timeit(f"is_prime2({value})", number=1000, globals=globals()))

# all performs better
# 5.977431236
# 6.207507692
