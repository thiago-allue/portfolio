
# coding: utf-8

# ## How do `and` and `or` really work?
# 
# Let's consider these two custom implementations of `and` and `or`.

# In[1]:


def my_and(*values):
    
    """An implementation of `and`, which accepts a list of arguments
    and returns the first argument that is False or the last argument
    if all arguments are True."""
    
    for value in values:
        if not value:
            return value
    return value


def my_or(*values):
    
    """And implementation of `or`, which accepts a list of arguments
    and returns the first argument that is True or the last argument
    if all arguments are False."""
    
    for value in values:
        if value:
            return value
    return value


# ## Unit testing
# 
# Let's try a few testcases to see if `my_and()` and `my_or()` are really equivalent to `and` and `or`.

# In[5]:


my_or('', 'a', '') == ('' or 'a' or '')


# ## Flow control
# 
# But `and` and `or` have another important property, which our custom implementations do not have: Not all arguments are even evaluated! This makes it possible to use `and` and `or` as flow control tools.

# In[14]:


# We limit ourselves to vertebrates, and even then this is not biologically accurate!
ANIMALS = 'mammal', 'reptile', 'amphibian', 'bird'
EGG_LAYING_ANIMALS = 'reptile', 'amphibian', 'bird'

is_animal = lambda animal: animal in ANIMALS
animal_lays_eggs = lambda animal: print('x') or animal in EGG_LAYING_ANIMALS

lays_eggs = lambda thing: is_animal(thing) and animal_lays_eggs(thing)
lays_eggs('reptile')

