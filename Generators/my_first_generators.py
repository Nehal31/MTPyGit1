import memory_profiler as profile


def my_gen(n):
    while n:
        yield n
        n = n - 1

a = my_gen(5)
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))







