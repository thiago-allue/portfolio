
# coding: utf-8

# ## Basic list operations
# 
# - A `list` is initialized with a square brackets around comma-separated elements
# - A `list` element can be any Python object
# - Add elements with `l.append()` and `l.insert()`
# - Remove elements `l.pop()` and `l.remove()`

# In[5]:


l = ['Paris', 'Oslo', 'Budapest']
l.remove('Oslo')
print(l)


# ## Slicing
# 
# *Works with all built-in iterators, except `set` objects*
# 
# - Get a single element through its position: `l[position]`
# - Get multiple elemetns through slicing: `l[from:to:steps]`
# - Negative steps reverse the order!

# In[11]:


l = ['Paris', 'Oslo', 'Budapest']
print(l[::-1])


# ## Copying
# 
# To create a copy of a `list`, you need to explictly use `l.copy()` or get a complete slice: `l[:]`

# In[14]:


l1 = ['Paris', 'Oslo', 'Budapest']
l2 = l1[:]
l2.append('Kiev')
print(l1, l2)

