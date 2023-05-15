.. tuorial.rst 4/28/23
=======================
Tkintertoy 1.4 Tutorial
=======================

  :Date: |today|
  :Author: **Mike Callahan**

Introduction
============

*Tkintertoy* grew out of a GIS Python (mapping) class I taught at a local college.
My students knew GIS but when it came time to put the workflows into a standalone
application, they were stumped with the complexity of programming a GUI, even with
*Tkinter*. So I developed an easy to use GUI library based on *Tkinter* that made it
much simpler for their applications. After several trials the result was *Tkintertoy*
which is easy to use, but also can be create more complex GUIs. I have been
teaching using it locally and created a series of narrated Powerpoint slides using
*Tkintertoy* in the development of easy applications on YouTube. With this version,
I have fixed a few minor bugs, improved the documentation, improved the operation of
the library, and cleaned up the code for version 1.4. Support for Python 2 was removed
since the library is no longer tested using Python 2.

Tkintertoy creates Windows which contain widgets. Almost every *tk* or *ttk* 
widget is supported and a few combined widgets are included. Most widgets 
are contained in a ``Frame`` which can act as a prompt to the user. The widgets
are referenced by string tags which are used to access the widget, its 
contents, and its containing Frame. All this information is in the ``content`` 
dictionary of the Window. The fact that the programmer does not need to keep
track of every widget makes interfaces much simpler to write, one only needs
to pass the window. Since the widgets are multipart, I call them **ttWidgets**.

*Tkintertoy* make it easy to create groups of widgets like radio buttons, check boxes,
and control buttons. These groups are referenced by a single tag but indivisual
widgets can be accessed through an index number. While the novice programmer does
not need to be concerned with details of creating and assigning a tk/ttk widget,
the more advanced programmer can access all the tk/ttk options and methods of the
widgets. Tkintertoy makes sure that all aspects of tk/ttk are exposed when the
programmer needs them.

In the following example below, one can see how the ideas in Tkintertoy can be used to
create simple but useful GUIs. GUI programming can be fun, which puts the "toy" in
Tkintertoy.

A "Hello World" Example
=======================
Let's look at a bare bones example of a complete GUI using imparative style. This GUI
will ask for the user's name and use it in a welcome message. This example uses these
widgets: **ttEntry**, **ttLabel**, and **ttButtonbox**:

  .. literalinclude:: examples/first.py
      :linenos:
      :language: python3

Here is a screen shot of the resulting GUI:

  .. image:: images/first.png

Here is an explanation of what each line does:

1. Import the ``Window`` code which is the foundation of Tkintertoy.
#. Create an instance of a ``Window`` object assigned to ``gui``. This will
   initialize Tk, create a Toplevel window, create an application Frame, and
   create a ``content`` dictionary which will hold all the widgets.
#. Change the title of ``Window`` to "My First Tkintertoy GUI!". If you don't do
   this, the title of the ``Window`` will default to "Tk". If you want no 
   title, make the argument '' or None.
#. Add an **ttEntry** widget to ``gui``. This will be the combination of a ttk Entry
   in a ttk LabelFrame. We are going to tag it with 'name' since that is what we
   going to collect there. However, the tag can be any string. All Tkintertoy widgets
   must have a unique tag which acts as the key for the widget in the ``content``
   dictionary. However, most of the time the programmer does not access the ``content``
   dictionary directly. The title of the Frame surrounding the Entry widget will be
   'Type in your name'. Entry frame titles are a great place to put instructions to your
   user. If you don't want a title, just leave off this argument. The default width of
   the Entry widget is 20 characters, but this, like many other options can be changed.
#. Add a **ttLabel** widget to ``gui``. This will be the combination of a ttk Label in a
   ttk LabelFrame. This tag will be 'welcome' since this where the welcome message will
   appear. Labels are a good widget for one line information to appear that the user
   cannot edit. The explanation of the type of information displayed in the **ttLabel**
   is displayed in the LabelFrame, just like in the **ttEntry**
#. Add a **ttButtonbox** row with a tag of 'commnds'. It defaults to two ttk Buttons,
   labeled 'Ok' and 'Cancel' contained in a unlabeled ttk Frame. The callback for the
   'Ok' button is the ``breakout()`` method which exits the GUI processing loop but keeps
   displaying the window. This will be explained below. The 'Cancel' button callback is
   the ``cancel()`` method which exits the loop, removes the window, and empties the
   ``content`` dictionary. Of course, the button labels and these actions can be easily
   modified by the programmer, but by providing a default pair of buttons, even a novice
   programmer can create a working GUI application.
