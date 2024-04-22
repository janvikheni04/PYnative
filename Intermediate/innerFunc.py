'''Create an inner function
Question description: -

Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
Create an inner function inside an outer function that will concatenate x and y.
At last, an outer function will join the word 'developer' to it.'''

def a(a,b):
    def innerF(a,b):
        return a + b
    
    r = innerF(a,b)
    return r + 'Developers'

r1 = a("Emma", "Kelly")
print(r1)