.. title: Lambda functions
.. slug: lambda-functions
.. date: 2007-11-14 17:42:00
.. tags: python, lambda, functions
.. category: Python
.. description: Examples of lambda function syntax and usage in Python

I often forget the syntax and usage of lambda functions, the following examples should help as a reminder.

```python
>>> def function(x):
...     return x*3
...
>>> function(2)
6
>>> func_with_lambda = lambda x: x*2
>>> func_with_lambda(2)
4
>>> (lambda x: x*2)(2)
4
>>>
```
