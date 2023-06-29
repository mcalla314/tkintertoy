.. ttgallery.rst 06/26/23

=============================
Tkintertoy ttgallery Tutorial
=============================

  :Date: |today|
  :Author: **Mike Callahan**

Introduction
============

In order to demostrate the capabilities of *Tkintertoy* I wrote an sampler-type
applications that demonstrates how to use most of the widgets in the library, *ttgallery*.
This application is a simple collect and retreive program where and user interacts with
the widgets and sees their selections in a text widget. It also shows two independent windows,
one that uses ttk widgets, the other uses older tk widgets.

A Gallery of **ttWidgets**
==========================

Below is the code followed by an explanation of every line:

  .. literalinclude:: examples/ttgallery.py
      :linenos:
      :language: python3

Here is a screen shot of the resulting GUI:

  .. image:: images/ttgallery.png

Here is an explanation of what each line does:

1.  Documentation of application.
2.  Same.
3.  Same.
4.  Same.
5.  Same.
6.  Same.
7.  Same.
8.  Same
9.  Same.
10. Same.
11. Blank line.
12. Import the ``Window`` code which is the foundation of Tkintertoy.
13. Blank line.
14. Create the Gui class. We will use composition style.
15. Blank line.
16. Create the __init__ method.
17. Method documentation.
18. Create a **Window** and assign an attribute as *gui*.
19. Create a second independent **Window** and assign an attribute as *gui2*.
20. Set the title of the main window.
21. Set the title of the second window.
22. Create the gui.
23. Blank line.
24. Create a method that creates and places all the widgets.
25. Method documentation.
26. This is the menu creation section.
27. Create a **ttMenu** as the main menu attached on the master window.
28. Create a file menu, the first option is 'Open...' which is connected
    to the popOpen method.
29. The second option is 'Save AS...' which is attached to the popSaveAs
    method.
30. The third option is 'Choose Directory' which is connected to the popChooseDir
    method.
31. The third option is 'Exit' whic is attached to the cancel method.
32.               

2.  Create an instance of a ``Window`` object assigned to ``gui``. This will initialize Tk,
    create a Toplevel window, create an application Frame, and create a ``content`` dictionary
    which will hold all the widgets.
3.  Change the title of ``gui`` to "My First Tkintertoy GUI!". If you don't do this, the title
    of the ``Window`` will default to "Tk". If you want no title, make the argument '' (a
    null string) or None.
4.  Add an **ttEntry** widget to ``gui``. This will be the combination of a ttk.Entry
    in a ttk.LabelFrame. We are going to tag it with 'name' since that is what we
    going to collect there. However, the tag can be any string. All Tkintertoy widgets
    must have a unique tag which acts as the key for the widget in the ``content``
    dictionary. However, most of the time the programmer does not access the ``content``
    dictionary directly, *Tkintertoy* provides methods for this. The title of the Frame
    surrounding the Entry widget will be 'Type in your name'. Entry frame titles are a
    great place to put instructions to your user. If you don't want a title, just leave
    off this argument. *Tkintertoy will use a plain ttk/tk.Frame instead. The default width
    of the Entry widget is 20 characters, but this, like many other options can be changed.
5.  Add a **ttLabel** widget to ``gui``. This will be the combination of a ttk.Label in a
    ttk.LabelFrame. This tag will be 'welcome' since this where the welcome message will
    appear. Labels are a good widget for one line information to appear that the user
    cannot edit. The explanation to the user of the type of information displayed in the
    **ttLabel** is displayed in the LabelFrame, just like in the **ttEntry**
6.  Add a **ttButtonbox** row with a tag of 'commands'. It defaults to two ttk.Buttons,
    labeled 'Ok' and 'Cancel' contained in a unlabeled ttk.Frame. Each button is connected
    to a function or method, called a "callback" which will execute when the user clicks on
    that button. The default callback for the 'Ok' button is the ``breakout`` method which
    exits the GUI processing loop but keeps displaying the window. This will be explained
    below. The 'Cancel' button callback is the ``cancel`` method which exits the loop,
    removes the window, and empties the ``content`` dictionary. Of course, the button labels
    and these actions can be easily modified by the programmer, but by providing a default
    pair of buttons and callbacks, even a novice programmer can create a working GUI application
    quickly. No callback programming is necessary.