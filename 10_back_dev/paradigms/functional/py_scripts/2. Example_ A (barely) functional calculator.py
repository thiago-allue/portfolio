
# coding: utf-8

# ## A procedural approach!
# 
# - Functions generally consist of multiple statements
#   - Assignments
#   - If-statements
#   - While loops
#   - Etc.

# In[2]:


OPERATORS = '+', '-', '*', '/'


def p_main():
    
    """The main flow."""

    print('Welcome to the barely functional calculator!')
    number1 = p_get_number()
    operator = p_get_operator()
    number2 = p_get_number()
    result = p_calculate(number1, operator, number2)
    print('The result is: %s' % result)


def p_get_number():
    
    """Reads an integer from the standard input and returns it.
    If a non-integer value is entered, a warning is printed,
    and a new value is read."""
            
    while True:
        s = input('Enter an integer: ')
        try:
            return int(s)
        except ValueError:
            print('That is not an integer!')
            

def p_get_operator():
    
    """Reads an operator from the standard input and returns it.
    Valid operators are: +, -, *, and /. If an invalid operator
    is entered, a warning is printed, and a new value is read."""    
    
    while True:
        s = input('Enter an operator (+, -, *, or /): ')
        if s in OPERATORS:
            return s
        print('That is not an operator!')
            
            
def p_calculate(number1, operator, number2):
    
    """Performs a calculation with two numbers and an operator,
    and returns the result."""
    
    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '/':
        return number1 / number2
    raise Exception('Invalid operator!')

    
p_main()


# ## A functional approach!
# 
# - Functions consist of only one expression
# - How can we validate input? (One of the many things we will learn later!)

# In[1]:


OPERATORS = '+', '-', '*', '/'


def f_get_number():
    return int(input('Enter an integer: '))


def f_get_operator():
    return input('Enter an operator (+, -, *, /): ')


def f_calculate(number1, operator, number2):
    return number1+number2 if operator == '+'         else number1-number2 if operator == '-'         else number1/number2 if operator == '/'         else number1*number2 if operator == '*'         else None    


def f_main():
    return f_calculate(
        f_get_number(),
        f_get_operator(),
        f_get_number(),
        )


print('The result is: %s' % f_main())

