
# coding: utf-8

# ## Statements
# 
# ### Assignment
# 
# Procedural programming relies heavily on assignments, which are statements.

# In[ ]:


x = 0
x += 1


# ### Conditional branching (if, elif, else)
# 
# In procedural programming, branching is often implemented with `if` statements, and the associated `elif` and `else` statements.

# In[ ]:


if x == 1:
    print('x == 1')
elif x == 2:
    print('x == 2')    
else:
    print('x not in [1, 2]')


# ### Loops
# 
# In procedural programming, loops are generally implemented with `for` or `while` statements.

# In[ ]:


for x in range(2):
    print(x*2)
    
while True:
    break


# ### Function, generator, and class definitions
# 
# In procedural programming, functions and classes are defined using `def` and `class` statements. `return` and `yield` are also statements.

# In[ ]:


class MyClass:
    pass

def my_function(x):
    return x*2

def my_generator(x):
    yield x*2


# ### Other statements
# 
# Python knows various other statements. You've probably seen them all.

# In[ ]:


import os

assert True

pass

del x

try:
    raise Exception()
except:
    pass

with open('/dev/null') as fd:
    pass


# ## Expressions
# 
# An expression is something that gives a value, and can be printed out. We will meet many expressions in this course! Here is a selection.

# In[1]:


# Values are expressions
print(10*2)
print('a')
# Function calls are expressions
print(print(10))
# List comprehensions are expressions
print([x*2 for x in range(2)])

