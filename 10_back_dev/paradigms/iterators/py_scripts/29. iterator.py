
# coding: utf-8

# ## What is an Iterator?
# 
# An Iterator is any object that implements the Iterator protocol. Iterators support:
# 
# - Looping through the object in a `for` loop
# - Using `in` to check whether the object contains some element
# 
# Most Iterator types, such as `list`, `dict`, and `tuple`, support more! But this extra functionality is not part of the Iterator protocol per se.

# In[9]:


t = 'a', 'b', 'c'
for e in t:
    print(e)


# ## `iter()`, `next()`, and `StopIteration`
# 
# Let's consider the protocol more formally:
# 
# - First, `iter()` provides an actual iterator object
# - Then, `next()` retrieves elements from this iterator object
# - Until the iterator is exhausted, in which case a `StopIteration` is raised

# In[7]:


i = iter(t)
print(next(i))
print(next(i))
print(next(i))
print(next(i))


# In other words, the `for` loop above is equivalent to the following code:

# In[8]:


i = iter(t)
while True:
    try:
        e = next(i)
    except StopIteration:
        break
    print(e)

