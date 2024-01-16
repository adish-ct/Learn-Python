# eval

""" eval is a built-in Python function that allows you to evaluate a dynamically created Python expression or statement.    """

a = '5 + 3'
print(eval(a))

# 8 - output


b = '(5 * 2) + (20 * 10)'
print(eval(b))

# 210 - output


x = 5
y = 10
code = 'x + y'

result = eval(code)
print(result)

# 15