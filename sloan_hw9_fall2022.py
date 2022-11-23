def Header(ProjectNum):
    
    title = f"""\nWelcome to H.W. 9 as presented by Sebastian Sloan you are currently \n
              enjoying problem {ProjectNum}. Please follow the instructions below \n
              and have a great day!!"""
              
    return title          

#Problem 1

print(Header(1))

print("""Welcome to Program 1. In this program you will enter 10 different numbers, \n
          the numbers Cannot be the same! If you enter the same number you will be \n
          asked to correct your mistake before continuing. Also Pleae NO Decimals! \n
          whole numbers only! Thank you! Once you have successfully \n
          entered 10 different numbers then the program will output all your \n
          numbers that you entered, the Sum of the numbers you entered and the \n
          average of the numbers you entered. Thank you and enjoy!""")
          
print("")
print("")
print("")


def CountUserListAmount(Param1):
    
    count = 0
    
    for number in Param1:
        
        count = count + 1
      
    return count

userList = []

while(CountUserListAmount(userList) < 10):
    
    individualNum = int(input("Please enter your next number here: "))
    
    for num in userList:
        
        if num == individualNum:
            print("This number has already been entered, Please enter another number that has not been used yet.")
            userList.pop()

    userList.append(individualNum)
        
else:
    
    print("")
    print(f"The numbers you entered are: {userList}")
    print("")
    print(f"The sum of the numbers that you entered is: {sum(userList)}")
    print("")
    print(f"The average of the numbers that you entered is: {(sum(userList))/10}")

# Problem 2

print(Header(2))

print("""\nThis program will tell you exactly how many letters are in a string \n
          That you type in! """)
print("")
          
def CountChar(paramString):
    
    count = 0

    for letter in paramString:
        
        count = count + 1
        
    return count
        
userSentance = input("Please enter your chosen sentance: ")

print(f"The number of characters including spaces that you used is: {CountChar(userSentance)}")

# Problem 3a

print(Header('3a'))

print("""\n In this program you will be asked to input a list of numbers. The \n
          numbers you enter will have no limit and can have decimal points in them.\n
          when you are finished entering numbers please type 'done' for your input \n
          Then the list of numbers that you put in will be listed for your review. Thank you \n
          and enjoy!""")
          
print("")
          
def GetNewNumberList():
    
    newList = [] 
    
    userNum = input("Please enter your next number here: ")
    
    newList.append(userNum)
        
    while(userNum != "done"):
            
        userNum = input("Please enter your next number here: ")
            
        newList.append(userNum)
        
    else:
        
        newList.pop()
        
    return [float(x) for x in newList]
                        
print(GetNewNumberList())
            
# Problem 3b

print(Header('3b'))   

print("""\nIn this program you will be asked to enter a string of numbers \n
            Then the program will tell you how many numbers are negative! Please \n
            only enter numbers and type 'done' when you are finished! have fun!""")
            
print("")

peoplesList = []
    
peoplesNum = input("Please enter the next number in your list here: ")
print("")

peoplesList.append(peoplesNum)

while(peoplesNum != "done"):
        
    peoplesNum = input("Please enter the next number in your list here: ")
    print("")
    
    peoplesList.append(peoplesNum)
    
else:
    
    peoplesList.pop()
    
    [float(x) for x in peoplesList]
    
def CountNegatives(paramOrigList):
            
    count = 0
    
    for number in paramOrigList:
                  
        if(float(number) < 0.0):
            
            count = count + 1
              
    return count
    
print(f" The number of Negative numbers in your list is: {CountNegatives(peoplesList)}")

# Problem 3c

print(Header('3c'))

print("""\n In this program you will be entering a list of items and the program will \n
            will return your list in reverse order!! """)
            
print("")

personsList = []
    
personsEntry = input("Please enter the next item in your list here: ")
print("")

if(personsEntry.isdigit()):
        
    personsList.append(int(personsEntry))
        
