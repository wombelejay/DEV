
The Python Interpreter and Idle, Part I
=======================================

.. index::
   folder for Python examples

.. _Your-Python-Folder:

   
Your Python Folder and Python Examples
--------------------------------------------------------------

First you need to set up a location to store your work and the
example programs from this tutorial. You can put
the folder for your Python programs most anywhere you like. However, for
Chapter 4, it will be important that *none of the directories*
*leading down to your Python folder contain any blanks in them*, in
particular your home folder. 

The normal place for you to have my examples folder is under your home folder, 
which has the same name as your Login ID. If you are just creating a login ID, 
it will save some hassle in Chapter 4, if your login ID does 
*not have a space in it*.
"Andy" or "anh" or AndyHarrington" would be fine for me, but  

   "Andy Harrington" 
   
would bomb the server in Chapter 4.
It is possible to do Chapter 4 with a folder outside your home folder,
as discussed at the beginning of Chapter 4.

.. _examples-folder:

Folder For My Examples
-----------------------

Download and save
http://anh.cs.luc.edu/python/hands-on/3.1/examples.zip. 

Note that the examples, like this version of the tutorial,
are for Python 3. There were major changes to Python in version
3.0, making it incompatible with earlier versions.

If you are using Python version 2.7 for some good reason, you should continue
with the older version of the tutorial. Go to
http://anh.cs.luc.edu/python/hands-on and find the links to the
proper version of the tutorial and examples.

Once you have the examples.zip archive, you need to extract the files. Make a file
browser window set to the directory where you put the zip file. Then:

Windows
	Right click on examples.zip, select Extract All. This
	will create the folder ``examples``. End up with a file browser
	window showing the contents of the examples folder. This will be
	your *Python folder* in later discussion.

Mac
	Double click on the zip file and the expanded examples folder appears.

.. index::
   zip file - can't edit 

.. warning::
    On Windows, files in a zip archive can be viewed while
    they are still in the zip archive. Modifying and adding files is
    not so transparent. Be sure that you *unzip the archive* and 
    *work from the regular directory* that holds the resulting unzipped
    files.


You also have the option of downloading

-  An archive containing the web version of the tutorial
   http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml.zip for local
   viewing, without the Internet. Download it and unzip as with the
   examples. The local file to open in your browser in in the ``handsonHtml``
   folder you unzipped and the main web page file to open is called
   ``index.html``.

-  The PDF version of the tutorial for printing
   http://anh.cs.luc.edu/python/hands-on/3.1/Hands-onPythonTutorial.pdf.
   Some people also like the typography of this version on the web, too.
   It is hyperlinked like html version.
   
.. index::
   example program; mad lib
   mad lib; first example program 

.. _Running-A-Sample:
    
Running A Sample Program
------------------------

This section assumes Python 3 is already on
your computer. Windows does not come with Python. (To load Python
see :ref:`getPython`.) 

Before getting to the individual details of Python, you will run a
simple text-based sample program. Find ``madlib.py`` in your Python
folder, set up in :ref:`Your-Python-Folder`.

.. note::
    Different keyboards label the key for ending a line differently:
    Windows keyboards may use :kbd:`Enter` while Mac keyboards use :kbd:`Return`.
    The tutorial may intermix instructions to press :kbd:`Enter` or 
    press :kbd:`Return`.
    They both are intended to mean the key for ending a line.

Options for running the program:

-  If you have trouble with the following options, opening the program
   in Idle is discussed in :ref:`Starting-Idle`. 

-  In Windows, you can display your folder contents, and double
   click on madlib.py to start the program.

-  On a Mac, you can Control-click on madlib.py in the Finder, select Open With,
   and choose the Python Launcher for your Python 3 version.  When you are done with 
   the program, close the terminal window.
   
-  In Linux you may be able to open a terminal window,
   change into your Python examples directory, and enter the command ::

     python madlib.py

   or
   possibly to distinguish Python 2 and 3::

     python3 madlib.py
     
   If neither of these work, get help.
   
Try the program a second time and make different responses.

.. match ]]

.. _Madlib-Explained-I:
    
A Sample Program, Explained
---------------------------------------------------

If you want to get right to the detailed explanations of writing
your own Python, you can *skip to the next section*
:ref:`Starting-Idle`. If you would like an overview of a working
program, even if all the explanations do not make total sense yet,
read on.

