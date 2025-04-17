.. title: Lambda functions
.. slug: lambda-functions
.. date: 2007-11-14 17:42:00
.. tags: python
.. category: General
.. description: 
.. categories: General
.. wp-status: publish

<html><body><p>I often forget the syntax and usage of lambda functions, the following examples should help as a reminder.



<code>

&gt;&gt;&gt; def function(x):

...     return x*3

... 

&gt;&gt;&gt; function(2)

6

&gt;&gt;&gt; func_with_lambda = lambda x: x*2

&gt;&gt;&gt; func_with_lambda(2)

4

&gt;&gt;&gt; (lambda x: x*2)(2)

4

&gt;&gt;&gt; 



</code></p></body></html>