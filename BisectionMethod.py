def bisection_method_with_iterations(f, a, b, max_iterations):
    #Checking if a and b have opposite signs
    if f(a) * f(b) >= 0:
        print("The function must have different signs at points a and b.")
        return None
    print(f"{'Iteration':^10} {'a':^10} {'b':^10} {'c':^10} {'f(c)':^10}")
    print("-" * 55)
    c = a
    for i in range(1, max_iterations + 1):
        c = (a + b) / 2.0
        fc = f(c)
        print(f"{i:^10} {a:^10.6f} {b:^10.6f} {c:^10.6f} {fc:^10.6f}")
        # If fc=0 we have found the root, no need to iterate further.
        if fc == 0:
            break
        # Decide the new interval
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return c
# Function whose root we have to find.
def f(x):
    return x**3 - 9 * x + 3
# Parameters
max_iterations = 6
a=2
b=4
# Calling bisection method
root = bisection_method_with_iterations(f, a, b, max_iterations)
# Output the result
if root is not None:
    print(f"\nThe root after {max_iterations} iterations is approximately {root:.6f}")
