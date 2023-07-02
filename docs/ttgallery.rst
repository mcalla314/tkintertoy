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
14. Create the Gui class. We will use composition style so we are not inheriting.
    from any other class.
15. Blank line.
16. Create the __init__ method. This method creates the windows, sets the
    titles, then calls the ``makegui`` method.
17. Method documentation.
18. Create a **Window** and assign an attribute as ``gui``.
19. Create a second independent **Window** and assign an attribute as ``gui2``.
20. Set the title of the main window.
21. Set the title of the second window.
22. Create the gui.
23. Blank line.
24. This method creates and places all the widgets in the main (ttk) window.
25. Method documentation.
26. This is the **ttMenu** creation section. Menus are good for placing command
    options in a pulldown structure. These can be quite complex so this is a
    simple example. Be sure to read the Tkinter documentation.
27. Create a **ttMenu** as the main menu attached to the master attribute to
    the main window.
28. Create a file menu list, the first option is 'Open...' which is connected
    to the popOpen method...
29. The second option is 'Save AS...' which is attached to the popSaveAs
    method...
30. The third option is 'Choose Directory' which is connected to the popChooseDir
    method...
31. The fourth option is 'Exit' whic is attached to the cancel of ``gui``. This
    method is included with all *Tkintertoy* windows.
32. Create a misc menu list, the first about is 'About' which is attached to the
    popAbout method...
33. The second option is 'ChooseColor' which is attached to the popColor
    method...
34. Create the file menu as a submenu attached to the main menu using the file
    menu list.
35. Create the misc menu as a submenu attached to the main menu using the misc
    menu list.
36. Add the file menu as a pulldown under the 'File' label of the main menu.
37. Add the misc menu as a pulldown under the 'Misc' label of the main menu.
38. Add the main menu to the ``menu`` option of the master attribute of the main
    window. This will make the 'File' and 'Misc' labels appear at the top of the
    window.
39. This is the **ttNotebook** creation section. Notebooks are a collection
    of windows, called pages, stacked on top of each other accessed by a tab
    at the top of the window. It is a good way to save on screen space and
    hide groups of widgets. Notebooks are a ttk only widget.
40. Create a list of tabs.
41. Create a **ttnotebook** using the above list. Store the list of pages in
    the 'pages' attribute. Each tab will create its own page.
42. This is the **ttText** section. The text widget includes vertical scrollbars
    and is an extremely powerful widget with lots of uses. Text is a tk only
    widget. Read the Tkinter
    documentation.
43. Create a **ttText** widget 60 characters wide by 10 characters high.
44. Plot it at column 0, row 1. The notebook will be at 0, 0.
45. This is the **ttProgressbar** creation section. Progress bars show the
    user how much time has elapsed during a long operation. Progress bars
    are a ttk only widget. We will see how to update a progress bar in the
    data collection methods.
46. Create a **ttProgressbar** that is 200 pixels wide.
47. PLot it at column 0, row 2.
48. This is the **ttButtonbox** creation section. Buttonboxes are groups
    of buttons connected to commands. These are the widgets that make
    actions happen.
49. Create a button list which has two labels ('Collect' and 'Exit') and the
    linked methods (``collect`` and ``cancel``).
50. Create a **ttButtonbox** with the above paramenters.
51. PLot it at column 0, row 3.
52. This is the **ttNotebook** pages creator section. Each page has its
    own creation method.
53. Create the first page, 'Simple'.
54. Create the second page, 'Dialog'.
55. Create the third page, 'Multi'.
56. Create the fourth page, 'Other'.
57. Plot the notebook at column 0, row 0. Notice, we filled the notebook
    page before we plotted it.
58. Set the displayed tab to 'Simple'.
59. Create the second window. We will fill this window with **ttWidgets**
    that set the keyword option *usetk=True* so you can see the difference
    between tk and ttk widgets. In some cases, working with ttk widgets is
    more complex and the visble difference may not be worth the hassle. A
    good example of this is the **ttEntry** widget.
60. Blank line.
61. Create the method that fills the first notebook page, 'Simple'. This page
    will contain the most commonly used widgets that are easy to implement.
62. Method documentation.
63. Create an attribute to store the first page window, ``simplePage``.
64. This is a label secton.
65. Add a **ttLabel** on the first page with bold text. Note that if you
    use the text keyword argument, you can specify the contents at creation.
    You don't have to use the ``set`` method.
66. Same.
67. Plot it at column 0, row 0. Notice that the columns and rows of ``simplePage``
    are different from ``gui``.
68. This is the line section. Lines are vertical or horizontal which seperate
    groups of widgets.
