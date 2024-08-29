def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    results = []

    for item in lst:
        if lst.index(item) % 2 == 0:
            results.append(item)

    return results

    # return lst[::2]
    # return [val for i, val in enumerate(lst) if i % 2 == 0]
