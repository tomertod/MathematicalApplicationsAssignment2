import math
def find_value_by_Interpolation(lst: list, x: float) -> float:
    """
    Estimate the value at x using Lagrange interpolation.

    This method uses all points in the input list to construct the Lagrange polynomial.

    Parameters:
        lst (list): A list of (x, y) tuples [(x0, y0), (x1, y1), ...].
        x (float): The x-value at which to evaluate the interpolated polynomial.

    Returns:
        float: The interpolated y-value at x.
    """
    p = 0
    for j, (xj, yj) in enumerate(lst):
        l = 1
        for k, (xk, _) in enumerate(lst):
            if k != j:
                l *= (x - xk) / (xj - xk)
        p += yj * l
    return p
    pass


def trapezoidal_integral(f, a: float, b: float, n: int = 100) -> float:
    """
    Approximate the definite integral of a function using the trapezoidal rule.

    Parameters:
        f (function): The function to integrate.
        a (float): The start of the interval.
        b (float): The end of the interval.
        n (int): Number of subdivisions (default is 100).

    Returns:
        float: The approximate integral of f from a to b.
    """
    h = (b - a) / n          
    total = 0
    i = 0
    while i <= n:           
        x = a + i * h
        if i == 0 or i == n: 
            total += f(x) / 2
        else:
            total += f(x)
        i += 1               
    return total * h 
    pass


if __name__ == '__main__':
    result1 = find_value_by_Interpolation([(4.0, 0.0), (2.0, 4.0), (6.0, 4.0)], 3.0)
    print(result1)  # Output: ~1.0
    result2 = trapezoidal_integral(math.sin, 0, math.pi)
    print(result2)  # Output: ~2.0 (exact integral of sin(x) from 0 to π)
