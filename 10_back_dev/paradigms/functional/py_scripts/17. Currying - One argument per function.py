
# coding: utf-8

# ## Let's take a simple function
# 
# Most functions, even simple ones, take multiple arguments

# In[2]:


def add(a, b, c):
    
    return a + b + c

print(add(10,100,1000))


# ## Binding function arguments
# 
# But we can 'bind' arguments to a function, so that we end up with a function that takes one argument less than the original function. This is done with `functools.partial()`.

# In[3]:


from functools import partial

add_10 = partial(add, 10)
add_10_100 = partial(add_10, 100)
print(add_10_100(1000))


# ## Currying
# 
# *Currying* is a specific kind of argument binding, in which we create a sequence of functions that each take exactly one argument. In Python, you can implement this elegantly with a decorator.

# In[8]:


from inspect import signature

def curry(fnc):
    
    def inner(arg):
        
        if len(signature(fnc).parameters) == 1:
            return fnc(arg)
        return curry(partial(fnc, arg))
    
    return inner
        
    
@curry
def add(a, b, c):
    
    return a + b + c


add_10 = add(10)
add_10_100 = add_10(100)
print(add_10_100(1000))

