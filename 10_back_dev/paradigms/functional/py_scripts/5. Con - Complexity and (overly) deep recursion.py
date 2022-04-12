
# coding: utf-8

# # Con: Complexity and (overly) deep recursion
# 
# Where procedural programming relies on loops, functional programming often relies on recursion.
# 
# ## A procedural approach
# 
# Let's first consider a procedural implementation of the factorial (!) operation.

# In[1]:


def p_factorial(n):
    
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


print(p_factorial(0)) # = 1 by convention
print(p_factorial(2)) # = 1×2 = 2
print(p_factorial(4)) # = 1×2×3x4 = 24


# ## A functional approach

# In[2]:


def f_factorial(n):
    
    return 1 if n == 0 else n*f_factorial(n-1)


print(f_factorial(0)) # = 1 by convention
print(f_factorial(2)) # = 1×2 = 2
print(f_factorial(4)) # = 1×2×3x4 = 24


# ## Meet `RecursionError`!
# 
# The procedural and functional implementations are valid and identical. But the functional implementation is limited by Python's maximum recursion depth of 1000!

# In[4]:


f_factorial(1000)

