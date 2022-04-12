
# coding: utf-8

# ## Exceptions
# 
# In Python, `Exception`s are the main way to deal with errors. Whenever an error occurs, an `Exception` object is 'raised'. This causes the code to abort, until the Exception is caught in a `try: … except: …` statement.

# In[3]:


def add_str(s):
    
    try:
        return sum([int(i) for i in s.split('+')])
    except AttributeError:
        return None

print(add_str(1+2))


# ## The curse of statements
# 
# 
# But `try` is a *statement*, and you can therefore not use it in `lambda` expressions! Unlike for most other statements, Python does not offer an expression alternative to the `try` statement.

# In[5]:


l_add_str = lambda s: sum([int(i) for i in s.split('+')])

print(l_add_str(1+2))

