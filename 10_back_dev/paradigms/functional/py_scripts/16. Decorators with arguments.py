
# coding: utf-8

# ## Let's start with our factorial function
# 
# For no particular reason. We just need a function that we can time!

# In[1]:


def factorial(n):
    
    return 1 if n == 0 else n*factorial(n-1)


# ## What if we want to specify the units of time?
# 
# If we want to specify the units of time (seconds or milliseconds), we need to provide the units of time as arguments to the decorator. We can do this, but it requires another level of nesting!

# In[3]:


import time


def timer_with_arguments(units='s'):

    def timer(fnc):

        def inner(arg):

            """Inner function"""

            t0 = time.time()
            fnc(arg)
            t1 = time.time()        
            diff = t1-t0
            if units == 'ms':
                diff *= 1000
            return diff

        return inner
    
    return timer


timed_factorial = timer_with_arguments(units='ms')(factorial)
timed_factorial(500)


# ## That's a decorator with arguments!
# 
# 
# Again, using the `@` syntax, this is gives very clean code!

# In[6]:


@timer_with_arguments(units='s')
def factorial(n):
    
    return 1 if n == 0 else n*factorial(n-1)


factorial(100)

