#Definition of the function for which root has to be computed
def f(x):
    return x**3 + 2*x - 2

#Definition of the derivative of function
def fprime(x):
    return 3*x**2 + 2

#Initialization of variables
epsilon = 0.0001  #Declaration and initialization of a constant which is approximately near 0
guess = 1      #Initial guess. Any value between 0 and 1 can be selected as initial guess.
i = 0            #Declaration and initialization of counter to check no. of iterations taken to converge

print('Iteration     Guess value of root')
#Condition for the while loop is set such that when function is evaluated to 0.001, the loop will converge.
while abs(f(guess)) >= epsilon:
    #Newton Raphson approximation
    guess = guess - (f(guess)/fprime(guess))
    #Counter
    i += 1
    #Results at each iteration
    print ('    '+ str(i) + '               ' + str(round(guess, 7)))

#Final result
print('Approximate solution of the root to 2 decimal places is '+str(round(guess,2))+'. It took total of ' + str(i) + ' iterations to converge.')
