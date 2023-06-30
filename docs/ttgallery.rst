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
28. Create a file menu list, the first option is 'Open...' which is connected
    to the popOpen method.
29. The second option is 'Save AS...' which is attached to the popSaveAs
    method.
30. The third option is 'Choose Directory' which is connected to the popChooseDir
    method.
31. The third option is 'Exit' whic is attached to the cancel method.
32. Create a misc menu list, the first about is 'About' which is attached to the
    popAbout method.
33. The second option is 'ChooseColor' which is attached to the popColor
    method.
34. Create the file menu as a submenu attached to the main menu.
35. Create the misc menu as a submenu attached to the main menu.
36. Add the file menu as a pulldown under the 'File' label of the main menu.
37. Add the misc menu as a pulldown under the 'Misc' label of the main menu.
38. Add the main menu to the master window.
39. This is the notebook section.
40. Create a list of tabs.
41. Create a **ttnotebook** using the list of tabs. Store the list of pages in
    the 'pages' attribute.
42. This is the text box section.
43. Create a **ttText** widget 60 characters wide by 10 characters high.
44. Plot it at column 0, row 1. The notebook will be at 0, 0.
45. This is the progress bar section.
46. Create a **ttProgressbar** that is 200 pixels wide.
47. PLot it at column 0, row 2.
48. This is the command button section.
49. Create a button list which has the labels and the linked methods.
50. Create a **ttButtonbox** with two buttons; 'Collect' and 'Exit'.
51. PLot it at column 0, row 3.
52. This is the notebook pages section.
53. Create the first page, 'Simple'.
54. Create the second page, 'Dialog'.
55. Create the third page, 'Multi'.
56. Create the fourth page, 'Other'.
57. Plot the notebook at column 0, row 0. Notice, we filled the notebook
    page before we plotted it.
58. Set the displayed tab to 'Simple'.
59. Create the second (tk) window.
60. Blank line.
61. Create the method that fills the first notebook page, 'Simple'.
62. Method documentation.
63. Create an attribute to store the first page window, *simplePage*.
64. This is a label secton.
65. Add a **ttLabel** on the first page with bold text. Note that if you
    use the text keyword argument, you can specify the contents at creation.
    You don't have to use the *set* method.
66. Same.
67. Plot it at column 0, row 0. Notice that the columns and rows of *simplePage*
    are different from *gui*.
68. This is the line section.
69. Add a horizontal line to the page.
70. Plot it at column 0, row 1, stetching across the page. If we did not use the
    sticky keyword argument, it would have plotted a single point!
71. This is the message section.
72. Add a **ttMessage** widget center justified.
73. Set the message content. This shows how you can use the set method.
74. PLot it at column 0, row 2.
75. This is the entry section.
76. Add a **ttStyle** for a **ttEntry** with green text. The tag must end with
    '.TEntry'
77. Add a **ttEntry** using the style.
78. Set the entry contents.
79. Plot it at column 0, row 3
80. This is the option list section.
81. Create a list of options.
82. Add a **ttOptionlist** using the option list. This is an older-style widegt.
83. Set the selected option to 'Option1'. Note that only a single option can be
    selected at a time. 
84. Plot it at column 0, row 4.
85. This is the combobox section.
86. Create a combobox option list.
87. Add a **ttCombobox** using the combobox option list.
88. Plot it at column 0, row 5.
89. This is the checkbox section.
90. Create a list of checkbox options.
91. Add a **ttCheckbox** using the list of checkbox options.
92. Set the selected option to 'CheckOption1'. Note that multiple options can be
    selected at a time.
93. Plot it at column 0, row 6.
94. Disable the second option ('CheckOption2') from being selected. This
    demonstrates how to change the state of a widget. To enable, you would set the
    state to ['!disabled'].
95. This is the radio button section.
96. Create a list of radio button options.
97. Add a **ttRadiobox** using the list of radio button options. Note that only A
    single option can be selected at a time.
98. Plot it at column 0, row 7.
99. This is the scale section.
100. Add a horizontal **ttScale** that goes between 1 and 10, that has an entry
     width of 2 characters and a width of 200 pixels.
101. Plot it at column 0, row 8.
102. This is the spinbox section.
103. Create a date list for month, date, and year.
104. Add a **ttSpinbox** for dates that runs from 1/1/2000 to 12/31/2099.
105. Set the date to 4/21/2023.
106. Plot it at column 0, row 9.
107. Blank line.
108. Create the method make fills the 'Dialog' page.
109. Method documentation.
110. Create an attribute to store the second page window, *dialogPage*.
111. This is the open dialog section.
112. Add a **ttOpen** with an entry width of 40 characters.
113. PLot it on the 'Dialog' page at column 0, row 0.
114. This is the save as dialog section.
115. Add a **ttSaveAs** with an entry width of 40 characters.
116. PLot it at column 0, row 1.
117. This is the choose directory dialog section.
118. Add a **ttChooseDir** with an entry width of 40 characters.
119. PLot it at column 0, row 2.
120. Blank line.


