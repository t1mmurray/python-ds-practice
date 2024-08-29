def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    trueVals = []
    for item in lst:
        if item:
            trueVals.append(item)

    return trueVals
