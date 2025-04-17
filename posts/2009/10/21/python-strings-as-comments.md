.. title: Python Strings as Comments
.. slug: python-strings-as-comments
.. date: 2009-10-21 06:29:00
.. tags: python, strings, comments
.. category: Programming
.. description: How Python discards string literals that are not assigned, allowing them to function as comments

The question was:

In Python we can emulate multiline comments using triple-quoted
strings, but conceptually strings and comments are very different.
I.e. strings are objects, comments are auxillary text discarded at
compile time. Strings are objects created at runtime, comments are
not.

The answer from Steven D'Aprano:

Guido's time-machine strikes again.

```python
>>> import dis
>>> def test():
...     x = 1
...     """
...     This is a triple-quote comment.
...     """
...     return x
...
>>> dis.dis(test)
  2           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (x)

  6           6 LOAD_FAST                0 (x)
              9 RETURN_VALUE
```

String literals -- not just triple-quoted strings, but any string
literal -- that don't go anywhere are discarded by the Python compiler,
precisely so they can be used as comments.
