# _*_ coding: utf-8 _*_


def sorts(arr):
    yield (arr, [])
    n = len(arr)
    for i in range(1, n):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            yield (arr, [j, j+1])
            j = j - 1
        arr[j + 1] = tmp
        yield (arr, [j+1])
    yield (arr, [])


if __name__ == '__main__':
    from util import rand_int_array, animate
    arr = rand_int_array(20, 1, 100)
    arr_origin = arr[:]
    arr_gen = sorts(arr)
    animate(arr_origin, arr_gen, 100)
