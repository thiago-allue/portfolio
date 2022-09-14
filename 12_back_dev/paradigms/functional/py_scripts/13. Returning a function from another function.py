
# coding: utf-8

# ## Four steps to baking a (pre-baked) croissant
# 
# In the weekend, I often eat pre-baked croissants for breakfast. To bake them, you need to perform four steps:

# In[1]:


preheat_oven = lambda: print('Preheating oven')
put_croissants_in = lambda: print('Putting croissants in')
wait_five_minutes = lambda: print('Waiting five minutes')
take_croissants_out = lambda: print('Take croissants out (and eat them!)')


# Now let's perform all these steps in order!

# In[2]:


preheat_oven()
put_croissants_in()
wait_five_minutes()
take_croissants_out()


# ## Passing all steps to a launcher function
# 
# Alternatively, we can create a launcher function (`peform_recipe()`) to which we pass all functions, and which then performs all these functions for us. This is, by itself, not very useful.

# In[3]:


def perform_steps(*functions):
    
    for function in functions:
        function()
        
        
perform_steps(preheat_oven,
    put_croissants_in,
    wait_five_minutes,
    take_croissants_out)


# ## Wrapping all steps into a single recipe
# 
# But we can go even further! We can create a `create_recipe()` function that takes all functions, and returns a new function that executes all the passed functions for us!

# In[5]:


def create_recipe(*functions):
    
    def run_all():
        
        for function in functions:
            function()
            
    return run_all


recipe = create_recipe(preheat_oven,
    put_croissants_in,
    wait_five_minutes,
    take_croissants_out)
recipe()

