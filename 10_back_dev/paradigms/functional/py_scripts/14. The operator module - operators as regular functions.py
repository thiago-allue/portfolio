
# coding: utf-8

# Let's take our old friend: the factorial function!

# In[1]:


l_factorial = lambda n: 1 if n == 0 else n*l_factorial(n-1)


# ## Chaining functions and combining return values
# 
# Say that we want to call this function a number of times, with different arguments, and do something with the return values. How can we do that?

# In[2]:


def chain_mul(*what):
    
    """Takes a list of (function, argument) tuples. Calls each
    function with its argument, multiplies up the return values,
    (starting at 1) and returns the total."""
    
    total = 1
    for (fnc, arg) in what:
        total *= fnc(arg)
    return total


chain_mul( (l_factorial, 2), (l_factorial, 3) )


# ## Operators as regular functions
# 
# The function above is not very general: it can only multiple values, not multiply or subtract them. Ideally, we would pass an operator to the function as well. But `*` is syntax and not an object that we can pass! Fortunately, the Python's built-in `operator` module offers all operators as regular functions.

# In[4]:


import operator


def chain(how, *what):
        
    total = 1
    for (fnc, arg) in what:
        total = how(total, fnc(arg))
    return total


chain(operator.truediv, (l_factorial, 2), (l_factorial, 3) )

