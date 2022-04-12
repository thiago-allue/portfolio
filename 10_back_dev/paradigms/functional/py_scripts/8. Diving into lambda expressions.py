
# coding: utf-8

# ## A simple procedural function
# 
# In procedural programming, functions are defined with `def` statements.

# In[1]:


from math import sqrt


def p_pythagoras(x, y):
    
    return sqrt(x**2 + y**2)

p_pythagoras(1, 1)


# ## A simple `lambda` function
# 
# In functional programming, we can use `lambda` expressions for the same purposes.

# In[3]:


l_pythagoras = lambda x, y: sqrt(x**2 + y**2)
l_pythagoras(1,1)


# ## Recursion requires a name
# 
# Functions created with `lambda` expressions can be nameless. But for a function to call itself, it needs a name. In such cases, a `def` statement may be more intuitive.

# In[4]:


def f_factorial(n):
    
    return 1 if n == 0 else n*f_factorial(n-1)


f_factorial(3)


# In[5]:


l_factorial = lambda n: 1 if n == 0 else n*l_factorial(n-1)
l_factorial(3)


# ## When lambda's are convenient
# 
# `lambda` expressions are very convenient if you quickly need a short function, for example to pass as an argument to `map()` or `filter()`.

# In[6]:


l = [0, 1, 2, 3, 4]
list(map(lambda x: x*2, l))

