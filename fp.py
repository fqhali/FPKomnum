import numpy
import sympy

# integralnya -> f(x) = (4/5)*x**5-4*x**3 sebagai input
# x0 = 2
# x3 = 11
# h = 3

def errortrue(f_value, y_values):
    return abs(((f_value-y_values)/f_value)*100)

def heun_method (f, x0, x3, h):
    x = sympy.symbols('x')
    f_derivative = sympy.diff(f, x)
    print(f"\nf(x, y) = {f_derivative}\n")
    xn = x0
    step = 3
    
    for i in range(step):
        f_value = f.subs(x, xn)
        f_valueup = f.subs(x, xn+h)
        f_derivative_value = f_derivative.subs(x, xn)
        f_derivative_valueup = f_derivative.subs(x, xn+h)
        if(i == 0 ):
            print(f"Step 1:\nx0 = {xn:.2f}\ty0 = {f_value:.2f}\n")
            #print(f"{f_derivative_value}")
            #print(f"{f_derivative_valueup}")
            #print(f"{f_value}")

            y_values = f_value + (((f_derivative_value+f_derivative_valueup)/2)*h)
            xn = xn + h
            print(f"x0 = {xn:.2f}\ty1 = {y_values:.2f}\n")
            error = round(errortrue(f_valueup, y_values), 2)
            print(f"\t\tEt = {error:.2f}%")
            continue
        y_values = y_values + (((f_derivative_value+f_derivative_valueup)/2)*h)
        xn = xn + h
        print(f"Step {i+1}:\nx0 = {xn:.2f}\ty1 = {y_values:.2f}\n")
        #print(f"{f_value}")
        error = round(errortrue(f_valueup, y_values), 2)
        print(f"\t\tEt = {error:.2f}%")


    
def main():
    x = sympy.symbols('x')
    f = input("Enter the function f(x) in terms of x: ")
    f = sympy.sympify(f)
    x0 = float(input("Enter x0: "))
    x3 = float(input("Enter x3: "))
    h = float(input("Enter step h: "))
    heun_method(f, x0, x3, h)

if __name__ == "__main__":
    main()