elif(personsEntry.replace('.', '', 1).isdigit()):
        
    personsList.append(float(personsEntry))
        
else:
        
    personsList.append(personsEntry)

while(personsEntry != "done"):
        
    personsEntry = input("Please enter the next item in your list here: ")
    print("")
    
    if(personsEntry.isdigit()):
        
        personsList.append(int(personsEntry))
        
    elif(personsEntry.replace('.', '', 1).isdigit()):
        
        personsList.append(float(personsEntry))
        
    else:
        
        personsList.append(personsEntry)
    
else:
    
    personsList.pop()
    
    
def ReverseList(paramOrigList):
    
    emptyList = []
    
    for positions in paramOrigList:
        
        emptyList.insert(0,positions)
        
    return emptyList
              
print(f"Here is the revesed order of your list: {ReverseList(personsList)}")
        
# Problem 3d

print(Header('3d'))

print("""This program will take any list you put in and return the first and last \n
          thinkgs that you put into the list. Please tyep 'done' when you are finished \n
          entering your list. Thank you and enjoy!""")
          
print("")

associatesList = []
    
associatesEntry = input("Please enter the next item in your list here: ")
print("")

if(associatesEntry.isdigit()):
        
    associatesList.append(int(associatesEntry))
        
elif(associatesEntry.replace('.', '', 1).isdigit()):
        
    associatesList.append(float(associatesEntry))
        
else:
        
    associatesList.append(associatesEntry)

while(associatesEntry != "done"):
        
    associatesEntry = input("Please enter the next item in your list here: ")
    print("")
    
    if(associatesEntry.isdigit()):
        
        associatesList.append(int(associatesEntry))
        
    elif(associatesEntry.replace('.', '', 1).isdigit()):
        
        associatesList.append(float(associatesEntry))
        
    else:
        
        associatesList.append(associatesEntry)
    
else:
    
    associatesList.pop()
    
def GetListFirstLast(paramOrigList):
    
    firstAndLast = []
    
    for area in paramOrigList:
        
        if(area == paramOrigList[0]):
            
            firstAndLast.append(area)
            
        elif(area == paramOrigList[-1]):
            
            firstAndLast.append(area)
            
    return firstAndLast

print(f"The first and last enteries you made are: {GetListFirstLast(associatesList)}")
        
# Problem 3e

print(Header('3e'))

print("""This program will remove all negative numbers from the list that you \n
          input. Please only input floats or integers for this program. and ass\n
          always please enter 'done' when you are finished making your list. Thank you \n
          and have fun!! """)
          
print("")

internList = []
    
internEntry = input("Please enter the next item in your list here: ")
print("")

if(internEntry.isdigit()):
        
    internList.append(internEntry)
        
elif(internEntry.replace('.', '', 1).isdigit()):
        
    internList.append(internEntry)
    
elif(internEntry.startswith("-")):
    
    internList.append(internEntry)
        
else:
        
    print("I said only numbers Please.")

while(internEntry != "done"):
        
    internEntry = input("Please enter the next item in your list here: ")
    print("")
    
    if(internEntry.isdigit()):
        
        internList.append(internEntry)
        
    elif(internEntry.replace('.', '', 1).isdigit()):
        
        internList.append(internEntry)
        
    elif(internEntry.startswith("-")):
        
        internList.append(internEntry)
        
    else:
        
        if(internEntry != "done"):
            print("I said only numbers Please.")
    
else:
    
    internList.pop()
        

def DeleteNegatives (paramOrigList):
        
    positiveList = []
    
    for number in paramOrigList:
        
        if(number.isdigit() > 0):
            
            positiveList.append(int(number))
            
        elif(number.replace('.', '', 1).isdigit() > 0):
            
            positiveList.append(float(number))
            
    return positiveList
    
print(f"Here is your list of positive integers and floats: {DeleteNegatives(internList)}")



    

    

        