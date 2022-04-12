
# coding: utf-8

# ## Generator expressions: Basic syntax
# 
# - Basic syntax: `(expression for element in iterable)`
# - Parentheses are optional if leaving them does not result in ambiguity
# - Because they are generators, they are *lazy* and not evaluated immediately. You need actively iterate through them!

# In[2]:


from math import sqrt

g = (sqrt(i) for i in range(5))
for i in g:
    print(i)


# Because they are generators, you can iterate over them using `next(g)` until you get a stopiteration.

# In[4]:


g = (sqrt(i) for i in range(5))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# ## Filtering generator expressions
# 
# - Filtering syntax: `(expression for element in iterable if expression)`
# - This is an alternative (in many cases) to the `continue` statement
# 
# Let's consider a `for` loop that skips all odd numbers:

# In[5]:


g = (i for i in range(10) if not i%2)
for i in g:
    print(i)


# ## Breaking generator expressions (deprecated)
# 
# It is, in principle, possible to break a generator expression by explicitly raising a `StopIteration`. However, this behavior has been deprecated and as of Python 3.6 gives a `DeprecationWarning`.

# In[6]:


def fibonacci():
    
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]

        
def stop():
    raise StopIteration()
    
    
g = (i for i in fibonacci() if i < 10 or stop())
for i in g:
    print(i)


# Usually, you can avoid this construction by rewriting code. And if you *really want*, you can emulate by passing a custom `Exception` and catching this in a custom `wrap()` function.

# In[8]:


class EndGenerator(Exception): pass

def stop():
    raise EndGenerator()
    
def wrap(g):
    
    l = []
    while True:
        try:
            l.append(next(g))
        except EndGenerator:
            break
    return l
    
    
g = wrap(i for i in fibonacci() if i < 10 or stop())
for i in g:
    print(i)

