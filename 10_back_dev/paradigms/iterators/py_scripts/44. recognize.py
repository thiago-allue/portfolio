
# coding: utf-8

# # Choosing the best technique for the job
# 
# ## Common scenario: filtering and transforming elements from an iterator
# 
# Say that we have a list of movies between 2012 and 2015, all featuring Adam Sandler. Each movie is a tuple, consisting of a movie title and the movie's freshness rating on Rotten Tomatoes. We want to get all movie titles for which the freshness rating was 0.2 or higher.

# In[1]:


adam_sandler_movies = [
    ('Paul Blart: Mall Cop 2', 0.06),
    ('Blended', 0.14),
    ('Grown Ups 2', 0.07),
    ("That's My Boy", 0.2),
    ('Hotel Transylvania', 0.44)
]


# ### The traditional approach: using a `for` loop
# 
# The main advantage of a traditional `for` loop is that the syntax is familiar to most Python programmers, including novices. The main disadvantage is that it requires several lines of code to accomplish something simple.

# In[3]:


selected_titles = []
for title, freshness in adam_sandler_movies:
    if freshness < 0.2:
        continue
    selected_titles.append(title)
print(selected_titles)


# ### The Pythonic approach: using a `list` comprehension
# 
# A list comprehensions strikes a good balance between readability and conciseness. Not all Python programmers are familiar with list expressions, but because of the readable syntax, most Python programmers will be able to understand it.

# In[5]:


selected_titles = [title for title, freshness in adam_sandler_movies if freshness >= 0.2]
print(selected_titles)


# ### The functional approach: using `map()` and `filter()`
# 
# The `map()` and `filter()` functions are commonly used by programmers with a background in functional programming. So if they are your audience, you can use them. However, they are an aquired taste, and most people will find the list comprehension above easier to understand.

# In[8]:


selected_titles = map(
    lambda movie: movie[0],
    filter(lambda movie: movie[1] >= 0.2,
        adam_sandler_movies
    )
)
print(list(selected_titles))


# ## Common scenario: alternate two 'stateful' functions
# 
# Say that we want to simultaneously iterate through the Fibonacci and Tribonacci series.
# 
# ### The traditional approach: functions
# 
# When using functions, you need to somehow save the *state* of the functions, which is in this case is the Fibonacci or Tribonacci series that has been generated so far. You could do that in many ways, for example by passing the state as an argument to the functions.
# 
# The main advantage of this approach is that it is does not require any advanced programming techniques, that is, no generators. The main disadvantage is that the information flow from and to the functions can be difficult to follow.

# In[14]:


def fibonacci(*series):
    
    if len(series) < 2:
        return 1
    return sum(series[-2:])


def tribonacci(*series):
    
    if len(series) == 0:
        return 0
    if len(series) < 3:
        return 1
    return sum(series[-3:])


fibonacci_series = []
tribonacci_series = []
for i in range(10):
    f = fibonacci(*fibonacci_series)
    print('Fibonacci(%d)  = %d' % (i, f))
    fibonacci_series.append(f)
    t = tribonacci(*tribonacci_series)
    print('Tribonacci(%d) = %d' % (i, t))
    tribonacci_series.append(t)


# ### The Pythonic approach: generator coroutines
# 
# Generator coroutines allow you to suspend and resume functions. The main advantage of this approach is that the flow of the code is very clear. The main disadvantage is that not everyone is familiar with generators. In this case, the advantage of using generator coroutines probably outweighs the disadvantage.

# In[16]:


def fibonacci():
        
    yield 1
    yield 1
    l = [1, 1]
    while True:
        l.append(sum(l[-2:]))
        yield l[-1]
        

def tribonacci():

    yield 0
    yield 1
    yield 1
    l = [0, 1, 1]
    while True:
        l.append(sum(l[-3:]))
        yield l[-1]
        
        
for i, f, t in zip(range(10), fibonacci(), tribonacci()):
    print('Fibonacci(%d)  = %d' % (i, f))
    print('Tribonacci(%d) = %d' % (i, t))    