#. Place the 'name' ttwidget at row 0 (first row) of ``gui`` centered. The ``row=0``
   parameter could have been left off since it is the default. The ``plot()`` method
   is really a synonym for the tk ``grid()`` method. All arguments to ``grid()`` can
   be used in ``plot()``. Plot was selected as a better word for a novice. However, ``grid()``
   will also work. Until a widget is plotted, it will not appear. However, the ``gui``
   window is automatically plotted. Actually, you are plotting the ttk LabelFrame, the
   ttk Entry widget is automatically plotting in the Frame filling up the entire frame.
#. Place the 'welcome' widget at row 1 (second row) of ``gui`` centered. There is a 3
   pixel default vertical spacing between the Label widget and Entry widget.
#. Place the 'command' widget at row 2 (third row) of ``gui`` centered with a vertical
   spacing of 10 pixels.
#. Begin an infinite loop.
#. Wait for the user to press click on a button. The ``waitforUser()`` method is a
   synonym for the tk ``mainloop()`` method. Again, the name was changed to help a
   novice programmer. However, ``mainloop`` will also work. This method starts the event
   processing loop and is the heart of all GUIs. It handles all key presses and mouse clicks.
   Nothing will happen until this method is running. This loop will continue until the user
   clicks on the either the 'Ok' or 'Cancel' button. Clicking on close window system widget
   will have the same action as clicking on the 'Cancel' button. This action is built-in to
   all *Tkintertoy* windows.
#. To get to this line of code, the user clicked on a button. Test to see if the ``content``
   dictionary contains anything. If it does, the user clicked on the 'Ok' button. Otherwise,
   the user clicked on the 'Cancel' button.
#. To get to this line of code, the user clicked on the 'Ok' button. Collect the contents of
   the 'name' ttwidget and add it to the "Welcome" string in the 'welcome' ttwidget. This
   shows how easy it is to get and set the contents of a widget using the given methods. To
   get the value of a widget call the ``get()`` method. To change the value of any widget
   call the ``set()`` method. The type of widget does not matter, ``get()`` and ``set()``
   work for all widgets. Since all widgets are contained in the ``content`` directory
   of ``gui``, the programmer does not need to keep track of individual widgets, only their
   containing frames or windows. Again, the usually programmer does not access ``content``
   directly, they should use ``get`` and ``set`` methods.
#. This line of code is reached only if the user clicked on 'Cancel' which 
   emptied the ``content`` directory. In this case, the user is finished with the
   application.
#. Break the infinite loop and exit the program. Notice the difference between the infinite
   application loop set up by the ``while`` statement and the event processing loop set up by
   the ``waitforUser()`` method. Also note that when the user clicked on 'Cancel', the tkintertoy
   code exited, but the Python code that called tkintertoy was still running. This is why you must
   break out of infinite loop.

So you can see, with 15 lines of code, Tkintertoy gives you a complete GUI driven application,
which will run on any platform Tkinter runs on with little concern of the particular host.
Most Tkintertoy code is cross platform.

Simple Map Creation Dialog
==========================

Below is the code to create a simple dialog window which might be useful for a GIS 
tool which creates a map. This example was also written in imparative style in order
to help the typical GIS or novice Python script writer. Procedure and object-oriented
style mode will be demonstrated later. We will need the filename of the input CSV file,
the output PNG map image, and the title for the map. We will use the following widgets:
**ttOpen**, **ttSaveAs**, **ttEntry**, and **ttText** as a status window.

We want the layout for the dialog to look like this:

  .. image:: images/map1.png

Here is the code (we will not worry not the code that actually creates the map!):

  .. literalinclude:: examples/map1.py
      :linenos:
      :language: python3

Each line of code is explained below:

1. Import the ``Window`` object from tkintertoy.
#. Create an instance of a ``Window`` and label it ``gui``.
#. Set the title ``gui`` to "Create a Map".
#. We want to limit the input files to .csv only. This list will be used in the
   method in the next line. Notice, you can filter multiple types.
#. Add an **ttOpen** dialog widget. This is a combination of a 40 character wide
   ttk Entry widget, a 'Browse' ttk Button, and a ttk LabelFrame. If the user clicks
   on the 'Browse' button, they will see a directory limited to CSV files.
#. We want to limit our output to .png only.
#. Add a **ttSaveAs** dialog widget. This is a combination of a 40 character wide
   ttk Entry widget, a 'Browse' ttk Button, and a ttk LabelFrame. If the user clicks
   on the 'Browse' button, they will see a directory limited to PNG files. If the file already
   exists, an overwrite confirmation dialog will pop up.
