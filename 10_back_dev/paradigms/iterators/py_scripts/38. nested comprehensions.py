
# coding: utf-8

# ## Nested comprehensions
# 
# - Basic syntax: `[expression for element1 in iterable1 for element2 in iterable2]`
# 
# Let's say that you want to define a 2×2 grid of x,y coordinates. With a nested `for` loop, you could this as follows:

# In[1]:


grid = []
for x in range(2):
    for y in range(2):
        grid.append((x,y))
print(grid)


# With a nested list comprehension, this becomes:

# In[3]:


def g(s):
    print(s)
    yield 1
    print(s)
    yield 2

grid = [ (x, y) for x in g('x') for y in g('y') ]
print(grid)

