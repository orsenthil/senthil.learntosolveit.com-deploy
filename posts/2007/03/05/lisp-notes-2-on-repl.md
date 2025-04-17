---
title: "Lisp Notes -2. On REPL"
slug: lisp-notes-2-on-repl
date: 2007-03-05 09:39:00
tags: ai, lisp, pcl, repl, emacs
category: Programming
description: Notes on Common Lisp's REPL (Read-Eval-Print Loop) environment and using it with Emacs, from the book "Practical Common Lisp."
---

Subsequent to [Lisp Notes 1](http://phoe6.livejournal.com/46112.html), these are my notes for the Chapter 2 "Lather, Rinse, Repeat: A Tour of the REPL" in the [Practical Common Lisp Book](http://www.gigamonkeys.com/book/index.html)

* Lisp provides an interactive read-eval-print loop.

* Lisp can be used in Automated Theorem proving, planning and scheduling and computer vision. Large scale battlefield simulation, automated planning and natural language interfaces.

* Help in EMACS, Press CTRL Key, type h, release CTRL key and press t. This key combination called key-chord is represented like this. C-t h

* Info system is available by `C-h i`

* `C-h ?` brings complete list.

* `C-h k` lets us type any key combination and lets us know the command which will be invoked.

* `C-h w` lets us enter the command and returns the corresponding key combination.

<!--more-->

Crucial bit of emacs terminology is a Buffer. While working with EMACS, each file you edit will be represented by a different buffer, only one of which is current in any way.

**Buffers:**

* `C-x b` is command to switch to buffer.

Some key combinations may be available for switches to certain buffer.

For e.g. to switch to lisp source file.

* `C-c C-z` switch to buffer where you interact with lisp (REPL)

```
CL-USER>
```

This is the lisp command prompt. Lisp reads the lines of lisp expressions evaluates them according to the rules of lisp and prints the result.

The endless cycle of reading, evaluating and printing is why it is called read-eval-print loop or REPL for short.

It's also referred to as top level, top level listener, lisp listener.

From REPL we can:
- Define or redefine variables, functions, classes and methods.
- Evaluate any lisp expression.
- Load files containing lisp source code or compiled code.
- Compile other files or individual functions.
- Enter Debugger.
- Step through the code.
- Inspect the state of the individual lisp command.

```lisp
CL-USER>10
10
```

R - Reads "10" and converts to lisp object "10"
E - Evaluates to itself.
P - Prints "10"

```lisp
CL-USER>(+ 2 3)
5
```

`+` symbol is converted to `+` function which takes 2 and 3 as parameters.

```lisp
CL-USER>"hello,world"
"hello,world"
```

That was a "hello,world" value.

**Format function:**

Format takes a variable number of arguments, but the only two required to send the output a string.

```lisp
CL-USER>(format t "hello,world")
"hello,world"
NIL
```

* `t` sends the output to stdout.
* `NIL` is the return value of the function.

```lisp
CL-USER>(defun hello-world() (format t "hello,world"))
HELLO-WORLD
CL-USER>(hello-world)
hello,world
NIL
```

**Saving the file:**

* `C-x C-f` type the file name with extension as .lisp or .cl

* Inside the SLIME mode, `C-c C-q` invokes the command `slime-close-parens-at-point` which will insert as many closing parenthesis as necessary to match all the open parenthesis.

* To get the source file to lisp environment:
     * `C-c C-c` (slime-compile-defun)

     Or switch the REPL Buffer:
     * `C-c C-z` (directly from SLIME to REPL)

     Or
     * `C-x b` and all the buffer.

Make some changes and type again.

```lisp
(defun hello-world()
        (format t "Hello,World!"))
```

* `C-c C-c`

Or

* `C-c C-z`

```lisp
(hello,world)
Hello,World!
NIL
```

Save the changes to hello.lisp by typing `C-x C-s` in EMACS which invokes (save-buffer)

Exit SLIME, which is in REPL type ',' - a comma.

Invoke again:

```
M-x slime
CL-USER>(hello-world)
```

Will not get invoked because REPL is not aware and it will put you in the debugger mode. Pressing 'q' will exit the debugger.

```lisp
CL-USER>(hello-world)
;Evaluation aborted
CL-USER>
```

**Letting the REPL Know:**

1) `C-x b hello.lisp` and then compiling using `C-c C-c`

2) Load the whole file:

```lisp
(load "hello.lisp")
; Loading file
T
```

T- means loaded correctly.
FASL - Fast Load file

```lisp
(load(compile-file("hello.lisp"))
```

From the SLIME environment itself, the following features are available:

* `C-c C-l` (slime-load-file)
* `C-c C-k` to compile and load the file represented by the current buffer.
