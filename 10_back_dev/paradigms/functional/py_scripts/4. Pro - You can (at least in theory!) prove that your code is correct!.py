
# coding: utf-8

# # Pro: You can (at least in theory!) prove that your code is correct
# 
# Functional programming is characterized by:
# 
# - Short functions
# - Referential transparency (return values are completely predictable based on arguments)
# 
# These properties make it possible, in theory, to prove that functions do what they should do.
# 
# This contrasts with the traditional approach of testing functions on a case-by-base basis, or so-called *unit testing*.
# 
# ## Smile!

# In[2]:


import itertools


def smile(l):
    
    """Takes a list of integers. For each integer (i), create
    a list of smileys of length i. Then flatten this list and
    return the result."""

    # This is very functional!
    return list(itertools.chain(*[['☺']*i for i in l]))

# [1,2] → [ ['☺'], ['☺', '☺'] ] → ['☺', '☺', '☺']
print(smile([1,2]))


# ## Unit testing
# 
# If we want to test if `smile()` works as it should, we can design a set of test cases. And then, for each of these test cases, we verify that the output matches our expectation. This is called *unit testing*.
# 
# Here I use simple `assert` statements; in real life, you would generally use some library designed specifically for unit testing, such as `nose` or Python's built-in `unittest`.

# In[8]:


print('Starting test')
assert(smile([]) == [])
assert(smile([1]) == ['☺'])
assert(smile([0]) == [])
assert(smile([1,0,2]) == ['☺', '☺', '☺'])
print('Done')


# ## Provability
# 
# But we can also look inside the function, and try to understand what it does. In this case, we can actually simplify the function a lot!
# 
# `l×a + l×b + l×c →  l×(a+b+c)`
# 
# And now it's obvious that the function is correct. (And that the initial solution was unnecessarily complicated!)

# In[7]:


def smile(l):
    
    return ['☺'] * sum(l)

print(smile([1,2]))

