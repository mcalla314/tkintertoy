.. tuorial.rst 06/26/23

=======================
Tkintertoy 1.6 Tutorial
=======================

  :Date: |today|
  :Author: **Mike Callahan**

Introduction
============

*Tkintertoy* grew out of a GIS Python (mapping) class I taught at a local college.
My students knew GIS but when it came time to put the workflows into a standalone
application, they were stumped with the complexity of programming a GUI, even with
*Tkinter*. So I developed an easy to use GUI library based on *Tkinter* that made it
much simpler to code applications. After several trials, the result was *Tkintertoy*
which is easy to use, but also can be create more complex GUIs. I have been
teaching a Python class in a local vocational technical college using *Tkintertoy*
with great success.

With this version, I have fixed a few minor bugs, improved the documentation, improved
the operation of the library, and cleaned up the code for version 1.5. Support for
Python 2 was removed since the library is no longer tested using Python 2.

Tkintertoy creates ``Windows`` which contain widgets. Almost every *tk* or *ttk*
widget is supported and a few combined widgets are included. Most widgets 
are contained in a ``Frame`` which can act as a prompt to the user. The widgets
are referenced by string *tags* which are used to access the widget, its
contents, and its containing Frame. All this information is in the ``content`` 
dictionary of the Window. The fact that the programmer does not need to keep
track of every widget makes interfaces much simpler to write, one only needs
to pass the window. Since the widgets are multipart, I call them **ttWidgets**.

*Tkintertoy* makes it easy to create groups of widgets like radio buttons, check
boxes, and control buttons. These groups are referenced by a single tag but
individual widgets can be accessed through an index number. While the novice
programmer does not need to be concerned with details of creating and assigning a
tk/ttk widget, the more advanced programmer can access all the tk/ttk options and
methods of the widgets. Tkintertoy makes sure that all aspects of tk/ttk are
exposed when the programmer needs them. *Tkintertoy* is light-weight wrapper of
*Tkinter* and can be used a gentle introduction to the complete library.

In the following examples below, one can see how the ideas in Tkintertoy can be used
to create simple but useful GUIs. GUI programming can be fun, which puts the "toy" in
*Tkintertoy*.

A "Hello World" Example
=======================

Let's look at a bare bones example of a complete GUI using imparative style. Imparative code
are sometimes called scripts since their structure is simple. More complex code are ususally
called applications.

This GUI will ask for the user's name and use it in a welcome message. This example uses these
widgets: **ttEntry**, **ttLabel**, and **ttButtonbox**.

In relating this application to a command-line application, the entry replaces the ``input``
function, the label replaces the ``print`` function, and the buttonbox replaces the Enter
key. Below is the code followed by an explanation of every line:

  .. literalinclude:: examples/first.py
      :linenos:
      :language: python3

Here is a screen shot of the resulting GUI:

  .. image:: images/first.png

Here is an explanation of what each line does:

1.  Import the ``Window`` code which is the foundation of Tkintertoy.
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
7.  Place the 'name' ttwidget at column 0 (first column), row 0 (first row) of ``gui`` centered.
    The second argument is the column (x dimension counting from zero) and the third argument is
    the row (y dimension). Both these value default to 0 but it is a good idea to always include
    them. The ``plotxy`` method is basically the tk ``grid`` method with the column and row keywords
    arguments specified. All other keyword arguments to ``grid`` can be used in ``plotxy``. Plot
    was selected as a better word for a novice. However, ``grid`` will also work. Until a widget is
    plotted, it will not appear. However, the ``gui`` window is automatically plotted. Actually,
    you are plotting the ttk.LabelFrame, the ttk.Entry widget is automatically plotting in the
    Frame filling up the entire frame using *sticky='nswe'*.
8.  Place the 'welcome' widget at column 0, row 1 (second row) of ``gui`` centered. There is a 3
    pixel default vertical spacing between widget rows.
9.  Place the 'command' widget at column 0, row 2 of ``gui`` centered with a vertical spacing of 10
    pixels with *pady=10*.
10. Begin an infinite loop.
11. Wait for the user to press click on a button. The ``waitforUser`` method is a synonym
    for the tk ``mainloop`` method. Again, the name was changed to help a novice programmer.
    However, ``mainloop`` will also work. This method starts the event processing loop and is
    the heart of all GUIs. It handles all key presses and mouse clicks. Nothing will happen
    until this method is running. This loop will continue until the user clicks on the either the
    'Ok' or 'Cancel' button. Clicking on close window system widget will have the same action as
    clicking on the 'Cancel' button. This action is built-in to all *Tkintertoy* windows.
12. To get to this line of code, the user clicked on a button. Test to see if the ``content``
    dictionary contains anything. If it does, the user clicked on the 'Ok' button. Otherwise,
    the user clicked on the 'Cancel' button.
13. To get to this line of code, the user clicked on the 'Ok' button. Collect the contents of
    'name' and add it to the "Welcome" string in 'welcome'. This shows how easy it is to get
    and set the contents of a widget using the given methods. To get the value of a widget call
    the ``get`` method. To change the value of any widget call the ``set`` method. The type of
    widget does not matter, ``get`` and ``set`` work for all widgets. Since all widgets are
    contained in the ``content`` directory of ``gui``, the programmer does not need to keep
    track of individual widgets, only their containing frames or windows. Again, the usually
    programmer does not access ``content`` directly, they should use ``get`` and ``set`` methods.
14. This line of code is reached only if the user clicked on 'Cancel' which emptied the
    ``content`` directory. In this case, the user is finished with the application.
