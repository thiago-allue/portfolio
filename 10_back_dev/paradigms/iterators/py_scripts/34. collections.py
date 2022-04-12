
# coding: utf-8

# ## `collections.namedtuple`
# 
# `namedtuple()` is a factory function; that is, it generates a class, and not an instance of a class (an object).
# 
# So there are two steps:
# 
# 1. First, use `namedtuple()` to generate a `class`
# 2. And then create an instance of this `class`

# In[4]:


from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
jay_z = Person(name='Sean Carter', age=47)
print('%s is %s years old' % (jay_z.name, jay_z.age))


# ## `collections.OrderedDict`
# 
# If your code requires that the order of elements in a `dict` is preserved, use `OrderedDict`—even if your version of Python (e.g. CPython 3.6) already does this!
# 
# Otherwise, `OrderedDict` behaves exactly like a regular `dict`.

# In[5]:


from collections import OrderedDict

d = OrderedDict([
    ('Lizard', 'Reptile'),
    ('Whale', 'Mammal')
])

for species, class_ in d.items():
    print('%s is a %s' % (species, class_))


# ## collections.defaultdict
# 
# Use `defaultdict` if you want non-existing keys to return a default value, rather than raise a `KeyError`.
# 
# Otherwise, `OrderedDict` behaves exactly like a regular `dict`.

# In[11]:


from collections import defaultdict

favorite_programming_languages = {
    'Claire' : 'Assembler',
    'John' : 'Ruby',
    'Sarah' : 'JavaScript'
}

d = defaultdict(lambda: 'Python')
d.update(favorite_programming_languages)
print(d['John'])

