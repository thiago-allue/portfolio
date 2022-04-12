
# coding: utf-8

# # Built-in functions for working with iterators
# 
# These functions are always available. You don't need to import them.
# 
# ## `zip()`: linking elements from multiple iterators
# 
# Without `zip()`:

# In[1]:


species_list = ['Whale', 'Lizard', 'Ant']
class_list = ['Mammal', 'Reptile', 'Insect']
cuteness_list = [3, 2, 1, 0]

for i in range(len(species_list)):
    species = species_list[i]
    class_ = class_list[i]
    print('%s is a %s' % (species, class_))


# With `zip()`:

# In[3]:


for species, class_, cuteness in zip(species_list, class_list, cuteness_list):
    print('%s is a %s and has a cuteness rating of %d' % (species, class_, cuteness))


# ## map(): applying a function to each element from an iterator
# 
# The first argument is a function. The second argument is an iterator. The function should take an element as a single argument.

# In[4]:


from math import sqrt
fibonacci = [1,1,2,3,5,8]
for i in map(sqrt, fibonacci):
    print(i)


# An equivalent generator expresssion:

# In[5]:


for i in (sqrt(j) for j in fibonacci):
    print(i)


# ## enumerate(): getting indices along with elements

# Without `enumerate()`:

# In[6]:


i = 0
for species in species_list:
    print(i, species)
    i += 1


# With `enumerate()`:

# In[7]:


for i, species in enumerate(species_list):
    print(i, species)


# An equivalent generator expression:

# In[9]:


for i, species in ((i, species_list[i]) for i in range(len(species_list))):
    print(i, species)


# ## filter(): excluding elements

# Without `filter()`:

# In[11]:


for i in fibonacci:
    if i%2:
        continue
    print(i)


# With `filter()`:

# In[12]:


for i in filter(lambda i: not i%2, fibonacci):
    print(i)


# An equivalent generator expression:

# In[13]:


for i in (j for j in fibonacci if not j%2):
    print(i)

