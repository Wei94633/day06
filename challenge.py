import time

def power(a,b):
    result = 1
    for i in range(b):
        result = result * a

    return result

start = time.perf_counter()
power(42, 84)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
power(42, 168)
end = time.perf_counter()
print(end - start)