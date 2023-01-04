
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap


# Applying decorator to a lambda
print((trace(lambda x: x + 2))(3))


# The lambda is decorated with trace()
# The first argument of map() is a lambda that multiplies its argument by 2
print(list(map(trace(lambda x: x * 2), range(3))))
"""
Outputs:
[TRACE] func: <lambda>, args: (0,), kwargs: {}
[TRACE] func: <lambda>, args: (1,), kwargs: {}
[TRACE] func: <lambda>, args: (2,), kwargs: {}
[0, 2, 4]
"""