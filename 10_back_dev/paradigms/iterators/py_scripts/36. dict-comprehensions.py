
# coding: utf-8

# ## Dict comprehensions: Basic syntax
# 
# - Basic syntax: `{key: value for key, value in iterable}`
# - The curly braces are necessary!
# 
# Let's first consider how you could create a `dict` that maps animal species onto their class. Ideally, we would like to Capitalize the strings!

# In[2]:


SPECIES = 'whale', 'grasshopper', 'lizard'
CLASS = 'mammal', 'insect', 'reptile'

d = {}
for species, class_ in zip(SPECIES, CLASS):
    d[species.capitalize()] = class_.capitalize()
print(d)


# Now let's implement this with a `dict` comprehension:

# In[4]:


d = {species.capitalize(): class_.capitalize() for species, class_ in zip(SPECIES, CLASS)}
print(d)


# ## Filtering dict comprehensions
# 
# - Filtering syntax: `{key: value for key, value in iterable if expression}`
# - This is an alternative (in many cases) to the continue statement
# 
# Let's say that we don't want to include insects! Without a `dict` comprehension, we might do this as follows:

# In[5]:


d = {}
for species, class_ in zip(SPECIES, CLASS):
    if class_ == 'insect':
        continue
    d[species.capitalize()] = class_.capitalize()
print(d)


# With a `dict` comprehension, this becomes:

# In[6]:


d = {
    species.capitalize(): class_.capitalize()
    for species, class_ in zip(SPECIES, CLASS)
    if class_ != 'insect'
}
print(d)

