def regula_falsi_method( f,a,b,max_iterations):
    if f(a)*f(b)>0:
        print("a and b must have opposite signs")
        return None
    print(f"{'Iterations':^11}{'a':^11}{'b':^11}{'c':^11}{'f(c)':^11}")
    print("-"*56)
    for i in range(1,max_iterations+1):
        #calculating c by regula falsi method
        c=b-(b-a)*(f(b))/(f(b)-f(a))
        fc=f(c)
        print(f"{i:^10} {a:^10.7f} {b:^10.7f} {c:^10.7f} {fc:^10.7f}")
        if f(c)==0:
            break
        if f(c)*f(a)<0:
            b=c
        else:
            a=c
    return c
def f(x):
    return x**3 - 9*x + 1

max_iterations=6
a=2
b=4
root=regula_falsi_method(f,a,b,max_iterations)
if root is not None:
    print(f"\nThe root after {max_iterations} iterations is approximately: {root:.6f}")