69. Add a horizontal line to the page.
70. Plot it at column 0, row 1, stetching across the page. If we did not use the
    *sticky='we'* keyword argument, it would have plotted a single point!
71. This is the entry section.
72. Add a **ttStyle** for a **ttEntry** with green text. The tag must end with
    '.TEntry'
73. Add a **ttEntry** using the style.
74. Set the entry contents.
75. Plot it at column 0, row 3
76. This is the **ttCombobox** section. Comboboxes are a combination of a entry
    and a list. They are good for giving the user a fixed set of options but allowing
    them to create their own.  
77. Create a combobox option list.
78. Add a **ttCombobox** using the above list.
79. Plot it at column 0, row 5.
80. This is the checkbox section.
81. Create a list of checkbox options.
82. Add a **ttCheckbox** using the above list.
83. Set the selected option to 'CheckOption1'. Note that multiple options can be
    selected at a time.
84. Plot it at column 0, row 6.
85. Disable the second option ('CheckOption2') from being selected. This
    demonstrates how to change the state of a widget. To enable, you would set the
    state to ['!disabled'].
86. This is the radio button section.
87. Create a list of radio button options.
88. Add a **ttRadiobox** using the list of radio button options. Note that only A
    single option can be selected at a time.
89. Plot it at column 0, row 7.
90. This is the **ttScale** section. Scales are a good widget for single integer
    entry if the range is small.
91. Add a horizontal **ttScale** that goes between 1 and 10, that has an entry
    width of 2 characters and a width of 200 pixels.
92. Plot it at column 0, row 8.
93. This is the **ttSpinbox** section. Spinboxes are a great way to enter a group
    of related integers in a particular format like dates, times, ss numbers, etc.
94. Create a date list for month, date, and year.
95. Add a **ttSpinbox** for dates that runs from 1/1/2000 to 12/31/2099.
96. Set the date to 4/21/2023.
97. Plot it at column 0, row 9.
98. Blank line.
99. Create the method that fills the 'Dialog' page. These widgets are the
    built-in tk dialog widgets.
100. Method documentation.
101. Create an attribute to store the second page window, ``dialogPage``.
102. This is the **ttOpen** dialog section. This is how the user can select A
     file to open.
103. Add a **ttOpen** with an entry width of 40 characters.
104. PLot it on the 'Dialog' page at column 0, row 0.
105. This is the **ttSaveAs** dialog section. This is how the user can select
     a file to save is work. If the filename already exists, a confirming overwrite
     dialog pops up.
106. Add a **ttSaveAs** with an entry width of 40 characters.
107. PLot it at column 0, row 1.
108. This is the **ttChooseDir** dialog section. This allows the user to select a 
     working directory.
109. Add a **ttChooseDir** with an entry width of 40 characters.
110. PLot it at column 0, row 2.
111. Blank line.
112. Create the method that fills the 'Multi' page. This page will contain
     more complex widgets.
113. Method documentation.
114. This is the **ttListbox** section. While an older tk only widget, listboxes
     are still very useful. They can be configured to allow a single, or multiple
     option section.
115. Create an attribute to store the third page window, *multiPage*.
116. Create a list of listbox options.
117. Add a **ttlistbox** that uses the above options that is 4 characters
     high. Listboxes default to single selection.
118. Plot it on the 'Multi' page at column 0, row 0.
119. This is the **ttLedger** section. Ledger is a new widget based on a
     a ttk.Treeview. It is good for displaying multicolumn data. it includes
     a vertical scrollbar. Horizontal scrolling in treeview does not work so
     if you need horizontal scrolling use a text widget.
120. Create a list of lists that contain the column header and column width in
     pixels.
121. Add a **ttLedger**, using the above list with height of 4 characters.
122. Add a line of data to the Ledger.
123. Same.
124. Same.
125. Plot it at column 0, row 1.
126. This the **ttCollector** section. This is a new complex widget combining
     multiple widgets and a ledger with 2 command buttons. In this example,
     we will combine a combobox and a radio button box. It acts like a dialog
     inside of a dialog.
127. We are going to add a **ttFrame**     
     box, a 



71. This is the **ttMessage** section. This is a tk only widget good for displaying
    multiple line text. 
72. Add a **ttMessage** widget center justified.
73. Set the message content. This shows how you can use the set method.
74. PLot it at column 0, row 2.80. This is the option list section. This is an older tk only widget, similar
    to a combox without the entry widget.
81. Create a list of options.
82. Add a **ttOptionlist** using the option list.
83. Set the selected option to 'Option1'. Note that only a single option can be
    selected at a time. 
84. Plot it at column 0, row 4.12     



