
# coding: utf-8

# ## Inner and outer functions
# 
# Let's start by defining a very basic nested function.

# In[3]:


def outer():
    
    def inner():
        
        print('I\'m inner')
    
    inner()

outer()


# Now let's all function refer to a variable `x`. This is *the same* variable, the global variable x, in all cases.

# In[4]:


def outer():
    
    def inner():
        
        print('Inner:\t\t', x)
    
    print('Outer (before):\t', x)
    inner()
    print('Outer (after):\t', x)

    
x = 'global'
print('Global (before):', x)
outer()
print('Global (after): ', x)


# ## Controlling the variable scope with `global` and `nonlocal`
# 
# But as soon as the function assign a new value to `x`, they create their own local variable `x`. So now there are three variables `x`: at the global level, at the level of `outer()`, and at the level of `inner()`. But we can change this using two statements:
# 
# - `global` binds a variable to the global level
# - `nonlocal` (Python >= 3) binds a variable to one level higher

# In[7]:


def outer():
    
    def inner():
        
        nonlocal x
        x = 'inner'
        print('Inner:\t\t', x)
    
    x = 'outer'
    print('Outer (before):\t', x)
    inner()
    print('Outer (after):\t', x)

    
x = 'global'
print('Global (before):', x)
outer()
print('Global (after): ', x)

