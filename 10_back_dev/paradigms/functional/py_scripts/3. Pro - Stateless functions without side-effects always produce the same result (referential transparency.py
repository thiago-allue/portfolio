
# coding: utf-8

# # Stateless functions without side-effects always produce the same result
# 
# Or: *Referential transparency*
# 
# ## A stateful example
# 
# Using `global` variables in functions is one example of relying on, and modifying state.

# In[1]:


current_speaker = None


def register(name):
    
    global current_speaker
    current_speaker = name
    
    
def speak(text):
    
    print('[%s] %s' % (current_speaker, text))
    
    
register('John')
speak('Hello world!')
register('Carlos')
speak('Foobar!')


# ## Objects are also states
# 
# Objects are, by definition, states. Therefore, methods (object functions) are stateful.

# In[2]:


class Speaker():
    
    def __init__(self, name):
        
        self._name = name
        
    def speak(self, text):
        
        print('[%s] %s' % (self._name, text))
        

john = Speaker('John')
john.speak('Hello world!')
carlos = Speaker('Carlos')
carlos.speak('Foobar!')


# ## Stateless functions are often trivial
# 
# A stateless function relies only on:
# 
# - The arguments that have been passed to the function
# - Return values from other (stateless) functions
# 
# The result is often a very simple function. But when was simplicity ever a bad thing?

# In[3]:


def speak(speaker, text):
    
    print('[%s] %s' % (speaker, text))
    

john = 'John'
speak(john, 'Hello world!')
carlos = 'Carlos'
speak(carlos, 'Foobar!')

