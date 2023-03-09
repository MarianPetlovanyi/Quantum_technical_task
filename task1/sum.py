import time
def my_sum(N):
    return int(N*(2+N-1)/2)


if __name__ == '__main__':
    my_array = [1, 3, 10, 10**25]
    for num in my_array:
        start = time.time()
        result = my_sum(num)
        end = time.time()
        print(f"N = {num}, sum = {result}, time = {end-start}")
