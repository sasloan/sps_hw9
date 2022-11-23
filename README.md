Homework 9- CIS 2110
Page 1 of 6
1 For EACH of the programs below, write a Python program.  
2 Deliverable:  ONE file (text format- no word or PDF!) that contains all three programs.  The programs 
3 should run in sequence- one after the other (this is a lot easier for me to grade).  
4 Your user-interface should be intuitive to use and neatly formatted.  If you get input from the user, tell 
5 them exactly what you want (eg: Please enter the discount percentage as a decimal number: )
6 Emphasis should be on turning in CODE THAT RUNS!  If your code doesn’t run perfect, get it to run, and 
7 then include pseudocode as comments telling me what you WANTED to do- I’ll try to get you all the 
8 points I can.  
9 For the user interactions- the examples I give below are just examples.  You do NOT need to use the 
10 same wording or spacing, but you should include a header (greeting) and ending.
11
12 Program 1  (10 points)
13 Write a Python program that reads integer numbers from the user, one by one, and appends them to a 
14 list IF the number input by the user is NOT already contained in the list.   If the number is already 
15 entered in the list, the user should be prompted “That number is already in the list- please enter 
16 another number.” When the list contains 10 numbers, the program should display the contents of the 
17 list, then the sum of the numbers, and then the average of the numbers contained in the list.  Your user 
18 interface should be easy to use, and offer instructions to the user when appropriate.   Hint: To append 
19 new values, review section 6.2.1 of “Python for everyone”.  
20
21 Program 2  (10 points)
22 Write a Python function 
23 Def CountChar(paramString)
24 that returns a count of the number of characters in the string paramString.  DO NOT use the length 
25 function (use a while or a for loop).  
26
27 Program 3 
28 a) Write a Python function    def GetNewNumberList()   (10points)
29 The function you write should be named GetNewNumberList().  When it is called, it should create a new 
30 list, then accept any number of floating point or integer numbers from the user, and add each new 
31 number to the list.  When the user is done adding new numbers, they should type “done”.  Then, the list 
32 that holds the numbers input by the user should be returned to the user as a single list.   Hint: To 
33 append new values, review section 6.2.1 of “Python for everyone”.  
34
Homework 9- CIS 2110
Page 2 of 6
35 b) Write a Python function    def CountNegatives(paramOrigList)   (10points)
36 The function you write should be named CountNegatives, and it should accept a list of numbers (intger 
37 or float values).  The function should return the a count of the number of NEGATIVE values that were in 
38 the list that CountNegatives processed.  Note- If no negative numbers were input, the program should 
39 return 0.
40 For example, the code below should print the value:    3
41
42 tempList = [-5,4,0,-1,-1111,7,8,10]
43 tempValue = CountNegatives(tempList)
44 print(tempValue)
45
46c) Write a Python function    def ReverseList(paramOrigList)   (10points)
47 The function you write should be named ReverseList, and it should accept a list of elements of any type.  
48 The function should return a list with the elements in the reverse or der of what they were originally.  
49 Eg:  if you feed in the list [1,”apple”,5.5,”tree farm”,7]
50
51 ReverseList should return the list [7,”tree farm”, 5.5,”apple”,1]
52
53d) Write a Python function    def GetListFirstLast(paramOrigList)   (10points)
54 The function you write should be named GetListFirstLast, and it should accept a list of elements of any 
55 type.  The function should return a list with the FIRST and LAST elements in the list.  
56 Eg:  if you feed in the list [1,”apple”,5.5,”tree farm”,7]
57
58 GetListFirstLast should return the list [1,7]
59
60e) Write a Python function    def DeleteNegatives (paramOrigList)   (10points)
61 The function you write should be named DeleteNegatives, and it should accept a list of float and/or int 
62 types.  The function should return a list with the FIRST and LAST elements in the list.  
63 Eg:  if you feed in the list [1,-2,5.5,-3,7]
64
65 GetListFirstLast should return the list [1,5.5,7]
Homework 9- CIS 2110
Page 3 of 6
66
67
68 Program 4
69 Write a program that tests each of the methods you wrote for programs 2 and 3.  
70 Below are some examples of how the programs could be tested.  These examples show the user 
71 interactions with the computer.  In these examples, assume the computer prompts are green and the 
72 user input is blue.  Your programs do NOT need to be worded or formatted exactly like my examples- 
73 these are just guidelines.   
74 Note: For the tests I’m requesting, I know there might be easier ways to perform the tasks that I’m 
75 asking you to perform other than creating and using functions.  The point is NOT to make it difficult for 
76 you- rather, the point is to test the functions you wrote above.  SO please know- if your tests for 
77 program 4 perform the tasks, but don’t use the functions you wrote above, you will receive a zero.  (I 
78 assume this goes without saying but just want to be crystal clear.)