Here is the text of the madlib.py program, followed by line-by-line
brief explanations. Do not worry if you not totally understand the
explanations! Try to get the gist now and the details later. The
numbers on the right are not part of the program file. They are
added for reference in the comments below::

    #! /usr/bin/env python3                                  0
    '''                                                      1 
    String Substitution for a Mad Lib                        2 
    Adapted from code by Kirby Urner                         3 
    '''                                                      4 
                                                             5 
    storyFormat = '''                                        6 
    Once upon a time, deep in an ancient jungle,             7 
    there lived a {animal}.  This {animal}                   8 
    liked to eat {food}, but the jungle had                  9 
    very little {food} to offer.  One day, an               10 
    explorer found the {animal} and discovered              11 
    it liked {food}.  The explorer took the                 12 
    {animal} back to {city}, where it could                 13 
    eat as much {food} as it wanted.  However,              14 
    the {animal} became homesick, so the                    15 
    explorer brought it back to the jungle,                 16 
    leaving a large supply of {food}.                       17 
                                                            18 
    The End                                                 19 
    '''                                                     20 
                                                            21  
    def tellStory():                                        22 
        userPicks = dict()                                  23 
        addPick('animal', userPicks)                        24 
        addPick('food', userPicks)                          25 
        addPick('city', userPicks)                          26 
        story = storyFormat.format(**userPicks)             27 
        print(story)                                        28 
                                                            29 
    def addPick(cue, dictionary):                           30 
        '''Prompt for a user response using the cue string, 31 
        and place the cue-response pair in the dictionary.  32 
        '''                                                 33 
        prompt = 'Enter an example for ' + cue + ': '       34 
        response = input(prompt)                            35 
        dictionary[cue] = response                          36 
                                                            37 
    tellStory()                                             38 
    input('Press Enter to end the program.')                39 


Line By Line Explanation ::

    #! /usr/bin/env python3                                  0

This is not technically a part of the program.  
It is there to tell the operating system what version of Python
to choose, since the older Python 2 is incompatible with the
newer Python 3.  We will mostly run programs from inside 
the Idle programming environment, where this line is not needed.
To run just by clicking on the program
in an operating system window, however, 
the line is important if your computer also has Python 2.  ::

    '''                                                      1 
    String Substitution for a Mad Lib                        2 
    Adapted from code by Kirby Urner                         3 
    '''                                                      4 


1-4: There is multi-line text enclosed in triple quotes. Quoted
text is called a *string*. A string at the very beginning of a program
like this is *documentation* for the file.

5,21,29,37: Blank lines are included for human readability to
separate logical parts. The computer ignores the blank lines. ::

    storyFormat = '''                                        6 
    Once upon a time, deep in an ancient jungle,             7 
    there lived a {animal}.  This {animal}                   8 
    liked to eat {food}, but the jungle had                  9 
    very little {food} to offer.  One day, an               10 
    explorer found the {animal} and discovered              11 
    it liked {food}.  The explorer took the                 12 
    {animal} back to {city}, where it could                 13 
    eat as much {food} as it wanted.  However,              14 
    the {animal} became homesick, so the                    15 
    explorer brought it back to the jungle,                 16 
    leaving a large supply of {food}.                       17 
                                                            18 
    The End                                                 19 
    '''                                                     20 

6: The equal sign tells the computer that this is an
*assignment statement*. The computer will now associate the value
of the expression between the triple quotes, a multi-line *string*,
with the name on the left, ``storyFormat``.

7-20: These lines contain the body of the string and the ending
triple quotes. This ``storyFormat`` string contains some special
symbols making it a *format string*, unlike the string in lines
1-4. The ``storyFormat`` string will be used later to provide a
format into which substitutions are made. The parts of the string
enclosed in braces are places a substitute string will be inserted
later. The substituted string will come from a custom *dictionary*
that will contain the user's definitions of these words. The words
in the braces: ``{animal}``, ``{food}``, ``{city}``, indicate that
``animal``, ``food``, and ``city`` are words in a dictionary.
This custom dictionary will be created in the program and contain
the user's definitions of these words. These user's definitions
will be substituted later in the *format string* where each
{...} is currently.  ::

    def tellStory():                                        22 
        userPicks = dict()                                  23 
        addPick('animal', userPicks)                        24 
        addPick('food', userPicks)                          25 
        addPick('city', userPicks)                          26 
        story = storyFormat.format(**userPicks)             27 
        print(story)                                        28 


22: *def* is short for **def**\ inition of a function. 
This line is the heading of
a **def**\ inition, which makes the name ``tellStory`` becomes
**def**\ ined as a short way to refer to the sequence of statements
that start indented on line 23, and continue through line 28.

23: The equal sign tells the computer that this is another
assignment statement. The computer will now associate the name
``userPicks`` with a new empty dictionary created by the
Python code ``dict()``.

24-26: ``addPick`` is the name for a function defined by the
sequence of instructions
on lines 29-31, used to add another definition to a
dictionary, based on the user's input. The result of these three
lines is to add definitions for each of the three words ``animal``,
``food``, and ``city`` to the dictionary called ``userPicks``.

