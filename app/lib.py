# def is_valid_email(email):
#     """
#     >>> is_valid_email('student@localhost.ru')
#     True
#
#     >>> is_valid_email('vasya')
#     False
#     """
#
#     return '@' in email

def distance(data):
    """
    >>> distance([4])
    0

    >>> distance([4, 5])
    1
    """

    return max(data) - min (data)

def negative_count(scores):
    """
    >>> negative_count([1, 200, -50, 10, -20])
    2

    >>> negative_count([2, 0, 14])
    0

    >>> negative_count([])
    0
    """
    negative = 0
    for score in scores:
        if score < 0:
            negative += 1

    return negative

