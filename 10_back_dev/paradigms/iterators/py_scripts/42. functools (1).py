
# coding: utf-8

# ## The `functools` module
# 
# The `functools` module provides higher-level functions, many of which or often used in combination with iterators.

# In[1]:


import functools as ft


# The `partial()` function binds arguments to a function, so that they function can later be called without passing this argument. 
# 
# This is related to the functional-programming concept *currying*, in which a single function that takes multiple arguments is turned into a chain of functions that each take on argument.

# In[3]:


import math

print(math.sqrt(9))
sqrt_9 = ft.partial(math.sqrt, 9)
print(sqrt_9())


# The `@lru_cache()` decorator remembers the results of a function call, and, when the function is called again with the same set of arguments, returns this result right away. This is a form of caching, and is related to the functional-programming concept *memoization*.

# In[10]:


import itertools as it
import time

@ft.lru_cache()
def prime_below(x):

    return next(
        it.dropwhile(
            lambda x: any(x//i == float(x)/i for i in range(x-1, 2, -1)),
            range(x-1, 0, -1)
            )
        )

t0 = time.time()
print(prime_below(10000))
t1 = time.time()
print(prime_below(10000))
t2 = time.time()
print('First took %.2f ms' % (1000.*(t1-t0)))
print('Then took %.2f ms' % (1000.*(t2-t1)))


# The `@singledispatch` decorator allows you to create different implementations of a function, given different argument types. The type of the *first* argument is used to decide which implementation of the function should be used.

# In[15]:


@ft.singledispatch
def add(a, b):
    return a+b

@add.register(str)
def _(a, b):
    return int(a)+int(b)

print(add('1', '2'))

