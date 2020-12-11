class ValueCannotBeNegative(Exception):
    """
    Raised when value is negative
    """


nums = [1, 4, 3, 2, 5]

for num in nums:
    if num < 0:
        raise ValueCannotBeNegative
