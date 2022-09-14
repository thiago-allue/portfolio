
# coding: utf-8

# ## Let's start with our factorial function
# 
# For no particular reason. We just need a function that we can time!

# In[2]:


l_factorial = lambda n: 1 if n == 0 else n*l_factorial(n-1)


# ## Timing
# 
# ### The procedural way, going line by line
# 
# Factorial is a recursive and hence time-consuming operation. Let's see how long it takes.

# In[3]:


import time

t0 = time.time()
l_factorial(900)
t1 = time.time()
print('Took: %.5f s' % (t1-t0))


# ### The functional way, with a wrapper function
# 
# But a better way is to write a wrapper function that times every function that's passed onto it!

# In[4]:


def timer(fnc, arg):
    
    t0 = time.time()
    fnc(arg)
    t1 = time.time()
    return t1-t0

print('Took: %.5f s' % timer(l_factorial, 900))


# ### The fully functional way, with lambda wrapper functions
# 
# We can even turn `timer()` into a lambda function, although it takes a pretty functional state of mind to do so!

# In[5]:


l_timestamp = lambda fnc, arg: (time.time(), fnc(arg), time.time())
l_diff = lambda t0, retval, t1: t1-t0
l_timer = lambda fnc, arg: l_diff(*l_timestamp(fnc, arg))

print('Took: %.5f s' % l_timer(l_factorial, 900))

