.. title: Who slides Wins
.. slug: who-slides-wins
.. date: 2017-02-15 09:22:07 UTC-08:00
.. tags: projects
.. category:
.. link:
.. description:
.. type: text

Few years ago, I wrote this {{% wikipedia article="15 puzzle" text="n-puzzle" %}} using {{% wikipedia article="Pygame" %}} for fun.  It was inspired from the
sliding block puzzle game that I had played as a kid, which had numerals in the front and
a picture of {{% wikipedia article="Taj Mahal" %}} in the back. The idea was to slide and fit the photo together.

https://github.com/orsenthil/who-slides-wins

**How to play**

1. Human plays first. Use Arrow Keys to Move and Fit the Picture.
2. Press Enter when Done.
3. Computer Plays and tries to beat you with less moves that you took.

It uses {{% wikipedia article="A* search algorithm" text="A*" %}} with {{% wikipedia article="Taxicab geometry" text="Manhattan Distances" %}} to Solve the puzzle.

If you want to try it on your computer.

1. Install {{% wikipedia article="Python (programming language)" text="python2.7" %}}
2. Create a {{% wikipedia article="Virtual environment" text="virtualenv" %}}.
3. pip install pygame
4. clone the git repo.
5. python run_game.py