15. Break the infinite loop and exit the program. Notice the difference between the infinite
    application loop set up by the ``while`` statement and the event processing loop set up by
    the ``waitforUser`` method. Also, note that when the user clicked on 'Cancel', the tkintertoy
    code exited, but the Python code that called tkintertoy was still running. This is why you must
    break out of infinite loop.

So you can see, with 15 lines of code, Tkintertoy gives you a complete GUI driven application,
which will run on any platform Tkinter runs on with little concern of the particular host.
Most *Tkintertoy* code is cross platform.

Simple Map Creation Dialog
==========================

Below is the code to create a simple dialog window which might be useful for a GIS tool which creates
a map. This example was also written in imparative style in order to help the typical GIS or novice
Python script writer. Procedure and object-oriented style coding will be demonstrated later.

We will need the filename of the input CSV file, the output PNG map image, and the title for the map.
We will use the following widgets: **ttOpen**, **ttSaveAs**, **ttEntry**, and **ttText** as a status
window.

We want the layout for the dialog to look like this:

  .. image:: images/map1.png

Here is the code (we will not worry not the code that actually creates the map!):

  .. literalinclude:: examples/map1.py
      :linenos:
      :language: python3

Each line of code is explained below:

1.  Import the ``Window`` object from tkintertoy.
2.  Create an instance of a ``Window`` and label it ``gui``.
3.  Set the title ``gui`` to "Create a Map".
4.  We want to limit the input files to *.csv only. This list will be used in the method in the
    next line. Notice, you can filter multiple types.
5.  Add an **ttOpen** dialog widget. This is a combination of a ttk.Entry widget, a 'Browse' ttk.
    Button, and a ttk.LabelFrame. If the user clicks on the 'Browse' button, they will see a
    directory limited to CSV files. To allow the user to see the entire path, we changed the width
    of the entry to 40 characters.
6.  We want to limit our output to .png only.
7.  Add a **ttSaveAs** dialog widget. This is a combination of a ttk.Entry widget, a 'Browse' ttk.
    Button, and a ttk.LabelFrame. If the user clicks on the 'Browse' button, they will see a directory
    limited to PNG files. If the file already exists, an overwrite confirmation dialog will pop up.
8.  Add an **ttEntry** widget that is 40 characters wide to collect the map title.
9.  Add a **ttText** widget, which is a combination of a ttk.Text widget, a vertical ttk.Scrollbar,
    and a ttk.LabelFrame. It will have a width of 40 characters, a height of 5 lines, and will be used
    for all status messages. The **ttText** widget is extremelly useful for many different purposes.
10. Add a **ttButtonbox** with the default 'Ok' and 'Cancel' buttons.
11. Plot the 'input' widget at column 0, row 0, vertically separating widgets by 10 pixels.
12. Plot the 'output' widget at column 0, row 1, vertically separating widgets by 10 pixels. Notice
    this will cause a 20 pixel separation between the input and output widgets.
13. Plot the 'title' widget at column 0, row 2, vertically separating widgets by 10 pixels.
14. Plot the 'status' widget at column 0, row 3, vertically separating widgets by 10 pixels.
15. Plot the 'commands' widget at column 0, row 4, vertically separating widgets by 20 pixels. This
    will be 30 pixels from the status widget.
16. Enter the event processing loop and exit when the user clicks on a button. This script will
    execute once so there is no need for an infinte loop.
17. If the user clicked on the OK button do the following:
18. Create the status message.
19. Display the status message.
20. Pretend we are making a map but in reality just pause for 5 seconds so the user can see the status
    message.
21. This is where the actual map making code would begin.
22. Exit the program.

Notice, if the user clicks on the Cancel button, the program exits at line 17.
 
Selection Widgets
=================

Many times you want to limit the user to a fixed set of options. This next example demonstrates
widgets that are useful for this task. We will create a hamburger ordering application which will
use three type of selection widgets: **ttRadiobox**, **ttCheckbox**, and **ttListbox**. We will stay
with imparative style programming.

Radiobox widgets are great for showing the user an list of dependent options. Only one option in the
group can be selected at a time. The name "radiobutton" comes from old-fashioned car radio tuner buttons,
when you pushed one to change a station, the previous one selected poped-up.

Checkboxes allow the user to select many independent options at a time. Listboxes can be programmed to do
both.

We will use a radiobox to select whether the user want a single, double, or a triple burger. We will
use a listbox to indicate which toppings the user wants, and a checkbox to indicate the desired condiments.

Below is a screenshot of the application:

  .. image:: images/burger.png

Here is the code:

  .. literalinclude:: examples/burger.py
      :linenos:
      :language: python3

1.  Import the ``Window`` object from tkintertoy.
2.  Create an instance of a ``Window`` and label it ``app``.
3.  Set the title ``app`` to "Order a Hamburger".
4.  Create a list of burger types.
5.  Add a **ttRadiobox** which is a list of three ttk.Radiobuttons labeled with the type of burgers.
    These will be referenced with a single tag, 'type'. If we want to reference a single Radiobutton, we will
    use an index; [0], [1], or [2].
6.  Create a list of burger toppings.
7.  Add a **ttListbox** which is a tk.Listbox with a vertical tk.Scrollbar. The elements are the items in the
    list of toppings. Notice that *selectmode='multiple'* so the user will be able to select multiple toppings
    without pressing the control or shift keys. This is a good example of when a listbox is useful for multiple
    options. While it does take up screen space, it makes it easy to select many multiple options but restricts
    the user to a fixed set of options.
