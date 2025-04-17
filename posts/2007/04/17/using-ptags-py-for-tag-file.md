.. title: using ptags.py for tag file
.. slug: using-ptags-py-for-tag-file
.. date: 2007-04-17 20:25:00
.. tags: python, tools, ctags
.. category: Programming
.. description: How to use Python's ptags.py script to generate tag files for source code navigation

1. Place the `ptags.py` file in your `$PATH`.
2. From the project directory containing your Python project, run the following command:

```bash
find . -name "*.py" -print | xargs ptags.py
```
I was previously using various inefficient methods to achieve this.
