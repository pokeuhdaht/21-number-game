import random

class Player:
    def __init__(self,name):
        self.name=name
        self.first=False

def firstPlayer(user,computer):
    selection=""
    while selection.lower() !="f" and selection.lower() !="s": 
        print("Do you want to go First or Second? (F/S)")
        selection=input("> ")
        if selection=="f":
            print("You have opted to go first.")
            user.first=True
            return None
        if selection=="s":
            user.first=False
            print("You have opted to go second.")
            return None

def CurrentInput(usedNumbers):
    print("Current Input")
    if len(usedNumbers)==0:
        print("0")
    else:
        for i in usedNumbers:
            print(i,end=" ")
        print()

def GetPlayerInput():
    validChoices=[1,2,3]
    while True:
        print("Would you like to increase the number by 1, 2, or 3?")
        choice=input("> ")
        if choice.isdigit() and int(choice) in validChoices:
            return int(choice)
        else:
            print("Please select a valid number")
            
def GetComputerInput(listLength):
    if listLength==17:
        return 3
    elif listLength==18:
        return 2
    elif listLength==19:
        return 1
    elif listLength==20:
        return 1
    else:
        return random.randint(1,3)

def IncreaseListLength(listLength,IncreaseUserInput):
    listLength=listLength
    j=0
    while j < IncreaseUserInput:
        listLength.append(len(listLength)+1)
        j+=1
    return listLength

def gameStart():
    usedNumbers=[]
    user=Player("User")
    computer=Player("Computer")
    firstPlayer(user, computer)
    CurrentInput(usedNumbers)
    while True:       
        if user.first==True:
            IncreaseUserInput=GetPlayerInput()
            numbersUsed=IncreaseListLength(usedNumbers,IncreaseUserInput)
            print("After Player Input:")
            CurrentInput(usedNumbers)
            if len(usedNumbers)>=21:
                return False
            IncreaseComputerInput=GetComputerInput(usedNumbers)
            numbersUsed=IncreaseListLength(usedNumbers,IncreaseComputerInput)
            print("After Computer Input:")
            CurrentInput(usedNumbers)
            if len(usedNumbers)>=21:
                return True
        if user.first==False:
            IncreaseComputerInput=GetComputerInput(usedNumbers)
            numbersUsed=IncreaseListLength(usedNumbers,IncreaseComputerInput)
            print("After Computer Input:")
            CurrentInput(usedNumbers)
            if len(usedNumbers)>=21:
                return True
            IncreaseUserInput=GetPlayerInput()
            numbersUsed=IncreaseListLength(usedNumbers,IncreaseUserInput)
            print("After Player Input:")
            CurrentInput(usedNumbers)
            if len(usedNumbers)>=21:
                return False      

def main():
    winCondition=gameStart()
    if winCondition==False:
        print("Sorry. You Lose :(")
    else:
        print("Congratulations! You WON! :D")

main()
exit()