8.  Create a list of condiments.
9.  Create a **ttCheckbox** which is a list of three ttk.Checkbuttons labeled with the condiments. The
    orientation will be vertical. This is another widget where the user can select multiple options.
    It is best used with a small number of options.
10. Add a **ttText** with a height of 5. This is where the order will appear. Note that the width of the text
    widget determines the width of the entire application.
11. Add a **ttButtonbox** with the default 'Ok' and 'Cancel' buttons.
12. Plot the 'type' widget at column 0, row 0.
13. Plot the 'toppings' widget at column 1, row 0.
14. Plot the 'condiments' widget at column 2, row 0.
15. Plot the 'order' widget at column 0, row 1, strectched across three columns with *colunmspan=3*.
16. Plot the 'commands' widget at column 0, row 2, also stretched across three columns.
17. Blank line
18. Begin a infinite loop.
19. Enter the event processing loop and exit when the user clicks on a button.
20. If the user clicked on the OK button do the following:
21. Get the burger type.
22. Get the selected toppings list.
23. Get the selected condiments list.
24. Start the order message. The *allValue=True* clears the text widget of any previous orders.
25. If the user selected any toppings...
26. Add the toppings phrase in the 'orders' widget.
27. Create a string containing the selected toppings separated by a comma.
28. Add it to the 'orders' widget.
29. If the user selected no toppings...
30. Mark the burger as plain.
31. If the user selected any condiments...
32. Add the condiments phrase.
33. Create a string containing the selected condiments separated by a comma.
34. Add it to the order.
35. Reset the 'type' widget.
36. Reset the 'toppings' widget.
37. Reset the 'condiments' widget and loop back to 19.
38. If the user clicked on the 'Cancel' button...
39. Break the infinate loop. The *Tkintertoy* application was automatically canceled.

This is a example showed some of the selection widgets that are available in *Tkintertoy*.
The best one to use is up to the programmer's discretion. As you can see, this code is getting
too long for imparative style. We will use procedure style in the next example.

Dynamic Widgets
===============

A very useful technique is to create a widget which is dependent on the contents of another widget.
The code below shows a **ttCombobox** which is dependent on a **ttRadiobox** row.

The trick to have the contents of a combobox be dependent on a radiobox, is to create a combo widget
and then create a callback function which looks at the contents of the radiobox and then sets the item
list attribute of the combo widget. This time we will use procedure style code which is a more advanced
style but still accessable to the novice programmer. We will also do a better job in adding comments
to the code.

Here is the screenshot:

  .. image:: images/dynamic_widget1.png

The callback function will have to know the widget that called it which is included when the Window is
passes as an argument, which will lead to some strange looking code. This complexity can be eliminated
by writing in an object-oriented fashion, which will be covered in the next example.

Below is the code:

  .. literalinclude:: examples/dynamic_widget1.py
      :linenos:
      :language: python3

Below explains every line:

1.  Import ``Window`` from tkintertoy.
2.  Blank line.
3.  Define the callback function, ``update``. It will have a single parameter, the calling ``Window``.
4.  This is the function documentation string. It is a great idea to have a documentation string for every
    function and method. Since we are using the triple quote our comment can exceed a single line.
5.  These next three lines define the lookup dictionary.
6.  Same
7.  Same
8.  Get the category the user clicked on. This shows an advantage of *Tkintertoy's* content directory. All
    widgets are included in the window. The programmer does not have to pass individual widgets.
9.  Using this category as a key, set all the values in the **ttCombobox** widget list to the list returned.
    by the lookup dictionary, rather than the entry widget. This is why *allValues=True*.
10. Change the entry value of 'items' to '...' which is why *allValues=False*. This will overwrite any
    selection the user had made. The allValues option has different effects depending on the widget type.
11. Blank line.
12. Create the main function, ``main``. It will have no parameters. Most Python applications have a main driving
    function.
13. The documentation line for ``main``
14. Create the three categories.
15. Create an instance of ``Window`` assigned to ``gui``.
16. Set the title for ``gui``.
17. Add a **ttRadiobox** box using the categories.
18. Add a **ttCombobox** widget. This is a combination of a ttk.Combobox contained in a ttk.LabelFrame. This
    widget will update its items list whenever the user clicks on a radiobox button. This is an example of using
    the *postcommand* option for the combobox. Normally, *postcommand* would be assigned to a single method or
    function name. However, we need to include ``gui`` as an parameter. This is why ``lambda`` is there.
    Do not fear ``lambda``. Just think of it as a special ``def`` command that defines a function in place.
19. Add a **ttButtonbox** with the default 'Ok' and 'Cancel' buttons.
20. Initialize the items widget entry widget to just three dots. This lets the user know there are selections
    available in the pulldown.
21. Plot the category widget at column 0, row 0.
22. Plot the items widget at column 0, row 1.
23. Plot the command buttons at column 0, row 2.
24. Start the event processing loop and wait for the user to click on a button. Notice that as the user clicks
    on a category button, the list in the items combobox changes and the event loop keeps running. We do not need
    an infinite loop.
25. If the user clicked on 'Ok' by seeing if content is not empty.
26. Retrieve the value of the category widget using the get method.
27. Retrieve the value of the items widget that was selected or typed in.
28. This where the actual processing code would start.
29. Exit the program. Calling ``cancel`` is the same as clicking on the Cancel button.
30. Blank line.
31. Call ``main``. Even though we defined ``main`` above, Python will not execute the function until we call it.

Object-Oriented Dynamic Widgets
===============================

