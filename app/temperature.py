def min_temp(measurements):
    """
    >>> min_temp([20, 28, 18, 20])
    [18, 20, 20]

    >>> min_temp([20, 18])
    [18, 20]
    """
    measurements.sort()
    return measurements[:3]
