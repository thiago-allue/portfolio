
# coding: utf-8

# # The `itertools` module
# 
# The `itertools` module provides many convenient functions for working with iterators. Below is a useful selection, but there are more!

# In[1]:


import itertools as it


# ## Functions that create (or operate on) iterators
# 
# `count()` returns an infinite counter. (So it's like an infinite `range()`.)

# In[3]:


for i in it.count(start=10, step=-1):
    if not i:
        break
    print(i)


# `cycle()` loops an iterator infinitely.

# In[5]:


s = 'iterators rock'
for i, ch in zip(range(20), it.cycle(s)):
    print(i, ch)


# `repeat()` creates an infinite iterator from a single element.

# In[6]:


s = 'iterators rock'
for i, s in zip(range(10), it.repeat(s)):
    print(i, s)


# `chain()` links multiple tail to head.

# In[7]:


for e in it.chain('abc', [3,2,1], 'cba'):
    print(e)


# ## Functions to select and group iterator elements
# 
# `compress()` filters an iterator based on a list of selectors. Selectors can be any values that evaluate to boolean `True` or `False`.

# In[8]:


sentence = 'iterators', "don't", 'rock'
selector = True, False, True
for word in it.compress(sentence, selector):
    print(word)


# `takewhile()` takes elements while a criterion is satisfied.

# In[9]:


for i in it.takewhile(lambda x: x < 10, it.count()):
    print(i)


# `dropwhile()` does the opposite: it skips elements while a criterion is satisfied.

# In[10]:


for i in it.dropwhile(lambda x: x < 5, it.count()):
    if i > 10:
        break
    print(i)


# `groupby()` allows you to split an interator into multiple iterators based on a grouping key. Groups have to be consecutive, meaning that you generally want to sort the iterator by the grouping function.

# In[12]:


is_even = lambda x: not x%2

for e, g in it.groupby(
        sorted(range(10), key=is_even),
        key=is_even
    ):
    print(e, list(g))


# ## Combinatorial functions
# 
# `product()` returns the cartesian product of two iterators, which is roughly equal to a nested `for` loop.

# In[13]:


for x, y in it.product([0,1,2], [3,4,5]):
    print(x, y)


# `permutations()` returns all possible different orders (permutations) of the elements in an iterator.

# In[14]:


for i in it.permutations([1,2,3]):
    print(list(i))


# `combinations()` returns all possible ways in which an `r` number of elements can be selected from an iterator, irrespective of the order.

# In[15]:


for i in it.combinations([1,2,3], r=2):
    print(list(i))