While I told you to not fear lambda, if you write code in an object-oriented mode, you don't have to be
concerned about lambda. One can write complex guis in **Tkintertoy** without object-oriented style, which
might be better for novice programmers, but most guis should be oject-oriented once the programmer is
ready. While, the details of writing object-oriented code is far beyond the scope of this tutorial, we
will look at the previous example in an object-oriented mode using composition. You will see, it is not
really complicated at all, just a little different. The GUI design did not change.

Below is the new code:

  .. literalinclude:: examples/dynamic_widget1.py
      :linenos:
      :language: python3

And the line explanations:

1.  Import ``Window`` from tkintertoy.
2.  Blank line.
3.  Create a class called ``Gui``. This will contain all the code dealing with the interface. We are not
    inheriting from a parent class in this example. We will see how to do this in another example below.
4.  This is a class documentation string. It is a great idea to document all classes, too.
5.  Blank line.
6.  Create an initialize method that will create the interface, called ``__init__``. This strange name
    is required. Methods names that begin and end with double underscore are special in Python.
7.  This is the method documentation string.
8.  Create the three categories.
9.  Create an instance of ``Window`` assigned to ``self.gui``. The self means gui is an attribute of the
    instance and all methods in the class will have access to ``self.gui``.
10. Set the title for ``self.gui``.
11. Add a **ttRadiobox** using the categories.
12. Add a **ttCombobox** widget which will update its items list whenever the user clicks on a radiobox
    button. Notice that the *postcommand* option now simply points to the callback method without ``lambda``
    since ALL methods can access ``self.gui``. This is the major advantage to object-oriented code. It
    reduces argument passing.
13. Add a **ttButtonbox** with the default 'Ok' and 'Cancel' buttons.
14. Initialize the items widget.
15. Plot the category widget at column 0, row 0.
16. Plot the items widget at column 0, row 1.
17. Plot the command buttons at column 0, row 2.
18. Blank line.
19. Create the callback method using the ``self`` parameter.
20. This is the method documentation string.
21. These next three lines define the lookup dictionary.
22. Same
23. Same
24. Get the category the user clicked on.
25. Using this category as a key, set all the items in the combobox widget list to the list returned
    by the lookup dictionary, rather than the entry widget, which is why *allValues=True*.
26. Clear the items widget.
27. Blank line.
28. Create the main driving function.
29. Main documentation string. 
30. Create an instance of the ``Gui`` class labeled ``app``. Notice that ``app.gui`` will refer to the
    ``Window`` created in the ``__init__`` method and ``app.gui.content`` will have the contents of the
    window.
31. Start the event processing loop and wait for the user to click on a button.
32. If the user clicked on Ok...
33. Retrieve the value of the category.
34. Retrieve the value of the entry part of the combobox.
35. This where the actual processing code would start.
36. Blank line.
37. Call main.

Notice if the user clicks on 'Cancel' there is no more code to execute.

There are very good reasons for learning this style of programming. It should be used for all except
the simplest GUIs. You will quickly get use to typing "self." All future examples in this tutorial
will use object-oriented style of coding.

Using the Collector Widget
==========================

This next example is the interface to a tornado path generator. Assume that we have a database that has
tornado paths stored by date, counties that the tornado moved through, and the maximum damaged caused
by the tornado (called the Enhanced Fajita or EF scale).

This will demonstrate the use of the **ttCollector** widget, which is a combination of a ttk.Treeview,
and two ttk.Buttons. It acts as a dialog inside a dialog. Below is the screenshot:

  .. image:: images/tornado.png

You can see for the date we will use a **ttSpinbox**. A ttSpinbox is a group of tk/ttk.spinboxes that are
limited to integers, separated by a string, and contained in a tk/ttk.Frame. This is a excellent widget for
dates, times, social security numbers, etc. The ``get`` method will return s string with the values of each
box, with the separtor in between. The ``set`` method also requires the separtor in the string.

The county will be a **ttCombobox** widget, the damage will use **ttCheckbox** and all choices will be shown
in the **ttCollector** widget. Here is the code:

  .. literalinclude:: examples/tornado.py
      :linenos:
      :language: python3

Here are the line explanations, notice the first steps are very similar to the 
previous example:

1.  Import ``Window`` from tkintertoy.
2.  Blank line.
3.  Create a class called ``Gui``. This will contain all the code dealing with the interface.
4.  This is a class documentation string.
5.  Blank line.
6.  Create an initialize method that will create the interface. All methods in the class will have
    access to ``self``.
7.  This is the method documentation string.
8.  Create a list of county names.
9.  Same
10. Create a list of damage levels.
11. Create the parameter list for the date spinner. The first digit is the width in characters, the second
    is the lower limit, the third is the upper limit.
12. The initial date will be 1/1/1980.
13. Set up the column headers for the **ttCollector** widget. The first value is the the header string,
    the second is the width of the column in pixels.
14. Create an instance of ``Window`` labeled ``self.gui``. Again, the ``self`` means that every method
    in the class will have access. Notice, there are no other methods in this class so making gui an
    attribute of self is unnecessary. However, it does no harm, other programmers expect it, and future
    methods can be added easily.
15. Set the title of ``self.gui`` to "Tornado Path Generator".
16. Add a date **ttSpinbox**. This is a combination of 3 ttk.Spinboxes seperated by a slash (/) contained
    in a ttk.LabelFrame. It will be labeled 'tdate' in order to not cause any confusion with a common date
    library.
