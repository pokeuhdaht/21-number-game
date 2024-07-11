
import random

#player selects first or second
def player():
    select=""
    while select != "F" and select != "f" and select != "S" and select != "s":
        print("Do you want to go First or Second? (F/S)")
        select=input("> ")
    if select=="F" or select=="f":
        print("You have opted to go first.")
        return True
    else:
        print("You have opted to go second.")
        return False


#grabs payer increase
def playerInp():
    inp=0
    while inp < 1 or inp > 3:
        print("Would you like to increase number by 1, 2, or 3?")
        inp=int(input("> "))
        if inp < 1 or inp > 3:
            print("Please select a valid number.")
    return inp


def compInp(numLst):
    if numLst==17:
        return 3
    elif numLst==18:
        return 2
    elif numLst==19:
        return 1
    elif numLst==20:
        return 1
    else:
        return random.randint(1,3)
        


def gameStart():

    #if True - Player=First
    #if False - Computer=First
    first=player()
    
    numLst=[]
    game=True       #flag
    
    if first==True:
        while game==True:
            print("Current Inputs")
            if len(numLst)==0:
                print("0")
            else:
                for i in numLst:
                    print(i,end=" ")
            print()
            increaseP=playerInp()
            if increaseP==1:
                numLst.append(len(numLst)+1)
            elif increaseP==2:
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)
            else:
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)

            if len(numLst)>=21:
                return False

            increaseC=compInp(len(numLst))
            print("The computer chose to increase by "+str(increaseC))
            if increaseC==1:
                numLst.append(len(numLst)+1)
            elif increaseC==2:
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)
            else:
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)

            if len(numLst)>=21:
                return True
            
    elif first==False:
        while game==True:
        
            increaseC=compInp(len(numLst))
            print("The computer chose to increase by "+str(increaseC))
            if increaseC==1:
                numLst.append(len(numLst)+1)
            elif increaseC==2:
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)
            else:
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)

            if len(numLst)>=21:
                return True

            print("Current Inputs")
            if len(numLst)==0:
                print("0")
            else:
                for i in numLst:
                    print(i,end=" ")
            print()
            increaseP=playerInp()
            if increaseP==1:
                numLst.append(len(numLst)+1)
            elif increaseP==2:
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)
            else:
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)
                numLst.append(len(numLst)+1)

            if len(numLst)>=21:
                return False
         

def main():
    win=gameStart()

    if win==False:
        print("Sorry. You Lose. :(")
    else:
        print("Congratulations! You WON! :D")
                                                
             
main()

exit()









