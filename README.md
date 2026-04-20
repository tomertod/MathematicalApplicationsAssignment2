# Mathematical Applications - Assignment 2
## Numerical Analysis: Lagrange Interpolation & Trapezoidal Integration

### Submitting Students:
* **Tomer Todria** - 318784709
* **Asaf Katz** - 323841338

---

### Project Description
This assignment focuses on two core challenges in numerical analysis: **Polynomial Interpolation** and **Numerical Integration**. The implementations were written in pure Python, adhering to the constraint of not using external mathematical libraries.

---

### Implementation Details

#### Part 1: Lagrange Interpolation
The function `find_value_by_Interpolation` estimates the value of an unknown function at point $x$, given a set of $n$ coordinates.

* **Algorithm:** We implement the **Lagrange form** of the interpolating polynomial.
* **Logic:** 1. For each point $j$, we construct the **Lagrange Basis Polynomial** $L_j(x)$, which satisfies $L_j(x_j) = 1$ and $L_j(x_k) = 0$ for all $k \neq j$.
    2. The final result is the linear combination: $P(x) = \sum y_j \cdot L_j(x)$.
* **Complexity:** The function iterates through the points to build the products, ensuring an $O(n^2)$ time complexity for evaluating a single point.

#### Part 2: Numerical Integration (Trapezoidal Rule)
The function `trapezoidal_integral` approximates the definite integral (the area under the curve) of a function $f$ over the interval $[a, b]$.

* **Algorithm:** We utilize the **Composite Trapezoidal Rule**.
* **Logic:** 1. The interval $[a, b]$ is divided into $n$ equal sub-intervals of width $h = \frac{b-a}{n}$.
    2. We approximate the region under the curve as a series of trapezoids rather than rectangles.
    3. **Formula:** The sum is calculated as:  
       $\int_{a}^{b} f(x) dx \approx \frac{h}{2} \left[ f(a) + 2\sum_{k=1}^{n-1} f(x_k) + f(b) \right]$
* **Accuracy:** By increasing the parameter $n$, the "fineness" of the division increases, leading to a more accurate approximation of the integral.

---

### How to Run
1. Ensure you have Python 3.x installed.
2. Run the script containing the functions.
3. Example usage for Interpolation:
   ```
   points = [(4, 0), (2, 4), (6, 4)]
   result = find_value_by_Interpolation(points, 3) # Expected: 1.0
   ```
4. Example usage for Integration: 
```
# Define your function f(x)
area = trapezoidal_integral(f, a=0, b=1, n=100)
```

### ### Constraints & Notes:
1. No External Libraries: The solution is implemented using only native Python features (lists, loops, basic math).
2. Efficiency: The integration method is optimized to evaluate the function $f(x)$ only once for each point in the interval.