17. Set the 'tdate' to the default. Notice to set and value of a spinbox you use a string with seperators.
18. Add a county **ttCombobox**.
19. Add a damage level **ttCheckbox**.
20. Add a **ttCollector**. The collector has a tag, the column header list from line 13, a list of the
    widget tags it needs to collect, and the propmt. It also includes two buttons, 'Add' and 'Delete'.
    Clicking on 'Add' will collect the values in the widgets and add them in a line in the treeview.
    Clicking on 'Delete' will delete the currently selected line in the treeview.
21. Same.
22. Add a **ttButtonbox** with the default 'Ok' and 'Cancel' buttons.
23. Plot the 'tdate' widget at column 0, row, 0, separating the widgets by 5 pixels.
24. Plot the 'county' widget at column 0, row 1, separating the widgets by 5 pixels.
25. Plot the 'damage' level widget at column 0, row 2, separating the widgets by 5 pixels.
26. Plot the 'path' widget at column 0, row 3, separating the widgets by 5 pixels.
27. Plot the 'command' widget at column 0, row 4, separating the widgets by 10 pixels.
28. Blank line.
29. Create a ``main`` function.
30. This is the function documentation.
31. Create an instance of the ``Gui`` class which will create the GUI.
32. Start the event processing loop
33. If the user clicked on 'Ok'...
34. Get all the lines in the collector as a list of lists.
35. This is where the tornado path generation code would begin but we are just going to print the data
    in a pop-up information window. The example gives [['4/3/2010', 'Clark', 'EF2'], ['4/3/2010', 'Floyd', 'EF2']].
36. Call the driving function.

When you click on 'Add', the current selections in 'tdate', 'counties', and 'level' will be added into
the collector widget in a row. If you select a row and click on 'Delete', it will be removed. Thus
the collector acts as a GUI inside of a GUI, being fed by other widgets. If this was a real application,
we would generate a tornado path map of the EF-2 tornadoes that moved through Clark and Floyd counties
on April 4, 2010.
  
Using the Notebook Container
============================

**Tkintertoy** includes containers which are ``Windows`` within ``Windows`` in order to organize widgets.
A very useful one is the **ttNotebook** which is a ttk.Notebook. This example shows a notebook that
combines two different map making methods into a single GUI. This will use the following widgets:
**ttEntry**, **ttCheckbox**, **ttText**, **ttSpinbox**, and **ttButtonbox**. The style of code will
stay with composition.

Below is a screenshot:

  .. image:: images/mapper.png

Here is the code. We will also demonstrate to the set and get the contents of more widgets and introduce
some simple error trapping:

  .. literalinclude:: examples/mapper.py
      :linenos:
      :language: python3

Here are the line explanations:

1.  Import datetime for automatic date functions
2.  Import ``Window`` from tkintertoy.
3.  Blank line.
4.  Create a class called ``Gui``. This will contain the code dealing with the interface.
5.  Class documentation string.
6.  Create an initialize method that will create the interface. All methods in the class will have
    access to ``self``.
7.  This is the method documentation string.
8.  Create an instance of ``Window`` that will be asignned to an attribute ``dialog``. All methods in this
    class will have access.
9.  Set the title of the window to Mapper 1.0.
10. This code section is for the notebook widget.
11. Create a list which contains the names of the tabs in the notebook: 'Routine' & 'Accumulate'.
    'Routine' will make a map of one day's rainfall, 'Accumulate' will add up several days worth
    of rain.
12. Add a **ttNotebook**. The notebook will return two ``Windows`` in a list which will be used as a
    container for each notebook page.
13. This code section is for the 'Routine' notebook page.
14. Assign the first page (page[0]) of the notebook, which is a ``Window`` to an attribute ``routine``.
15. Get today's date.
16. Convert it to [date, month, year, month abr]; ex. [24, 6, 2023, 'Jun']
17. Add a title **ttEntry** widget. This will be filled in dynamically and be the title of the map.
18. Set the title using today's date.
19. Same.
20. Plot the title at column 0, row 0.
21. Add an output filename **ttEntry** widget. This will also filled in dynamically.
22. Set the output filename using today's date.
23. Plot the output filename widget at column 0, row 1.
24. Create a list of two types of jobs: Make KMLs & Make Maps.
25. Add a jobs **ttCheckbox**.
26. Turn on both check boxes, by default.
27. Plot the jobs widget at column 0, row 2.
28. This code section is for the 'Accumulate' notebook page.
29. Assign the second page (page[1]) of the notebook, which is a ``Window`` to an attribute ``accum``.
30. Create the list for the parameters of a date spinner.
31. Add an ending date **ttSpinbox**, with the callback set to self.updateAccum().
32. Same.
33. Set the ending date to today.
34. Plot the ending date widget at column 0, row 0.
35. Add a single days back **ttSpinbox** with the callback set to self.updateAccum() as well.
36. Same.
37. Set the default days back to 2.
38. Plot the days back widget at column 0, row 1.
39. Add a title **ttEntry**. This will be filled in dynamically.
40. Plot the title widget at column 0, row 2.
41. Add an output filename **ttEntry**. This will be filled in dynamically.
42. Plot the output filename widget at column 0, row 3.
43. Fill in the title using the default values in the above widgets.
44. This section of code is for the rest of the dialog window.
45. Add a messages **ttText**. This is where all messages to the user will appear.
46. Plot the messages widget at column 0, row 1 of the dialog window. The notebook will be at column 0, row 0.
47. Add a command **ttButtonbox**, the default are labeled Ok and Cancel.
48. Set the callback for the first button to the ``go`` method. We are changing the *command* parameter.
    This shows how easy it is to get to the more complex parts of Tk/ttk from tkintertoy. The ``setWidget``
    allows the programmer to change any of the tk/ttk options after the widget is created.
