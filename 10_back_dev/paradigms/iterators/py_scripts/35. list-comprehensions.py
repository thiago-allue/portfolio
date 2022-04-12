
# coding: utf-8

# ## List comprehensions: Basic syntax
# 
# - Minimal syntax: `[expression for element in iterable]`
# - The square brackets are necessary—without it's a generator expression!
# 
# Let's consider a `for` loop that prints out the square root of 0 - 4:

# In[1]:


from math import sqrt

for i in range(5):
    print(sqrt(i))


# Now let's implement this with a `list` comprehension:

# In[3]:


[print(sqrt(i)) for i in range(5)]


# ## Filtering list comprehensions
# 
# - Filtering syntax: `[expression for element in iterable if expression]`
# - This is an alternative (in many cases) to the `continue` statement
# 
# Let's consider a `for` loop that skips all odd numbers:

# In[5]:


for i in range(5):
    if i%2:
        continue
    print(i)


# Now let's implement this with a `list` comprehension:

# In[7]:


[print(i) for i in range(5) if not i%2]


# ## Breaking list comprehensions
# 
# - There is no way to `break` a list comprehension
# - Although you can do this with a generator expression, which we will meet later this section!
# 
# Let's consider a `for` loop that iteratres over an infinite generator function, `fibonacci()`, until a number that is larger than 10 is encountered:

# In[8]:


def fibonacci():
    
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]

        
for i in fibonacci():
    if i > 10:
        break
    print(i)


# There is no way to implement this behavior with a `list` comprehension. The following results in an infinite loop!

# In[9]:


[i for i in fibonacci() if i <= 10]

