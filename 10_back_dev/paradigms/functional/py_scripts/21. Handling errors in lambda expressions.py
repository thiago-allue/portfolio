
# coding: utf-8

# ## Let's reconsider our lambda

# In[3]:


l_add_str = lambda s: sum([int(i) for i in s.split('+')])


# ## A Maybe-like decorator
# 
# The Maybe monad is not very Pythonic. But we can do something similar using a decorator.

# In[5]:


def maybe(fnc):
    
    def inner(*args):
        
        for a in args:
            if isinstance(a, Exception):
                return a
        try:
            return fnc(*args)
        except Exception as e:
            return e
        
    return inner

safe_add_str = maybe(lambda s: sum([int(i) for i in s.split('+')]))
print(safe_add_str(1+2))


# ## Exceptions are fine!
# 
# Even though `Exception`s are not entirely compatible with a functional programming style, they are still a very good way to deal with errors!
