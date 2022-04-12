
# coding: utf-8

# ## Let's start with our factorial function
# 
# For no particular reason. We just need a function that we can time!

# In[1]:


def factorial(n):
    
    return 1 if n == 0 else n*factorial(n-1)


# ## Another way of timing a function
# 
# Here's another way to time a function: by writing a wrapper function (`timer()`) that takes a function as an argument (`fnc`), and returns a new function that times and executes `fnc`!

# In[3]:


import time

def timer(fnc):
    
    def inner(arg):
        
        t0 = time.time()
        fnc(arg)
        t1 = time.time()
        return t1-t0
    
    return inner


timed_factorial = timer(factorial)
timed_factorial(500)


# ## That's a decorator! (But there's a nicer syntax)
# 
# The `timer` function that we've defined above is a decorator. You can apply a decorator to a function directly, using the `@` syntax.

# In[4]:


@timer
def timed_factorial(n):
    
    return 1 if n == 0 else n*factorial(n-1)


timed_factorial(500)

