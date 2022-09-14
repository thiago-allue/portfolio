
# coding: utf-8

# # Con: Functional programming doesn't (always) match how humans think
# 
# ## Consider voting
# 
# Political voting has at least two actors: the voter and the politician. Voting is an action of the voter; we don't think of being voting upong as an action of the politician. The politician that was voted upon is a property of the voter. The number of votes received is a property of the politician.
# 
# This logic can be beautifully encapsulated by object-oriented programming
# 
# 
# ## An object-oriented approach

# In[1]:


class Voter:
    
    def __init__(self, name):
        
        self.name = name
        self.voted_for = None
        
    def vote(self, politician):
        
        self.voted_for = politician
        politician.votes += 1
        
    def __str__(self):
        
        return self.name        
        
        
class Politician:
    
    def __init__(self, name):
        
        self.name = name
        self.votes = 0
        
    def __str__(self):
        
        return self.name
        

macron = Politician('Macron')
jean = Voter('Jean')
jean.vote(macron)
print('%s voted for %s' % (jean, jean.voted_for))
print('%s received %d vote(s)' % (macron, macron.votes))


# ## A functional approach
# 
# We can implement the same logic using purely functional programming. But the result is clunky, and less intuitive then the object oriented counterpart.

# In[2]:


def vote(voters, politicians, voter, politician):
    
    voters[voter] = politician
    if politician in politicians:
        politicians[politician] += 1
    else:
        politicians[politician] = 1
    return voters, politicians


def voted_for(voters, voter):
    
    return '%s voted for %s' % (voter, voters.get(voter, None))


def votes(politicians, politician):
    
    return '%s received %d vote(s)' % (politician, politicians.get(politician, 0))


voters, politicians = vote({}, {}, 'Jean', 'Macron')
print(voted_for(voters, 'Jean'))
print(votes(politicians, 'Macron'))

