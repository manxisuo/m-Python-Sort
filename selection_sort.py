# _*_ coding: utf-8 _*_


def sorts(arr):
    yield (arr, [])
    n = len(arr)  # type: int
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                yield (arr, [i, min_idx, j])
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield (arr, [i, min_idx])
    yield (arr, [])


if __name__ == '__main__':
    from util import rand_int_array, animate
    arr = rand_int_array(50, 1, 50)
    arr_origin = arr[:]
    arr_gen = sorts(arr)
    animate(arr_origin, arr_gen, 100)
