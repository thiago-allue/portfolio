
# coding: utf-8

# Let's start with some function, `camelcase()`, which transform `'a_string_like_this'` into `'AStringLikeThise'`.

# In[1]:


def camelcase(s):
    
    return ''.join([w.capitalize() for w in s.split('_')])

print(camelcase('some_function'))


# ## The Maybe monad
# 
# The Maybe monad consists of two kinds of data, which are typically called `Just` and `Nothing`. They both behave very simply:
# 
# - When a function is bound to a `Just` value, the function is simply executed, and the result is stored in a new `Just` value.
# - When a function is bound to a `Nothing` value, the function is bypassed, and `Nothing` is returned right away.
# - In additon, when a function generates an error, it returns a `Nothing` value.
# 
# See how similar this is to `nan` behavior?

# In[4]:


class Just:
    
    def __init__(self, value):
        
        self._value = value
        
    def bind(self, fnc):
        
        try:
            return Just(fnc(self._value))
        except:
            return Nothing()
    
    def __repr__(self):
        
        return self._value
    


class Nothing:
    
    def bind(self, fnc):
        
        return Nothing()
    
    def __repr__(self):
        
        return 'Nothing'
    
    
print(Just('some_function').bind(camelcase))
print(Nothing().bind(camelcase))
print(Just(10).bind(camelcase))


# ## The List monad
# 
# The `List` monad stores a list of values. When it is bound to a function, each value is passed onto the function separately, and the result is stored as another `List`.

# In[5]:


class List:
    
    def __init__(self, values):
        
        self._values = values
        
    def bind(self, fnc):
        
        return List([fnc(value) for value in self._values])
    
    def __repr__(self):
        
        return str(self._values)
    
    
List(['some_text', 'more_text']).bind(camelcase)