49. Set the label of the second button to ``Exit`` using the same method as above but changing the *text*
    parameter. This shows how options of buttons can be dynamic.
50. Plot the command buttons at column 0, row 2.
51. Plot the notebook at column 0, row 0.
52. Set the default notebook page to 'Routine'. This will be the page displayed when the application
    first starts. Note that ``set`` and ``get`` use the notebook tab names.
53. Blank line.
54. This method will update the widgets on the 'Accumulate' tab.
55. This is the method documentation string.
56. Get the ending date from the widget.  This is an example of a use of a list comprehension. The ``get``
    method will return a date string. The ``split`` method will return a list of str, and the list comprehension
    convert the values to ints. The result will be [month, day, year].
57. This will turn the list of ints into a datetime object.
58. Turn the object into a comma-separated string 'date-int, month-int, year, month-abrev' like
    '24,6,2023,Jun'.
59. Get the number of days back the user wanted.
60. Set the title of the map in the title widget. As the user changes the dates and days back, this
    title will dynamically change. The user can edit this one last time before they click on 'Ok'.
61. Calculate the beginning date from the ending date and the days back.
62. Convert the datetime into a list of strings ['date-int','month-int'] like ['22','6'].
63. Same.
64. Set the title of the map file to something like 'accum06022-06242023'. Again, this will be dynamically
    updated and can be overridden. Notice that one method is updating two widgets.
65. Same.
66. Blank line.
67. This method will execute the correct the map generation code.
68. This is the method documentation string.
69. Get the selected notebook tab name.
70. Create an instance of a Mapper object. However, we have a chicken/egg type problem. Mapper must know
    about the Gui instance in order to send messages to the user. That is why the Mapper instance must
    be created after the Gui instance. However, the Gui instance must also know about the Mapper instance
    in order to execute the map making code. That is why the Mapper instance is created inside of this
    method. The Gui instance ``self`` is used as an argument to the Mapper initialization method. It
    looks funny but it works.
71. Blank line.
72. This code might fail so we place it in a try...except block.
73. If the current tab is 'Routine'...
74. Run the routine map generation code.
75. If the current tab is 'Accumulate'...
76. Run the accumulated map generation code.
77. Catch any exceptions.
78. Place all error messages into the messages widget. Any error messages will pop-up in a window.
79. Blank line.
80. Create a ``Mapper`` class which contains all the map generation code. This will be a stud here since
    map generation code is well beyond the scope of this tutorial.
81. Class documentation line.
82. Blank line.
83. Create an initialize method that will contain all the map making methods. For this example, this will
    be mainly stubs since actual GIS code is well beyond the scope of this tutorial.
84. Method documentation lines.
85. Same.
86. Make the Gui object an attribute of the instance so all methods have access.
87. Blank line.
88. This method contains the code for making the routine daily precipitation map.
89. Method documentation line.
90. Get the desired map title. This will be used in the magic map making code section.
91. Get the filename of the map.
92. Send a message to the user that the magic map making has begun.
93. This is well beyond the scope of this tutorial.
94. Blank line.
95. This method contains the code for making accumulated precipitation maps, that is, precipitation that
    fell over several days.
96. Method documentation line.
97. Get the desired map title. This will be used in the magic map making code section.
98. Get the filename of the map.
99. Send a message to the user that the magic map making has begun.
100. This is well beyond the scope of this tutorial.
101. Blank line.
102. The ``main`` function.
103. Create the GUI.
104. Run the GUI.
105. Blank line.
106. Standard Python. If you are executing this code from the command line, execute the main function.
     If importing, don't.

Object-Oriented Style Using Inheritance
=======================================

This example gets away from map maiking and is a demonstation of writting in an object-oriented
style using inheritance. This is the style most textbooks will use when explaining GUI creation.
Inheritance means that the application window will inherit all the features of a **Tkintertoy**
``Window``. So instead of refering to the tkintertoy window in the class as self.gui you would
use just self. Think of composition as the application *has* a Window and inheritance as the
application *is* a Window.

The example below is a pizza ordering system. It demostates several ttwidgets: **ttEntry**,
**ttRadiobox**, **ttCombobox**, **ttLine**, two **ttCheckboxes** with the indicator off and on,
**ttListbox**, **ttText**, and several **ttButtons**.

This application works as follows. The user first fills in the customer's name in the entry and
how they are going to get their pizzas in a radio button group with the indicator on. Next, for
every pizza, the user selects a size using a combo and crest type using a radio group with the
indicator off. Next, they click on the the toppings the customer asked for using a scrolling list.
Now, the user add extra cheese or extra sauce of both using a check group. Once the order for
the pizza is complete, the user clicks on the ``Add to Order`` button. This sends the pizza
order to the text box and clears the pizza option widgets, making ready to enter the next pizza.
When all the pizzas are entered. The user clicks on ``Print Order``, which here just prints
the user's name, their delivery method, and their pizzas on the terminal. In real life this
information would go to another system.

Below is a screenshot:

  .. image:: images/pizza.png

Here is the code. We will also demonstrate to the set and get the contents of more widgets and introduce
some simple error trapping:

  .. literalinclude:: examples/pizzagui.py
      :linenos:
      :language: python3

Here are the line explanations:

1.  Import Window from tkintertoy.
2.  Blank line.
3.  Create a class ``PizzaGui`` that inherits from ``Window``. You can think of ``PizzaGui`` as a child of
    ``Window``.
