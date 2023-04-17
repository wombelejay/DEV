
.. index::
   Idle; execution of editor file
   execution; Idle edit window
   editor; Idle

.. _The-Idle-Editor:

The Idle Editor and Execution
=============================

.. index:: loading a program in Idle
   Idle; loading a program

.. _Loading-a-Program:

Loading a Program in the Idle Editor, and Running It
----------------------------------------------------

It is time to put longer collections of instructions together. That
is most easily done by creating a text file and running the Python
interpreter on the file. Idle simplifies that process.

First you can put an existing file into an Idle Edit Window. Start with 
the sample program madlib.py.  If you have not downloaded it yet, see
:ref:`Your-Python-Folder`. 

Assuming you are already in Idle from the previous sections, 
you can open a file from there:

-   Click on the Idle :guilabel:`File` menu and select :guilabel:`Open`.
    (Or as you see, you can use
    the shortcut :kbd:`Ctrl-O`. 
    That means holding down the :kbd:`Ctrl` key, and
    pressing the letter :kbd:`O` for Open.) You should get a file selection
    dialog. 
-   You need to navigate to the folder with the file you want.  
    If you already had a file open, 
    and its window has the foreground focus when you make access the File menu, 
    then the folder that opens is the same as the folder from
    which the current file came.  

    If the Shell Window has the foreground focus, 
    then the folder opened depends on the operating system:

    *  Windows: 
       At least through Python 3.7,
       Windows is likely to open a buried system folder 
       that you *do not want to mess with*!  
       Switch to your Desktop or Documents, and find the right folder from there.  
       Hopefully the behaviour will be more like on a Mac in future
       version.

    *  Mac and Linux: A reasonable folder opens: Documents. 
       Navigate from there.
    
    **Hence it is important to set the focus on an Edit window to have
    the same folder appear when opening a new file.**

 -  Select the file you want. (The initial suggestion was madlib.py.)


.. index::
   double: Idle; running a program
   shell; running a program

You will see the source code again. Now run this program from
inside of Idle: Go to the :guilabel:`Run` menu of that Edit window, and select
:guilabel:`Run Module`. Notice the shortcut (F5) also available.

If the Shell window does not automatically come to the foreground,
select it. You should see a line saying ``RESTART`` and then the
start of the execution of the Mad Lib program with the cursor
waiting for your entry after the first prompt. Finish executing the
program. Be sure to type the final requested Enter, so you get back
to the interpreter prompt: ``>>>``

Look at the editor window again. You should see that different
parts of the code have different colors. String literals are likely
green. The reserved word ``def`` is likely orange. Look at the
last two lines, where the identifier ``tellStory`` is black, and
the identifier ``input`` is likely purple. Only identifiers that
are *not* predefined by Python are black. If *you* create an
identifier name, make sure Idle shows it in *black*.

.. index::
   Idle; bug running a Python 3.2 program

.. _idle-for-editing:

Starting Idle for Editing 
--------------------------------------------------------

You are strongly suggested to keep the programs you write in the given
examples folder along with all the examples provided to you.
You can always easily see the files you created, all together, by
sorting by creation date.  You are likely to create
new programs derived from some of the given examples, and
some earlier programs of your own.  Everything is easy to access
if you keep them together.  

The way I recommended to start Idle to work on this tutorial is 
to start by opening it on a file in the folder where you want to work, 
either a file you want to further edit, a related file you want to modify,
or just any Python file in the same folder if you want to start from scratch.

To open Idle with an initial file to edit,
select the Python file in an operating system window,
right click (Windows) or control-click (Mac),
to get a pop-up window to select how to open the file.
On Windows, the line for Idle requires you to open a sub-menu.
Select Idle for the latest version.

Opening Idle without a file reference, 
directly from the operating system, 
makes the associated folder
for opening and saving files be the same *wrong* one as
described in the previous section from inside Idle, 
when the Shell Window has foreground focus.

Alternate approaches to starting Idle
are discussed in the operating specific appendix sections.


.. index::
   double: running a program; Hello world

.. _The-Classic-First:

The Classic First Program
-------------------------

Have Idle started as in the previous section,
so some Python file has the foreground focus.

Open a new window by going to the
:menuselection:`File` menu and selecting :menuselection:`New File`. 
This gives you a rather
conventional text editing window with the mouse available, ability
to cut and paste, plus a few special options for Python.

Type (or paste) the following into the *editor* window (not the Shell Window)::

    print('Hello world!')

.. index:: save in Idle
   Idle; save

