.. title: Annoucement- pyljvim-0.0.3 Released.
.. slug: annoucement-pyljvim-0-0-3-released
.. date: 2006-12-03 05:18:00
.. tags: 
.. category: General
.. description: 
.. categories: General
.. wp-status: publish

pyljvim is a LiveJournal plugin for Vim. With this plugin, you can post to
LiveJournal directly from Vim! :)

In fact, I am posting this entry from Vim.

You can find it here: [pyljvim on Vim.org](http://www.vim.org/scripts/script.php?script_id=1724)

Installation is straightforward, and the usage is simple as well.

Thanks,
Senthil

> "Contemptuous lights flashed across the computer's console."
> -- *The Hitchhiker's Guide to the Galaxy*

----

**Comments**

Very interesting way to use Vim, very nice. ;) As I can understand, Python must
be installed (on Windows, of course)? Well, I think I'll try it.
Thanks and good luck.

Interesting, but would it be possible to preview before submitting an entry?

Thanks. Yes Python must be installed on windows to work. This version relies on
python to do the posting, but I would like to convert it to vim scripting itself
so that vim should be enough.  btw, support for unicode is also poor in this
version.I would like to add the unicode support in the next release.  The intial
release had a bug, where I stored my credentials in the file and zipped it, I
have uploaded a new one and it works fine. :-)

hmm.. preview as in converted to html? Nope, It is not possible.
I did not feel the need for it, but as you say, instead of preview ( I never
preview!) but verifying the syntax be a good thing to TODO? What do you say?

Nice to hear about the native Vim scripting instead of Python. I don't mean that
using of Python is the wrong way, but the Vim scripting might be much better in
this case. :-) Well, support for Unicode might be useful too. But it's not an
urgent matter. Maybe it would be more pleasant to use the usual 'iconv' for text
converting (with 'on-the-fly' converting, too), or not?  Another question is
this — the saving of the user's drafts. For example, one have wrote some stuff
and have not published it. What about the draft, whether it's stored in the
one's home directory or elsewhere?

Nice work saar!

I thought about the Draft thing. It is not yet present.  It currently saves the
entry with a temporary filename in the TEMP folder. One can retrieve it he
remembers the name of the file,but is not implemented as a feature yet.

Thanks for your feedback.

thanks sajith. :) Time for lispljemacs? btw, I did not completely write it from
scratch, 0.0.1 was implemented by <a href="http://www.vim.org/scripts/script.php?script_id=584" rel="nofollow">
Wartan Hachturow</a> and I took the maintainer ship from from and enhanced it
further. Hope to make it more usable.

Well, there is <a href="http://edward.oconnor.cx/ljupdate/" rel="nofollow">ljupdate</a> - I often use that.

blogger and vim
BTW I am planning something like what you have done for lj with blogger. Blogger and vim :)
//Navtej

Re: Barcamp Presentation
Hi Navtej, I didn't know that Barcamps are usually for webbased stuffs. I
thought it was just a hacker meet, to share things and show 'their cool stuff'.
The thoughtworks pulled lot of webbased talks only.

You know what, pyljvim pulled only one person :-) as it was the last
presentation of the whole camp. I just went ahead explaining the details to him.

was quite amused at the the topic and took some snaps, got to see if he has
uploaded any.  Yeah, looking forward to the mini pycon.
Hoping to python talks on topics other than web technologies.
c u there,Navtej.

Re: blogger and vim
yeah,that would be a good idea too. Just see if there if Blogger provides an
interface for clients. Rest should be workable.

But, why not move to livejournal itself Navtej? positives are: comment
notification( which I requested in blogger number of times,but it did not come
up till I moved) and other positive things of open source software.

LJ's community and friends feature is its backbone (IMO).