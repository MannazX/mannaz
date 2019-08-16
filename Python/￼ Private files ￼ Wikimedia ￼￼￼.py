# Exercise 3.25 Implement the factorial function.

def fact(n):
    """Computes n!
    :param n: A positive `int`.
    :return: An `int` with the value n!.
    """
    # Ensure that the input is a positive integer.
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"`fact` expects an positive integer, received: {n}")

    # Special case: 0! = 1! = 1.
    if n == 0 or n == 1:
        return 1

    # Compute the factorial.
    partial_factorial = 1
    for i in range(1, n + 1):
        partial_factorial *= i

    return partial_factorial


def test_fact():
    # Check an arbitrary case.
    n = 4
    expected = 4 * 3 * 2 * 1
    computed = fact(n)
    assert computed == expected
    # Check the special cases.
    assert fact(0) == 1
    assert fact(1) == 1


if __name__ == "__main__":
    test_fact()