Save the file with the menu sequence :menuselection:`File --> Save`,
and then enter the file
name ``hello.py``. Python program files should always be given a
name ending in ".py".  If you give no extension, ".py" is assumed.
You can also enter it explicitly.
   
There are also the options :menuselection:`File --> Save As` and
:menuselection:`File --> Save Copy As`.  Both
save a copy to a different name, but only
:menuselection:`File --> Save As` changes the name of
the file you are editing in Idle.

.. warning::
   It is the contents of the foreground Idle window that get saved.
   You are unlikely to mean to save the contents of the Shell
   window, but it is easy for that window to have the focus
   when you mean to save a program in an edit window.  

**Syntax coloring**: If you look in the editor, you should see that your text is color
coded. The editor will color different parts of Python syntax in
special colors. 

Now that you have a complete, saved program, choose
:menuselection:`Run --> Run Module`.
You should see the program run in the Python Shell window.

You just wrote and executed a program. Unlike when you use the
shell, this code is saved to a file in your Python folder. You can
open and execute the file any time you want. (In Idle, use
:menuselection:`File --> Open`.)

.. index::
   module
   file; Python module

To the interpreter, a program source file is a Python
*module*. We will tend to use the more general term: a program file
is a module. Note the term from the menu when running the program.

.. index:: shell; confusion with Edit Window

*Distinguish program code from Shell text*: It is easy to confuse
the Shell and the Edit windows. Make sure you keep them straight.
The hello.py program is just the line ::

    print('Hello world!')

that you typed into the edit window and saved. When you ran the
program in Idle, you saw results in the Shell. First came the
Restart notice, the one-line output from the program saying hello,
and a further Shell prompt::

    >>> ================================ RESTART ========
    >>> 
    Hello world!
    >>>

You could also have typed this single printing line directly in the
Shell in response to a Shell prompt. When you see
``>>>``, you could enter the
print function and get the exchange between you and the Shell::

    >>> print('Hello world')
    Hello world!
    >>>

..  warning::

    The three lines above are *not* a program you could save in a file
    and run. This is just an exchange in the *Shell*, with its
    ``>>>`` prompts, individual
    line to execute, and the response. 

    Again, just the single line, with
    no ``>>>``, ::

        print('Hello world!') 

    entered into the *Edit* window forms a program you can save and
    run. The ``>>>`` prompts have no place in a Python program file.

We will shortly get to more interesting many-statement
programs, where it is much more convenient to use the Edit window
than the Shell!

*The general assumption in this Tutorial will be that programs are*
*run in Idle and the Idle Shell is the Shell referred to.*
It will be explicitly stated when you should run a program directly
from the operating system.   

In general it is also fine to run our programs
from a cmd console (Windows) or terminal (Mac) 
or from a different development environment.   

.. warning::

   Running the text based example programs in Windows, like birthday2.py,
   by selecting them to run from a file folder, will *not* work well:  
   The program ends and the window automatically closes before you can
   see the final output.  
   
On a Mac you get to explicitly close the verbose terminal window 
created when you run a Python
program from the Finder.


.. index::
   single: documentation string; program

.. _Program-Documentation-String:

Program Documentation String
----------------------------

The hello program above is self evident, and shows how short and direct a
program can be (unlike other languages such as Java). Still, right
away, get used to documenting a program. Python has a special
feature: If the beginning of a program is just a quoted string,
that string is taken to be the program's *documentation string*.
Open the example file ``hello2.py`` in the Edit window:

.. literalinclude:: ../examples/hello2.py

Most commonly, the initial documentation goes on for several lines,
so a multi-line string delimiter is used (the triple quotes). Just
for completeness of illustration in this program, another form of
comment is also shown, a comment that starts with the symbol ``#`` and
extends to the end of the line. The Python interpreter completely
ignores this form of comment. Such a comment should only be
included for better human understanding. Avoid making comments that
do not really aid human understanding. (Do what I say, not what I
did above.) Good introductory comment strings and appropriate names
for the parts of your programs make fewer ``#`` symbol comments
needed!

Run the program and see the documentation and comment make no
difference in the result.

.. index::
   screen layout and Alt-2 resize
   Idle; Alt-2 resize
   Alt-2 Idle window resize

Screen Layout
-------------

Of course you can arrange the windows on your computer screen any
way that you like. A suggestion is to display the combination
of the editor to write, the shell to run, and the tutorial to
follow along. 

There is an alternative to maximization for the Idle editor window:
It you want it to go top to bottom of the screen but not widen, you
can toggle that state with 
:menuselection:`Options -> Zoom Height` or the keyboard shortcut
shown beside it.