#. Add an **ttEntry** widget that is 40 characters wide to collect the map title.
#. Add a **ttText** widget, with a width of 40 characters, a height of 5 lines, which
   will be used for all status messages.
#. Add a **ttButtonbox** with the default 'Ok' and 'Cancel' buttons.
#. Plot the 'input' widget in the first row (row 0), vertically separating widgets by
   10 pixels.
#. Plot the 'output' widget in the second row, vertically separating widgets by 10
   pixels. Notice this will cause a 20 pixel separation between the input and output
   widgets.
#. Plot the 'title' widget in the third row, vertically separating widgets by
   10 pixels.
#. Plot the 'status' widget in the fourth row, vertically separating widgets by 10
   pixels.
#. Plot the 'commands' widget in the fifth row, vertically separating widgets by 20
   pixels. This will be 30 pixels from the status widget.
#. Enter the event processing loop and exit when the user clicks on a button.
#. If the user clicked on the OK button do the following:
#. Create the status message.
#. Display the status message.
#. Pretend we are making a map but in reality just pause for 5 seconds so the user
   can see the status message.
#. This is where the actual map making code would begin.
#. Exit the program.

Notice, if the user clicks on the Cancel button, the program exits at line 17.
 
Dynamic Widgets
===============

A very useful technique is to create a widget which is dependent on the contents of 
another widget. The code below shows a **ttCombo** which is dependent on a **ttRadiobox** row.
Radio boxes limit the user to one option out of a fixed set. Combos combine a list with an
entry widget. Thus the user can select one of several options or type in their own choice.

The trick have have the contents of a combo be dependent on a radio box is to create
a **ttCombo** widget and then create a *callback* function which looks at the contents
of the **ttRadiobox** row and then sets the item list attribute of the combo widget.
This time we will use procedure style code which is a more advanced style but still 
accessable to the novice programmer. However, you will see later that an object-oriented
approach will eliminate some strange looking code.

Here is the screenshot:

  .. image:: images/dynamic_widget1.png

The callback function will have to know the widget that called it which is included 
when the Window is passes as an argument. This complexity can be eliminated by
writing in an object-oriented fashion, which will be covered in the following
section.

Below is the code:

  .. literalinclude:: examples/dynamic_widget1.py
      :linenos:
      :language: python3

Below explains every line:

1. Import ``Window`` from tkintertoy.
#. Blank line.
#. Define the callback function, ``update``. It will have a single parameter, the calling
   ``Window``.
#. This is the function documentation string.
#. These next three lines define the lookup dictionary.
#. Same as above.
#. Same as above.
#. Get the category the user clicked on.
#. Using this category as a key, set all the values in the **ttCombo** widget list
   to the list returned by the lookup dictionary, rather than the entry widget,
   which is why the allValues==True option is used.
#. Change the entry value of 'items' to '...' which is why allValues==False. This will
   overwrite any selection the user had made.
#. Blank line.
#. Create the main function, ``main``. It will have no parameters. Most Python applications
   have a main driving function.
#. The documentation line for ``main``
#. Blank line.
#. Create the three categories.
#. Create an instance of ``Window`` assigned to ``gui``.
#. Set the title for ``gui``.
#. Add a **ttRadio** box using the categories. This is a combination of three ttk
   RadioButtons contained in a ttk LabelFrame. Radiobuttons are great for giving the
   user a fixed set of exclusive options, ie. only one out of the set. Notice the
   programmer does not need to keep track of three radio buttons, only the **ttRadio**
   tag.
#. Add a **ttCombo** widget. This is a combination of a ttk Combobox contained in a
   ttk LabelFrame. This widget will update its items list whenever the user clicks
   on a **ttRadiobox** button. This is an example of using the ``postcommand``
   option for the **ttCombo** widget. Normally, ``postcommand`` would be assigned
   to a single method or function name. However, we need to include ``gui`` as an
   parameter. This is why ``lambda`` is there. Do not fear ``lambda``. Just think
   of it as a special ``def`` command that defines a function in place.
#. Add a **ttButtonbox** with the default 'Ok' and 'Cancel' buttons.
#. Initialize the category widget. This will be just as if the user clicked on Trees.
#. Initialize the items widget entry widget to just three dots. This lets the user know
   there are selections available in the pulldown.
#. Plot the category widget in the first row.
#. Plot the items widget in the second row.
#. Plot the command buttons in the third row.
#. Start the event processing loop and wait for the user to click on a button. Notice
   that as the user clicks on a category button, the list in the items combobox changes
   and the event loop keeps running.
