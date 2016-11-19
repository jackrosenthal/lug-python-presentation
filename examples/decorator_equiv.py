@logging
def foo(bar, baz):
    return bar + baz - 42

# equivalent to...
def foo(bar, baz):
    return bar + baz - 42
foo = logging(foo)