4.  Class documentation.
5.  Blank line.
6.  Create an instance of ``PizzaGui``.
7.  Method documentation.
8.  Initial an instance of ``Window`` and assign it to ``self``. This is how to call the initialzation code
    of the parent class. This will make the instance of ``PizzaGui`` an instance of ``Window``.
9.  Blank line.
10. This method will contain all the code to create the GUI.
11. Method documetation.
12. Set the title of the window.
13. Create a toppings tuple. This could have been a list as well.
14. Same.
15. Create a crust-type tuple.
16. Create an order-type tuple.
17. Create a extra tuple.
18. Create a size tuple.
19. Create a command list for the command buttons.
20. Add an entry for the customer name.
21. Add a radiobox for the order type.
22. Add a **ttLine**. This is a horizontal ttk.Separtor which will strectch across the entire window. It
    has no frame.
23. Add a **ttCombobox** for the size selection.
24. Add a **ttRadiobox** for the crust type. The oriention will be vertical. We want the entire box to light
    up when selected so we are setting the *indicatoron=False*, which is a tk feature, so *usetk=True*.
25. Same.
26. Add the ttListbox for toppings. We also want this to be vertical and we want to be able to select
    multiple toppings without pressing the Control or Shift keys. This shows how a listbox can be used
    instead of a checkbox.
27. Add the ttCheckbox for extra cheese and/or sauce.
28. Add a single command button, 'addpizza', that adds the pizza to the order.
29. Same.
30. Add a ttText widget to show the order.
31. Add the two command buttons defined in line 19.
32. Plot the 'name' entry at column 0, row 0, with a five pixel spacing.
33. Plot the order 'type' radiobox at column 1, row 0, with a five pixel spacing.
34. Plot the line at column 0, row 1 strectched across all of the row with a 10 pixel spacing. If we did
    not use the sticky='we' option, the line would be a single point!
35. Plot the 'size' combobox at column 0, row 2, with a 5 pixel spacing.
36. Plot the 'crust' radiobox at column 1, row 2, with a 5 pixel spacing.
37. Plot the 'toppings' listbox at column 0, row 3, with a 5 pixel spacing.
38. Plot the 'extras' radiobox at column 1, row 3, with a 5 pixel spacing.
39. Plot the 'addpizza' button at column 0, row 4, spread across both columns, with a 10 pixel spacing.
40. Plot the 'summary' text widget at column 0, row 5, spread across both columns, with a 5 pixel
    spacing.
41. Plot the 'command' buttons at column 0, row 6, spread across both columns, with a 10 pixel spacing.
42. Set the 'size' combobox to 'Medium'.
43. Blank line.
44. This method adds a pizza to the order.
45. Method documentation
46. Get the 'size' and the 'crust' selections and create an order str.
47. Collect all the 'toppings' selection create a new str.
48. Add the 'toppings' str to the order str.
49. Collect the 'extras' selection and create a new str.
50. Add the 'extras' selection to the order str.
51. Add the 'order' str to the 'order' text widget.
52. Call the ``clearPizza`` method.
53. Blank line.
54. This method would send an order to another display or computer. Here we are just printing the order to
    the console.
55. Method documentation.
56. Create a summary str with the customer 'name' and the order 'type'.
57. Get the contents of the 'summary' text widget.
58. Show the summary in a pop-up window. Normally this would go to a different display or computer.
59. Call the clearPizza method.
60. Clear the 'name' entry.
61. Clear the selections in the order 'type' radiobox.
62. Clear the 'summary' text widget.
63. Blank line.
64. This method will clear a pizza off of the widgets.
65. Method documentation
66. Set the 'size' combobox to 'Medium'
67. Clear the selection in the 'crust' radiobox.
68. Clear the selections in the 'toppings' listbox.
69. Clear the selections in the 'extras' checkbox.
70. Blank line.
71. The main function.
72. Function documentation.
73. Create an instance of *PizzaGui*.
74. Create the GUI.
75. Start the event loop.
76. Blank line.
77. Run ``main`` if not importing.

In this example, we see that the choice of which widget to use and how they appear is completely up to the
programmer. Novice programmers are encouraged to try out different options to see which widgets meet their
needs.

Dynamically Changing Widgets
============================

The next example is a simple implementation of a digital stopwatch that demonstrates
how to change a widget dynamically. **Tkintertoy** uses both tk and ttk widgets. The appearance
of ttk widgets are changed using the concept of **ttStyles** which will be shown. In addition,
this example will show how to change a widget state from enabled to disabled. This example
will also show how to separate the implementation and the gui code into two separate classes.
Lastly, this code will demonstrate how a complete application based on Tkintertoy could be
written. We will stay with inheritance style coding.

Below is a screenshot:

  .. image:: images/stopwatch.png

Here is the code:

  .. literalinclude:: examples/stopwatch.py
      :linenos:
      :language: python3

Here are the line explanations:

1.  File documentation. While this is a first example, all files should have a some documentation on
    first lines.
2.  Blank line.
3.  We will need the time function from the time module.
4.  Import ``Window`` from tkintertoy.
5.  Blank line.
6.  Define a function, ``sec2hmsc`` which will change floating seconds into (hours, minutes, seconds,
    centiseconds). Notice how type hints work. While the Python interpeter will take no action, other
    tools might find a use for them.
7.  Function documentation string.
8.  Split decimal seconds into whole hours with a remainder. This is an example of tuple unpacking.
9.  Split the remainder into whole minutes with a remainder.
10. Split the remainder into whole seconds and centiseconds.
11. Return the time values as a tuple.
12. Blank line.
13. Define the ``Stopwatch`` class which will encapsulate a stopwatch. Since there is no suitable object
    to inherit from, we will use compositon.