#. Check to see if the user clicked on Ok by seeing if content is not empty.
#. Retrieve the value of the category widget using the get method.
#. Retrieve the value of the items widget that was selected or typed in.
#. This where the actual processing code would start.
#. Exit the program. Calling ``cancel`` is the same as clicking on the Cancel button.
#. Blank line.
#. Call ``main``. Even though we defined ``main`` above, Python will not execute the
   function until we call it.

Object-Oriented Dynamic Widgets
===============================

While I told you to not fear lambda, if you write code in an object-oriented mode, 
you don't have to be concerned about lambda. One can write complex guis in tkintertoy
without object-oriented style, which might be better for novice programmers, most guis
should be oject-oriented once the programmer is ready. While, the details of writing
object-oriented code is far beyond the scope of this tutorial, we will look at the previous
example in an object-oriented mode using composition. You will see, it is not really
complicated at all, just a little different. The GUI design did not change.

Below is the new code:

  .. literalinclude:: examples/dynamic_widget2.py
      :linenos:
      :language: python3

And the line explanations:

1. Import ``Window`` from tkintertoy.
#. Blank line.
#. Create a class called ``Gui``. This will contain all the code dealing with the
   interface. We are not inheriting from a parent class in this example. We will see
   how to do this in another example below.
#. This is a class documentation string.
#. Blank line.
#. Create an initialize method that will create the interface, called ``__init__``. This
   strange name is required. Methods that begin and end with double underscore are special
   in Python.
#. This is the method documentation string.
#. Create the three categories.
#. Create an instance of ``Window`` assigned to ``self.gui``. This means that all
   methods in the class will be able to access the ``Window`` through ``self.gui``.
#. Set the title for ``self.gui``.
#. Add a **ttRadiobox** using the categories.
#. Add a **ttCombo** widget which will update its items list whenever the user
   clicks on a **ttRadiobox** button. Notice that the ``postcommand`` option now simply
   points to the callback method without ``lambda`` since ALL methods can access
   ``self.gui``. This is the major advantage to object-oriented code.
#. Add a **ttButtonbox** with the default 'Ok' and 'Cancel' buttons.
#. Initialize the category widget.
#. Initialize the items widget.
#. Plot the category widget in the first row.
#. Plot the items widget in the second row.
#. Plot the command buttons in the third row.
#. Blank lines improve code readability.
#. Create the callback method using the ``self`` parameter.
#. This is the method documentation string.
#. These next three lines define the lookup dictionary.
#. Same as above.
#. Same as above.
#. Get the category the user clicked on.
#. Using this category as a key, set all the items in the **ttcombobox** widget list
   to the list returned by the lookup dictionary, rather than the entry widget,
   which is why the ``allValues`` option is used.
#. Blank line.
#. Create an instance of the ``Gui`` class labeled ``app``. Notice that ``app.gui``
   will refer to the ``Window`` created in the ``__init__`` method and
   ``app.gui.content`` will have the contents of the window.
#. Start the event processing loop and wait for the user to click on a button.
#. Check to see if the user clicked on Ok by seeing if content is not empty.
#. Retrieve the value of the category using the get method.
#. Retrieve the value of the entry part of the **ttcombobox**. Again, note the difference
   between this line and line 26.
#. Same as above.
#. This where the actual processing code would start.
#. Exit the program.

There are very good reasons for learning this style of programming. It should be used 
for all except the simplest code. You will quickly get use to typing "self." All future
examples in this tutorial will use this style of coding.

Using the Collector Widget
==========================

This next example is the interface to a tornado path generator. Assume that we have a
database that has tornado paths stored by date, counties that the tornado moved 
through, and the maximum damaged caused by the tornado (called the Enhanced Fajita or 
EF scale).

This will demonstrate the use of the ``collector`` widget, which acts as a dialog 
inside a dialog. Below is the screenshot:

  .. image:: images/tornado.png

You can see for the date we will use a **ttSpinbox**, the county will be a
**ttCombo** widget``, the damage will use **ttCheckbox** and all choices
will be shown in the **ttCollector** widget. Here is the code:

  .. literalinclude:: examples/tornado.py
      :linenos:
      :language: python3

Here are the line explanations, notice the first steps are very similar to the 
previous example:

1. Import ``Window`` from tkintertoy.
#. Blank lines improve code readability.
#. Create a class called ``Gui``. This will contain all the code dealing with the
   interface.
