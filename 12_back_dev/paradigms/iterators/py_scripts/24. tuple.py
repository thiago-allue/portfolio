
# coding: utf-8

# ## Basic tuple operations
# 
# - A `tuple` is just a comma-separated sequence of elements, or surrounded by parentheses if this is required to avoid ambiguity
# - A `tuple` element can be any Python object
# - A `tuple` is immutable, so you cannot `append()`, `insert()`, `pop()`, or `remove()` elements
# - But you can concatenate (`+`), which creates a new `tuple`

# In[2]:


t = 'John', 24
t = t + ('Berlin',)
print(t)


# ## Working with sequences
# 
# *Works with all built-in sequences*
# 
# Python offers a clean syntax to perform common operations and checks with sequences:
# 
# - Loop through elements with `for`
# - Check if an element exists with `in`
# - Repeat with `*`
# - Check number of elements with `len()`
# - Etc.

# In[7]:


len(3 * t)

