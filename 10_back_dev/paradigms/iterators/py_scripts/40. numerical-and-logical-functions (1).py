
# coding: utf-8

# # Numerical and logical functions for working with iterators
# 
# These functions are always available. You don't need to import them.
# 
# ## `any()`: checks if at least one element evaluates to `True`
# 
# Without `any()`:

# In[3]:


none_true = [0, 0, 0]
some_true = [0, 1, 0]
all_true  = [1, 1, 1]

def check_any(i):
    for e in i:
        if e:
            return True
    return False

check_any(none_true)


# With `any()`:

# In[6]:


any(none_true)


# An equivalent implementation using a generator expression:

# In[9]:


True in (bool(e) for e in none_true)


# ## `all(): checks if all elements evaluates to `True`
# 
# Without `all()`:

# In[12]:


def check_all(i):
    for e in i:
        if not e:
            return False
    return True

check_all(none_true)


# With `all()`:

# In[15]:


all(none_true)


# An equivalent implementation using a generator expression:

# In[18]:


False not in (bool(e) for e in none_true)


# ## sorted(), min(), max(), and sum()

# `sorted()` takes an Iterator with numeric elements, sorts it, and returns a `list`:

# In[19]:


numbers = [2, -1, 2, 4]
sorted(numbers)


# Without `min()` and `max()`:

# In[21]:


sorted(numbers)[-1]


# With `min()` and `max()`:

# In[23]:


max(numbers)


# Without `sum()`:

# In[24]:


def get_sum(i):
    total = 0
    for e in i:
        total += e
    return total

get_sum(numbers)


# With `sum()`:

# In[25]:


sum(numbers)