14. Class documentation string.
15. Blank line.
16. Create the ``__init__`` method. This will initialize the stopwatch by calling ``reset``.
17. Method documentation string.
18. Call ``reset``. Since this will be the first time this method was called it will create an attributes
    which will hold the beginning time, the time elapsed while stopped, and the running flag.
19. Blank line.
20. Create the ``start`` method. This will start the stopwatch.
21. Method documentation string.
22. Get the current time and save it in the ``then`` attribute.
23. If the ``elapsed`` attribute is non-zero...
24. The stopwatch has been stopped and ``then`` needs to be adjusted.
25. Set the ``running`` attribute to True.
26. Blank line.
27. Create the ``check`` method. This method will return the elapsed time as a tuple.
28. Method documentation string.
29. If the stopwatch is running...
30. Get the current time.
31. Adjust ``elapsed`` with the current time.
32. In any case, call convert the decimal seconds to a time tuple
33. Return the time tuple.
34. Blank line.
35. Create the ``stop`` method. This will stop the stopwatch.
36. This is the method documentation string.
37. Update the elapsed time by calling ``check``..
38. Set ``running`` to False.
39. Blank line.
40. Create the ``reset`` method. This resets the stopwatch.
41. Method documentation string.
42. Reset all the attributes to the initial state.
43. Same.
44. Same.
45. Blank line.
46. Create the ``Gui`` class. This class will contain the gui for the stopwatch. We will use inheritance.
47. This is the class documentation string.
48. Blank line.
49. Create the ``__init__`` method which will initialize the gui.
50. Mehod documentation string.
51. Create an instance of a ``Window`` which will be ``self``.
52. Save the inputted Stopwatch as the ``stopw`` attribute.
53. Blank line.
54. Create the ``makeGui`` method which will create the gui and begin a display loop.
55. Method documentation string.
56. Set the title of the window.
57. Create a **ttStyle** which has large red characters. This is how we will color our **ttLabel** in
    the stopped state. We don't want the user to input anything so a label is the correct choice of widget.
    Notice that the style must be created for each type of widget. Since this style is for labels, the tag
    must end with ``.TLabel``.
58. Same.
59. Create a **ttStyle** which has large green characters. The is how we will color our label in the
    running state.
60. Same.
61. Create a **ttlabel** which will hold the elapsed time of the stopwatch.
62. Create a list of button labels and commands, ``buttons``, for the buttons. Note the
    commands are Gui methods.
63. Same.
64. Create a row of **ttButtons** which will be initialized using the labels and commands
    in ``buttons``.
65. Plot the 'elapsed' at column 0, row 0.
66. Plot the 'buttons' at column 0, row 1, with a 10 pixel spacing.
67. Update the gui.
68. Blank line.
69. Create the ``startstop`` method. Since the user will start and stop the stopwatch using
    the same button, this method will have do handle both tasks.
70. This is the method documentation string.
71. If the stopwatch is running...
72. Stop it.
73. Retext the first button as 'Start'. It was 'Stop'. This is the method to use to change a widget
    dynamically.
74. Change the 'elapsed' color to red.
75. Enable the 'Reset' button. 'Reset' should only be used while the stopwatch is stopped. The
    ! means "not" so we are setting the state of the second button to "not disabled" which
    enables it.
76. Else, the stopwatch was stopped...
77. Start the stopwatch.
78. Retext the first button as 'Stop'. It was 'Start'.
79. Change the 'elapsed' color to green.
80. Disable the 'Reset' button.
81. Blank line.
82. Create the ``reset`` method, which will reset the stopwatch. Since this is connected
    to the 'Reset' button and this button is disabled unless the stopwatch is stopped,
    this method can only be executed while the stopwatch is stopped.
83. Method documentation string.
84. Reset the stopwatch.
85. Blank line.
86. Create the ``update`` method which shows the elapsed time in 'elapsed'.
87. Method documentation string.
88. Get the elapsed time as a time tuple, (hours, minutes, seconds, centiseconds).
89. Create a template for the ``format`` string method that will convert each time
    element as a two digit number with leading leading zero separated by colons. If
    the time tuple was (0, 12, 6, 13) this template convert it to '00:12:06:13'.
90. Using the template, convert the time tuple into a string.
91. Update 'elapsed' with the time string.
92. After 0.01 seconds, call ``update`` again. This allows the stopwatch to update its
    display every hundredth of a second. Every **Tkintertoy** window has a **master**
    attribute which has many useful methods you can call. This line interrupts the
    event processing loop every 0.01 second which makes sure that the stopwatch is
    displaying the correct elapsed time.
93. Blank line.
94. Create the ``main`` function.
95. Function documentation.
96. Create a stopwatch.
97. Create the gui instance.
98. Make the gui.
99. Start the event processing loop.
100. Run ``main`` if not importing.

Conclusion
==========

It is hoped that with **Tkintertoy** and the included documentation, a Python instructor can quickly
lead a novice Python programmer out of the boring world of command-line interfaces and join the fun
world of GUI programming. To see all the widgets that **Tkintertoy** supports, run ttgallery.py. As
always, looking at the code can be very instructive.

As a result of the classes I have been teaching, I have created a series of narrated slideshows
on YouTube as *Programming on Purpose with Python* which features how to use **Tkintertoy** to
develop complete applications. Just search for *Mike Callahan* and *programming*.
