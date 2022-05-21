"""
for the function below, add your code in appropriate place that checks the input n.
n should be a non-negative integer, otherwise a ValueError should be raised
and a proper error message should be provided informing the user of the error
for simplicity, you may assume that the input is always an integer for this exercise
"""


class UncountableError(ValueError):
    def __init__(self, value):
        super().__init__(f'Invalid value for n, {value}. n must be greater than 0.')
        self.value = value


def count_from_zero_to_n(n):
    if not isinstance(n, int) or n < 0:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


count_from_zero_to_n('tr')
