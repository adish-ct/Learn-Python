"""
In Python, the generator is a way that specifies how to implement iterators. It is a normal 
function except that it yields expression in the function. It does not implement __itr__ and next() 
method and reduces other overheads as well.

If a function contains at least a yield statement, it becomes a generator. The yield keyword 
pauses the current execution by saving its states and then resumes from the same when required.

"""


def generator():
    li = [1, 2, 3, 4, 5, 6]

    for i in li:
        yield i

value = generator()
print(value.__next__())
print(value.__next__())