#. This is a class documentation string.
#. Blank lines improve code readability.
#. Create an initialize method that will create the interface. All methods in the
   class will have access to ``self``.
#. This is the method documentation string.
#. Create a list of county names.
#. Same as above.
#. Create a list of damage levels.
#. Create the parameter list for the date spinner. The first digit is the width, the
   second is the lower limit, the third is the upper limit.
#. The initial date will be 1/1/1980.
#. Set up the column headers for the **ttCollector** widget. The first value is the
   the header string, the second is the width of the column in pixels.
#. Create an instance of ``Window`` labeled ``self.gui``. Again, the ``self`` means
   that every method in the class will have access. Notice, there are no other methods
   in this class so making gui an attribute of self is unnecessary. However, it does no
   harm, other programmers expect it, and future methods can be added easily.
#. Set the title of ``self.gui`` to "Tornado Path Generator".
#. Add a date **ttSpinbox**. This is a combination of 3 ttk Spinboxes seperated by a slash
   (/) contained in a ttk LabelFrame. It will be labeled tdate in order to not cause any
   confusion with a common date library.
#. Set the date to the default.
#. Add a county **ttCombo**.
#. Add a damage level **ttCheckbox**. This is a combination of 6 ttk Checkbuttons contained
   in a ttk LabelFrame. Checkboxes are great for giving the user a fixed set of non-exclusive
   options.
#. Add a **ttCollector**.
#. Add the command option to **ttButtonbox**.
#. Plot the date widget in the first row, separating the widgets by 5 pixels.
#. Plot the county widget in the second row, separating the widgets by 5 pixels.
#. Plot the damage level widget in the third row, separating the widgets by 5
   pixels.
#. Plot the path widget in the fourth row, separating the widgets by 5 pixels.
#. Plot the command widget in the fifth row, separating the widgets by 10 pixels.
#. Blank lines improve code readability.
#. Create a ``main`` function. This is the way most Python scripts work.
#. This is the function documentation.
#. Blank lines improve code readability.
#. Create an instance of the ``Gui`` class which will create the GUI.
#. Wait for the user to click a button.
#. Get all the lines in the collector as a list of dictionaries.
#. This is where the tornado path generation code would begin.
#. Blank lines improve code readability.
#. Run the driving function.

Note when you click on add, the current selections in tdate, counties, and level will be
added into the **ttCollector** widget in a row. If you select a row and click on Delete,
it will be removed. Thus the collector acts as a GUI inside of a GUI, being fed by other
widgets.
  
Using the Notebook Container
============================

*Tkintertoy* includes containers which are ``Windows`` within ``Windows`` in order to
organize widgets. A very useful one is the **ttNotebook**. This example shows a
notebook that combines two different map making methods into a single GUI. This
will use the following widgets: **ttEntry**, **ttCheckbox**, **ttText**, **ttSpinbox**, and
**ttButtonbox**.

Below is a screenshot:

  .. image:: images/mapper.png

Here is the code. We will also demonstrate to the set and get the contents of more widgets
and introduce some simple error trapping:

  .. literalinclude:: examples/mapper.py
      :linenos:
      :language: python3

Here are the line explanations:

1. Import datetime for automatic date functions
#. Import ``Window`` from tkintertoy.
#. Blank lines improve code readability.
#. Create a class called ``Gui``. This will contain all the code dealing with the
   interface.
#. This is a class documentation string.
#. Create an initialize method that will create the interface. All methods in the
   class will have access to ``self``. We are also going to pass Mapper class (not an
   instance) which will contain all the non-interface code. In this case it will be stubs
   where real code would go. We will see how this works in line 77.
#. This is the method documentation string.
#. This lets all methods in this class access the Mapper instance.
#. Create an instance of ``Window`` that will be asignned to an attribute ``dialog``. All
   methods in this class will have access.
#. Set the title of the window to Mapper 1.0.
#. This code section is for the notebook widget.
#. Create a list which contains the names of the tabs in the notebook:
   ``Routine`` & ``Accumulate``. ``Routine`` will make a map of one day's rainfall,
   ``Accumulate`` will add up several days worth of rain.
#. Add a **ttNotebook**. The notebook will return two ``Windows`` which will be used
   as a container for each notebook page.
#. This code section is for the ``Routine`` notebook page.
#. Assign the first page (page[0]) of the notebook, which is a ``Window`` to an attribute
   ``routine``.
