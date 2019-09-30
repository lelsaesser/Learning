def example(*, a, b):
    pass

example(a="hello", b="world") # this call works
# example("hello", "world") # this call would fail: TypeError: example() takes 0 positional arguments but 2 were given


# only arguments after * are kwargs
def example_two(a, b, *, c, d):
    pass

example_two("value1", "value2", c="hello", d="world")