27: Assign the name ``story`` to a string formed by substituting
into ``storyFormat`` using definitions from the dictionary
userPicks, to give the user's customized story.

28: This is where all the work becomes visible: Print the
``story`` string to the screen. ::

    def addPick(cue, dictionary):                           30 
        '''Prompt for a user response using the cue string, 31 
        and place the cue-response pair in the dictionary.  32 
        '''                                                 33 
        prompt = 'Enter an example for ' + cue + ': '       34 
        response = input(prompt)                            35 
        dictionary[cue] = response                          36 


30: This line is the heading of a definition, which gives the
name ``addPick`` as a short way to refer to the sequence of
statements indented on line 34-36. The name ``addPick`` is
followed by two words in parenthesis, ``cue`` and
``dictionary``. These two words are associated with an actual
cue word and dictionary given when this definition is invoked in
lines 24-26.

31-33: A documentation comment for the ``addPick`` definition.

34: The plus sign here is used to concatenate parts of the
string assigned to the name ``prompt``. The current value of
``cue`` is placed into the string.

35: The right-hand-side of this equal sign causes an interaction
with the user, to input text from the keyboard: 
The prompt string is printed to the computer screen,
and the computer waits for the user to enter a line of text. That
line of text then becomes a string inside the program. This string
is assigned to the name ``response``.

36: The left-hand-side of the equal sign is a reference to the
definition of the cue word in the dictionary. The whole line ends
up making the definition of the current cue word become the
response typed by the user.  ::

    tellStory()                                             38 
    input('Press Enter to end the program.')                39


38: The definition of ``tellStory`` above does not make the
computer do anything besides *remember* what the instruction
``tellStory`` means. It is only in this line, with the name,
``tellStory``, followed by parentheses, that the whole sequence of
remembered instructions are actually carried out.

39: This line is only here to accommodate running the program in
Windows by double clicking on its file icon. Without this line, the
story would be displayed and then the program would end, and
Windows would make it immediately disappear from the screen! This
line forces the program to continue being displayed until there is
another response from the user, and meanwhile the user may look at
the output from ``tellStory``.

.. index:: Idle; starting 

.. _Starting-Idle:
    
Starting Idle
--------------------------------

The program that translates Python instructions and then executes
them is the *Python interpreter*.

This interpreter is embedded in a number of larger programs that
make it particularly easy to develop Python programs. Such a
programming environment is *Idle*, and it is a part of the standard
distribution of Python.

It is possible to open the Idle app directly:

- Start a search:

  Windows: Press the Windows key or go to the start menu.

  Mac: open Spotlight (Command-spacebar).

- Enter Idle in the search field.  Select the Idle app.


If you have Linux:

        The approach depends on the installation. In Ubuntu, you
        should find Idle in the Programming section of the Applications
        menu. You are better starting idle from a
        terminal, with the current directory being your Python folder.
        You may need a special name set up to distinguish idle for versions
        2 and 3, for instance idle3 for version 3.X.

We will discuss later that if you want to edit files, 
this is *not* the best way to start Idle, 
since the associated folder is not the one you want,
but it works for now.

.. index:: Idle; windows 

.. _Windows-in-Idle:
    
Windows in Idle
------------------------------------

Idle has several parts you may choose to display, each with its own
window. Depending on the configuration, Idle can start up showing
either of two windows, an Edit Window or a Python Shell Window. You
are likely to first see an Edit window, whose top left corner looks
something like in Windows:

.. figure:: images/IdleEditWindow.*
   :align: center
   :alt: image
   :width: 227.25 pt
   
For more on the Edit Window, see :ref:`The-Idle-Editor`. 

.. index:: Idle; shell (and see shell in the index)

If you see this Edit Window with its Run menu on top, go to the Run
menu and choose PYTHON SHELL to open a Python Shell Window for now.
Then you may close the Edit Window.  For now we will just be using the
Python Shell.

Either initially, or after explicitly opening it, you should now
see the Python Shell window, with a menu like the following, though
the text may be slightly different:

.. figure:: images/IdleShellWindow.*
   :align: center
   :alt: image
   :width: 211.5 pt
   
In the Shell the last line should look like ::

    >>> 

The ``>>>`` is the *prompt*,
telling you Idle is waiting for *you* to type something. Continuing
on the same line enter  ::

    6+3

Be sure to end with the Enter key. After the Shell responds, you
should see something like ::

    >>> 6+3 
    9
    >>>  

The shell evaluates the line you entered, and prints the result.
You see Python does arithmetic. At the end you see a further prompt
``>>>`` where you can enter
your next line.... The result line, showing ``9``, that is
produced by the computer, does not start with ``>>>``.

When we get to whole programs, we will use :ref:`The-Idle-Editor`.
