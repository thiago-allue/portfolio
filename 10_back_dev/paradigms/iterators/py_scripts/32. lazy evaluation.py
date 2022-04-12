
# coding: utf-8

# ## Eager evaluation
# 
# Let's consider a function that generates a fibonacci series of length `n`. This is an *eager* implementation, because the full series is created and held in memory at once.

# In[1]:


def eager_fibonacci(n):
    
    l = [1, 1]
    for i in range(n-2):
        l.append(sum(l[-2:]))
    return l

print(eager_fibonacci(10))


# ## Lazy evaluation
# 
# Now let's consider a Generator function that also generates a fibonacci series, but does so one number at a time. This is a *lazy* implementation, because only two numbers are held in memory at once (we need two numbers in order to determine the next number in the series). We also no longer need to specify the length of the series is advance. We just keep going!

# In[2]:


def lazy_fibonacci():
    
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]

        
for i, f in enumerate(lazy_fibonacci()):
    if i == 10:
        break
    print(f)