#. Get today's date.
#. Convert it to [date, month, year, month abr]; ex. [25, 12, 2018, 'Dec']
#. Add a title **ttEntry** widget. This will be filled in dynamically.
#. Set the title using today's date.
#. Same as above.
#. Plot the title in the first row.
#. Add an output filename **ttEntry** widget. This will also filled in dynamically.
#. Set the output filename using today's date.
#. Plot the output filename widget in the second row.
#. Create a list of two types of jobs: Make KMLs & Make Maps.
#. Add a jobs **ttCheckbox**.
#. Turn on both check boxes, by default.
#. Plot the jobs widget in the third row.
#. This code section is for the ``Accumulate`` notebook page.
#. Assign the second page (page[1]) of the notebook, which is a ``Window`` to an
   attribute ``accum``.
#. Create the list for the parameters of a date spinner.
#. Add an ending date **ttSpinbox**, with the callback set to self.updateAccum().
#. Same as above.
#. Set the ending date to today.
#. Plot the ending date widget in the first row.
#. Add a single days back **ttSpinbox** with the callback set to self.updateAccum()
   as well.
#. Same as above.
#. Set the default days back to 2.
#. Plot the days back widget in the second row.
#. Add a title **ttEntry**. This will be filled in dynamically.
#. Plot the title widget in the third row.
#. Add an output filename **ttEntry**. This will be filled in dynamically.
#. Plot the output filename widget in the fourth row.
#. Fill in the title using the default values in the above widgets.
#. This section of code is for the rest of the dialog window.
#. Add a messages **ttText**. This is where all messages to the user will appear.
#. Plot the messages widget in the second row of the dialog window. The notebook will be in
   the first row.
#. Add a command **ttButtonbox**, the default are labeled Ok and Cancel.
#. Set the callback for the first button to the ``go`` method. We are changing the
   *command* parameter. This shows how easy it is to get to the more complex parts
   of Tk/ttk from tkintertoy.
#. Set the label of the second button to ``Exit`` using the same method as above but
   changing the *text* parameter.
#. Plot the command buttons in the third row.
#. Plot the notebook in the first row.
#. Set the default notebook page to ``Routine``. This will be the page displayed when the
   application first starts.
#. Blank lines improve readability.
#. This method will update the widgets on the accumulate page expanding on dynamic widgets.
#. This is the method documentation string.
#. Get the ending date from the widget. It will come back as [month, day, year].
#. This will turn the list of ints into a datetime object.
#. Turn the object into a comma-separated string 'date-int, month-int, year, month-abrev'
   like '27,12,2018,Dec'.
#. Get the number of days back the user wanted.
#. Set the title of the map in the title widget. As the user changes the dates and days back,
   this title will dynamically change. The user can edit this one last time before they click
   on Ok.
#. Same as above.
#. Calculate the beginning date from the ending date and the days back.
#. Convert the datetime into a list of strings ['date-int','month-int'] like ['25','12'].
#. Set the title of the map file to something like 'accum1225-12272018'. Again, this will
   be dynamically updated and can be overridden.
#. Same as above.
#. Blank lines improve code readability.
#. This method will execute the correct the map generation code.
#. This is the method documentation string.
#. Get the selected notebook tab page, either 0 for the routine page or 1 for the accumulation
   page.
#. Create an instance of a Mapper object. However, we have a chicken/egg type problem. Mapper
   must know about the Gui instance in order to send messages to the user. That is why the
   Mapper instance must be created after the Gui instance. However, the Gui instance must
   also know about the Mapper instance in order to execute the map making code. That is why
   the Mapper instance is created inside of this method and why we passed the Mapper class
   as an argument. The Gui instance ``self`` is used as an argument to the Mapper
   initialization method. It looks funny but it works.
#. Blank lines improve code readability.
#. This code might fail so we place it in a try...except block.
#. If the current page is the routine page...
#. Run the routine map generation code.
#. If the current page is the accumulation page...
#. Run the accumulated map generation code.
#. Catch any exceptions.
#. Place all error messages into the messages widget.
#. Blank lines improve code readability.
#. Create a ``Mapper`` class which contains all the map generation code. This will be a stud
   here since map generation code is well beyond the scope of this tutorial.
#. Class documentation line.
#. Blank lines improve code readability.
#. Create an initialize method that will contain all the map making methods. For this
   example this will be mainly stubs since actual GIS code is well beyond the scope
   of this tutorial!
#. Method documentation lines.
#. Same as above.
#. Make the Gui object an attribute of the instance so all methods have access.
#. Blank lines improve code readability.
#. This method contains the code for making the routine daily precipitation map.
#. Method documentation line.
#. Get the desired map title. This will be used in the magic map making code section.
#. Get the filename of the map.
#. Send a message to the user that the magic map making has begun.
#. This is well beyond the scope of this tutorial.
#. Blank lines improve code readability.
#. This method contains the code for making accumulated precipitation maps, that is,
   precipitation that fell over several days.
