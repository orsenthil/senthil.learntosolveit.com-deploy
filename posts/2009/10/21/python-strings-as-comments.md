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


----


But docstrings are something else



You would need to add specific options to python to stop it from byte-compiling docstrings though.

_Anonymous_

----


Re: But docstrings are something else



Sorry, for the late reply, I myself had do some experimentations to understand this stuff. In the above snippet as you saw, the compiler discards any string which is not referenced. But it is still available as a __doc__ attribute of the test object.



&gt;&gt;&gt; def test():











&gt;&gt;&gt; import dis



&gt;&gt;&gt; dis.dis(test)



3           0 LOAD_CONST               1 (1)



3 STORE_FAST               0 (x)



4           6 LOAD_FAST                0 (x)



9 RETURN_VALUE



&gt;&gt;&gt; print test.__doc__



This is string



&gt;&gt;&gt;



But create a python snippet 'foo.py' like this:



def test():



"""This is a docstring"""



print test.__doc__



return True



test()



and do python foo.py vs python -OO foo.py you will see the .__doc__ attribute itself is discarded while doing optimization using -OO.

_Senthil_