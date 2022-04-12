
# coding: utf-8

# ## Basic dict operations
# 
# - A `dict` is defined using curly braces (`{}`) with key-value mappings
# - Both the keys and values can be any Python object—or almost, because keys must be hashable (but most objects are)

# In[1]:


d = {
    'Praying Mantis'    : 'Insect',
    'Whale'             : 'Mammal'
}
print(d)


# A `dict` is mutable, so you can add and remove elements.

# In[3]:


d['Lizard'] = 'Reptile'
print(d)


# ## Iterating through a `dict`
# 
# - By default, a `dict` iterates over its keys
# - But you can also iterate over its values using `d.values()`
# - Or iterate over `key, value` tuples using `d.items()` or (destructively) using `d.popitem()`
# 
# *Important:* Don't assume that elements are returned in a particular order! (Even though some implementations of Python do that.)

# In[9]:


d = {
    'Praying Mantis'    : 'Insect',
    'Whale'             : 'Mammal',
    'Lizard'            : 'Reptile'
}

while d:
    species, class_ = d.popitem()
    print(species, class_)
print(d)

