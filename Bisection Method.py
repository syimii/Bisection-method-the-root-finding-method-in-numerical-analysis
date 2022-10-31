import numpy as np
import matplotlib.pyplot as plt

# Define the function whose roots are required
def f(x):
    return x**3-(0.165*x**2)+3.993

# Implementing Bisection Method 
def bisection(xL, xU, e, maxiter):
    step = 1
    print('\n ****BISECTION METHOD IMPLEMENTATION***** ')
    condition = True
    while condition and step <= maxiter:
        xR = (xL + xU) / 2
        print('\nIteration-%d, xR = %0.6f and f(xR) = %0.6f' % (step, xR, f(xR)))
        
        if f(xL) * f(xR) < 0:
            xU = xR
        else:
            xL = xR
        condition = abs(f(xR)) > e
        print('Required Root is : %0.8f' % xR)
        step = step + 1
        if step > maxiter:
            print("\nYou have reached the maximum iterations.")
            print('Required Root after 20 iterations is : ' + str(xR))
    return xR, step

# Input Initial Guess, Tolerance and Max Iterations
xL = float(input('First Guess: '))
xU = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))
maxiter = 20 

# Checking Correctness of initial guess values and bisecting
if f(xL) * f(xU) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try again with different guess values.')
else:
    xR, step = bisection(xL, xU, e, maxiter)
    
# Plot the f(x) and root
x = np.linspace(-10, 10, 80)
plt.figure()
plt.plot(x, f(x), label = 'f(x)')
plt.plot(xR, f(xR), 'r*', label=('Root of f(x) after '+str(step-1)+' iterations'))
plt.title(r'$f(x) = x^{3}-0.165x^{2}+3.993$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()