
# coding: utf-8

# ## Iterator unpacking
# 
# When the right side of an assignment consists of multiple values, you get a list or a tuple. This is a regular assignment, and allows you to construct `tuple`s, `list`s, and `set`s.

# In[1]:


animals = 'Praying Mantis', 'Ant', 'Whale', 'Lizard'


# But the left side can also consist of multiple variables! This is called *unpacking* or *multiple assignment*.
# 

# In[3]:


a1, a2, a3, a4 = animals
print(a1, a2, a3, a4)


# ## Unpacking nested iterators
# 
# Iterators that consist of iterators can be unpacked in one go!

# In[4]:


animals_by_class = ('Praying Mantis', 'Ant'), 'Whale', 'Lizard'
(a1, a2), a3, a4 = animals_by_class
print(a1, a2, a3, a4)


# ## Unpacking an iterator with an unknown length
# 
# - Or: Star unpacking
# - Or: Extended iterator unpacking
# 
# *Note for Python 2: This is only supported in Python 3*
# 
# If you don't know how long an iterator is, you can capture the first and last items, and capture all the middle items in a rest variable.
# 

# In[6]:


animals = 'Praying Mantis', 'Ant', 'Whale', 'Lizard'
a1, *rest, a2 = animals
print(a1, rest, a2)


# ## Unpacking a `dict`
# 
# If you directly unpack a `dict`, you get the keys (in an unpredictable order!).

# In[8]:


animals_and_classes = {
    'Praying Mantis'    : 'Insect',
    'Ant'               : 'Insect',
    'Whale'             : 'Mammal',
    'Lizard'            : 'Reptile'
}

a1, a2, a3, a4 = animals_and_classes
print(a1, a2, a3, a4)


# To get the keys and the values, you can use the `dict.items()` function, and then unpack the result as a nested iterator.

# In[9]:


(k1, v1), (k2, v2), (k3, v3), (k4, v4) = animals_and_classes.items()
print(k1, v1)
print(k2, v2)
print(k3, v3)
print(k4, v4)