#. Method documentation line.
#. Get the desired map title. This will be used in the magic map making code section.
#. Get the filename of the map.
#. Send a message to the user that the magic map making has begun.
#. This is well beyond the scope of this tutorial.
#. Blank lines improve code readability.
#. Create the ``main`` function.
#. Create the GUI.
#. Run the GUI.
#. Blank lines improve code readability.
#. Standard Python. If you are executing this code from the command line, execute the
   main function. If importing, don't.
#. Same as above.

Object-Oriented Style Using Inheritance
=======================================

This example gets away from map maiking and is a demonstation of writting in an object-oriented
sytle using inheritance. This is the style most textbook will use when explaining GUI creation.
Inheritance means that the application window will inherit all the features of a Tkintertoy
``Window``. So instead of refering to the tkintertoy window in the class as self.gui you would
use just self.

The example below is a pizza ordering system. It demostates several ttwidgets: **ttentry**,
**ttradio**, **ttcombo**, **ttcheck** with the indicator off and on, **ttlist**, **tttext**,
and several **ttbuttons**.

This application works as follows. The user first fills in the customer's name in the entry and
how they are going to get their pizzas in a radio button group with the indicator on. Next, for
every pizza, the user selects a size using a combo and crest type using a radio group with the
indicator off. Next they click on the the toppings the customer asked for using a scrolling list.
Now, the user add extra cheese or extra sauce of both using a check group. Once the order for
the pizza is complete. The user clicks on the ``Add to Order`` button. This sends the pizza
order to the text box and clears the pizza option widgets, making ready to enter the next pizza.
When all the pizzas are entered. The user clicks on ``Print Order``, which here just prints
the user's name, their delivery method, and their pizzas on the terminal.



Dynamically Changing Widgets
============================

The next example is a simple implementation of a digital stopwatch that demonstrates
how to change a widget dynamically. Tkintertoy uses both tk and ttk widgets. The appearance
of ttk widgets are changed using the concept of **ttstyles** which will be shown. In addition,
this example will show how to change a widget state from enabled to disabled. This example
will also show how to separate the implementation and the gui code into two separate classes.
Lastly, this code will demonstrate how a complete application based on Tkintertoy could be
written.

Below is a screenshot:

  .. image:: images/stopwatch.png

Here is the code:

  .. literalinclude:: examples/stopwatch.py
      :linenos:
      :language: python3

Here are the line explanations:

1. File documentation.
#. Blank lines improve code readability.
#. We will need the time function from the time module
#. Import ``Window`` from tkintertoy.
#. Blank lines improve code readability.
#. Define a function, ``sec2hmsc`` which will change decimal seconds into (hours, minutes, seconds,
   centiseconds).
#. Function documentation string.
#. Same as above.
#. Split decimal seconds into whole hours with a remainder.
#. Split the remainder into whole minutes with a remainder.
#. Split the remainder into whole seconds and centiseconds.
#. Return the time values as a tuple.
#. Blank lines improve code readability.
#. Define the ``Stopwatch`` class which will encapsulate a stopwatch.
#. This is the class documentation string.
#. Blank lines improve code readability.
#. Create the ``__init__`` method. This will initialize the stopwatch.
#. This is the method documentation string.
#. Create an attribute which will hold the beginning time.
#. Create an attribute which will hold the time elapsed while stopped.
#. Create an attribute which will hold the running flag.
#. Blank lines improve code readability.
#. Create the ``start`` method. This will start the stopwatch.
#. This is the method documentation string.
#. Get the current time and save it in the ``then`` attribute.
#. Check to see if the ``elapsed`` attribute is non-zero.
#. If so, the stopwatch has been stopped and ``then`` needs to be adjusted.
#. Set the ``running`` attribute to True.
#. Blank lines improve code readability.
#. Create the ``check`` method. This method will return the elapsed time as a
   tuple.
