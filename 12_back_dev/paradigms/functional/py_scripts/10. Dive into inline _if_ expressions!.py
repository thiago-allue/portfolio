
# coding: utf-8

# ## Conditional branching: The procedural way
# 
# Consider a simple, procedural implementation of a function that translates grade points (8) to grade descriptions ('good').

# In[1]:


def p_grade_description(gp):
    
    """Dutch grades range between 0 and 10"""
    
    if gp > 7:
        return 'good'
    if gp > 5:
        return 'sufficient'
    return 'insufficient'

p_grade_description(8)


# ## Conditional branching: The functional way
# 
# A functional implementation of `p_grade_description()` makese use of the `if` expression.

# In[6]:


(lambda gp: 'good' if gp > 7 else 'sufficient' if gp > 5 else 'insufficient')(6)


# ## Concise, readable code
# 
# You can use `if` expressions in procedural code as well to implement concise, readable conditions.

# In[8]:


gender_code = 1
gender = 'female' if gender_code else 'male'
print(gender)

