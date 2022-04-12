
# coding: utf-8

# ## Exploring Generators
# 
# A Generator is a function with one or more `yield` statements. Each `yield` returns a value and suspends the Generator. When a suspended Generator is called again, it picks up where it left off.

# In[1]:


def my_generator():
    
    yield 'a'
    yield 'b'
    yield 'c'


# Because a Generator is an Iterator, they support `for` and `in`.

# In[4]:


print('d' in my_generator())


# You can also use `next()` to iterate through a Generator--after all, it is an Iterator!

# In[8]:


g = my_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# ## Sending information to a Generator
# 
# You can use `send()` to send information to a Generator. Inside the Generator, this will become the return value of `yield`. Because the Generator gives output before it receives input, the first `send()` must send `None`! The flow information between a Generator and the caller of the Generator can be tricky to follow.
# 
# Let's define a Generator that gives random replies until it receives 'Bye'.

# In[9]:


import random

SENTENCES = [
    'How are you?',
    'Fine, thank you!',
    'Nothing much',
    'Just chillin'
]


def random_conversation():
    
    recv = yield 'Hi'
    while recv != 'Bye!':
        recv = yield random.choice(SENTENCES)


# So how can we use this Generator?

# In[10]:


g = random_conversation()

print(g.send(None))
while True:
    try:
        reply = g.send(input())
    except StopIteration:
        break
    print('>>> ' + reply)
print('Conversation over!')

