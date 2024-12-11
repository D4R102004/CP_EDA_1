from typing import TypeVar
T = TypeVar('T')


def swap(arr: list[T], init_pos : int, go_to_pos: int):
    temp = arr[init_pos]
    arr[init_pos] = arr[go_to_pos]
    arr[go_to_pos] = temp


def less_pos(arr: list[T], begin: int) -> int:
    p = begin
    for i in range(begin + 1, len(arr)):
        if arr[i] < arr[p]:
            p = i
    return p


def sort_less(arr: list[T]) -> None:
    for k in range(len(arr)):
        swap(arr, k, less_pos(arr, k))


def power(k: int, n: int):
    if n == 0:
        return 1
    if n % 2 != 0:
        return k * power(k, n - 1)
    val = power(k, n // 2)
    return val * val


base = 2
exponent = 64
print(power(base, exponent))
