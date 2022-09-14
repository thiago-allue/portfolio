
# coding: utf-8

# ## Creating your own Iterator
# 
# An `Iterator` is a class that implements (at least) the following methods:
# 
# - `__iter__()`
# - `__next__()`
# 
# Let's implement an `Iterator` that allows you to walk through its elements in random order.

# In[7]:


import random


class RandomIterator:
    
    def __init__(self, *elements):
        
        self._elements = list(elements)
        
    def __iter__(self):
        
        random.shuffle(self._elements)
        self._cursor = 0
        return self
    
    def __next__(self):
        
        if self._cursor >= len(self._elements):
            raise StopIteration()
        e = self._elements[self._cursor]
        self._cursor += 1
        return e


# Now let's see our `RandomIterator` in action!

# In[10]:


i = RandomIterator(1, 2, 3)
for e in i:
    print(e)
print('--')
for e in i:
    print(e)

