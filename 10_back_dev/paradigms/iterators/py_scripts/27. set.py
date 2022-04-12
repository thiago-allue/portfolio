
# coding: utf-8

# ## Basic set operations
# 
# - A `set` is defined using curly braces (`{}`) with comma-separated elements
# - Elements can be any hashable Python object

# In[3]:


mammals = {'Human', 'Whale', 'Dog', 'Cat'}
print(mammals)


# You can add and remove elements. Adding an element that was already in the `set` does nothing.

# In[4]:


mammals.add('Mouse')
mammals.remove('Dog')
print(mammals)


# ## Set theory
# 
# The standard mathematical operations of set theory are supported.
# 
# - `s1.union(s2)` or `s1 | s2`
# - `s1.intersection(s2)` or `s1 & s2`
# - `s1.difference(s2)` or `s1 - s2`
# - `s1.issubset(s2)` or `s1 < s2`
# - `s1.issuperset(s2)` or `s1 > s2`
# - etc.
# 

# In[10]:


mammals = {'Human', 'Whale', 'Dog', 'Cat'}
pets = {'Dog', 'Cat', 'Goldfish'}

print(mammals > pets)