#. This is the method documentation string.
#. Same as above.
#. Check to see if the stopwatch is running.
#. If so, get the current time.
#. Adjust ``elapsed`` with the current time.
#. In any case, call convert the decimal seconds to a time tuple
#. Return the time tuple.
#. Blank lines improve code readability.
#. Create the ``stop`` method. This will stop the stopwatch.
#. This is the method documentation string.
#. Update the elapsed time.
#. Set ``running`` to False.
#. This is the method documentation string.
#. Create the ``reset`` method. This resets the stopwatch.
#. This is the method documentation string.
#. This method is the same as the ``__init__`` so just call it.
#. Blank lines improve code readability.
#. Create the ``Gui`` class. This class will contain the gui for the stopwatch.
#. This is the class documentation string.
#. Blank lines improve code readability.
#. Create the ``__init__`` method which will initialize the gui.
#. This is the method documentation string.
#. Same as above
#. Create an instance of a **Tkintertoy** window and save it as the ``win`` attribute.
#. Save the inputted Stopwatch as the ``stopw`` attribute.
#. Create the gui.
#. Blank lines improve code readability.
#. Create the ``makeGui`` method which will create the gui and begin a display loop.
#. This is the method documentation string.
#. Set the title of the window.
#. Create a **ttstyle** which has large red characters. This is how we will color our
   **ttlabel** in the stopped state. Due to operating system styles, **ttlabels**
   seem to be the safest widgets to experiment with styles. Certain parameters might
   be ignored by other widgets like **ttentry**. Notice that the style must be created
   for each type of widget. Since this style is for **ttlabels**, the tag must end with
   ``.TLabel``.
#. Same as above.
#. Create a **ttstyle** which has large green characters. The is how we will color our
   **ttlabel** in the running state.
#. Same as above.
#. Create a **ttlabel** which will hold the elapsed time of the stopwatch.
#. Create a list of button labels and commands, ``buttons``, for the buttons. Note the
   commands are Gui methods.
#. Same as above.
#. Create a row of **ttbuttons** which will be initialized using the labels and commands
   in ``buttons``.
#. Plot the **ttlabel**
#. PLot the **ttbutton** row.
#. Update the gui. You will see that calling update will start an event processing loop
   without the use of ``waitfoUser``.
#. Blank lines improve code readability.
#. Create the ``startstop`` method. Since the user will start and stop the stopwatch using
   the same button, this method will have do handle both tasks.
#. This is the method documentation string.
#. Check to see if the stopwatch is running.
#. If so, stop it.
#. Retext the first button as Start. It was Stop.
#. Change the color to red.
#. Enable the Reset button. Reset should only be used while the stopwatch is stopped. The
   ! means "not" so we are setting the state of the second button to "not disabled" which
   enables it.
#. Else, the stopwatch was stopped.
#. Start the stopwatch.
#. Retext the first button as Stop. It was Start.
#. Change the color to green.
#. Disable the Reset button.
#. Blank lines improve code readability.
#. Create the ``reset`` method, which will reset the stopwatch. Since this is connected
   to the Reset button and this button is disabled unless the stopwatch is stopped,
   this method can only be executed while the stopwatch is stopped.
#. This is the method documentation string.
#. Reset the stopwatch.
#. Blank lines improve code readability.
#. Create the ``update`` method which shows the elapsed time in the **ttlabel**.
#. This is the method documentation string.
#. Get the elapsed time and a time tuple, (hours, minutes, seconds, centiseconds).
#. Create a template for the ``format`` string method that will convert each time
   element as a two digit number with leading leading zero separated by colons. If
   the time tuple was (0, 12, 6, 13) this template convert it to '00:12:06:13'.
#. Using the template, convert the time tuple into a string.
#. Update the **ttlabel** with the time string.
#. After 0.01 seconds, call ``update`` again. This allows the stopwatch to update its
   display every hundredth of a second. Every Tkintertoy window has a **master**
   attribute which has many useful methods you can call. This line create an event
   processing loop but it only executes every 0.01 second which makes sure that the
   stopwatch is displaying the correct elapsed time.
#. Blank lines improve code readability.
#. Create the ``main`` function.
#. This is the function documentation.
#. Create a stopwatch.
#. Create and run the gui. Note, that assigning the gui is unnecessary.
#. Blank lines improve code readability.
#. Standard Python. If you are executing this code from the command line, execute the
   main function. If importing, don't.
#. Same as above.

Conclusion
==========

It is hoped that with *Tkintertoy+, a Python instructor can quickly lead a novice Python
programmer out of the boring world of command-line interfaces and join the fun world of
GUI programming. To see all the widgets that *Tkintertoy* supports, run ttgallery.py.
As always, looking at the code can be very instructive.

As a result of the classes I have been teaching, I have created a series of narrated slideshows
on YouTube as *Programming on Purpose with Python* which features how to use *Tkintertoy* to
develop complete applications. Just search for *Mike Callahan* and *programming*.


  

  







