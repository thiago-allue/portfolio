
# coding: utf-8

# ## Two Generators in parallel
# 
# The simplest way to run two Generators in parallel is to `zip()` them together in a `for` loop.

# In[1]:


def fibonacci():
        
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]
        

def tribonacci():

    yield 0
    yield 1
    yield 1
    l = [0, 1, 1]
    while True:
        l = [l[-2], l[-1], sum(l[-3:])]
        yield l[-1]


for i, (f, t) in enumerate(zip(fibonacci(), tribonacci())):
    if i == 10:
        break
    print(f, t)


# ## Letting two Generators communicate
# 
# Let's consider a slightly more complicated example in which two Generators need to communicate with each other. The `speaker` returns random sentences. These are received by the `replier`, who aborts the conversation when the `speaker` has said 'Bye!' and otherwise replies with a random sentence.

# In[2]:



import random


SENTENCES = [
    'How are you?',
    'Fine, thank you!',
    'Nothing much',
    'Just chillin',
    'Bye!'
    ]


def speaker():
    
    while True:
        yield random.choice(SENTENCES)

        
def replier():
    
    while True:
        recv = yield
        print('Received: %s' % recv)
        if recv == 'Bye!':
            break
        print('Replied: %s' % random.choice(SENTENCES))
        
s = speaker()
r = replier()
r.send(None)
while True:
    recv = s.send(None)
    try:
        r.send(recv)
    except StopIteration:
        break

