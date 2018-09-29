# _*_ coding: utf-8 _*_


def sorts(arr):
    yield (arr, [])
    n = len(arr)
    for i in range(n, 1, -1):
        for j in range(0, i - 1):
            yield (arr, [j, j+1])
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    yield (arr, [])


if __name__ == '__main__':
    from util import rand_int_array, animate
    arr = rand_int_array(20, 1, 500)
    arr_origin= arr[:]
    arr_gen = sorts(arr)
    animate(arr_origin, arr_gen, 100)
