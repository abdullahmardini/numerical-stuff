# Idea I got from class. I'm pretty sure the algorithm we were given could be 
# implemented recursively.

import math

print("If nothing prints after this, I goofed")

# Takes a (math) function f, the left bound a, the right b, some tolerance tol, 
# and the current approximation for the interval thus far approx. Since I'm 
# computing the area of a trapezoid, the area will {over,under}estimate the 
# actual area until the interval is small enough, then it will be roughly the 
# same. At that point, the approximation doesn't improve, and the new 
# approximation of half the interval will be roughly half the old approximation 
# (up to the tolerance). At this point, just return.
def recursive_trap(f, a, b, tol, approx):
    n_approx = 0.5*(f(a)+f(b)) * abs(b-a)
    if abs(n_approx - 0.5*approx) < tol:
        return n_approx 
    return ( recursive_trap(f, a, (a+b)/2, tol, n_approx) + 
             recursive_trap(f, (a+b)/2, b, tol, n_approx) )

# Function used in the definition of the error function "erf(x)" 
def f(x):
    return(2/math.sqrt(math.pi) * math.exp(-x*x))

print(recursive_trap(f, 0, 1, 1e-10, 100))