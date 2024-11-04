def odwracanie(L, left, right):
    L[left:right + 1] = L[left:right + 1][::-1]
    return L


def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L


def odwracanie_recur(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_recur(L, left + 1, right - 1)
    return L


assert (odwracanie([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 5) == [1, 2, 6, 5, 4, 3, 7, 8, 9])
assert (odwracanie_iter([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 5) == [1, 2, 6, 5, 4, 3, 7, 8, 9])
assert (odwracanie_recur([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 5) == [1, 2, 6, 5, 4, 3, 7, 8, 9])
