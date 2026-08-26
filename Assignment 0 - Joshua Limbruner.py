import sys

def listChoices(store): #method created
    print("Available Items:")
    for x in range (0,len(items),1):
        print("["+shorthand[x]+"] "+items[x]+": $"+str(store[items[x]]))
    print("[X] Checkout")
    print("[AI] Re-print Items/Actions")

class Receipt: #Class used
    def __init__(self):
        self.total=0
        self.itemsPurchased=[] #This is going to operate like a 2D Array, this way the code doesn't have to get check the dictionary for prices
    def addItem(self,store,item):
        self.total+=store[item]
        self.itemsPurchased.append([item,store[item]])
    def returnReceipt(self):
        print("RECEIPT\n--------------------")
        for x in self.itemsPurchased:
            print(x[0]+": $"+str(x[1]))
        amountPaid=0
        while self.total-amountPaid>0:
            amountPaid+=5
        print("\nTotal Price: $"+str(self.total)[:4]+"\nAmount Paid: $"+str(amountPaid)[:4]+"\nChange Returned: $"+str(abs(self.total-amountPaid))[:4]+"\n--------------------")

store = {'Bananas':0.65,'Bread':1.82,'Eggs':2.19,'Milk':4.31,'Oranges':1.54} #Dictionary
items=list(store) #Both lists that are used
shorthand=[] #Contains all of the choice options, for referencing in the items list, which is then used to go into store to get prices
for x in range (0,len(items),1): #Figure out what the shorthands are
    if items[x][0] in shorthand:shorthand.append(items[x][:2]) #Case for if an option's 1st letter is already taken, just adds the 2nd letter
    else:shorthand.append(items[x][0])
listChoices(store)
bill=Receipt()
userEntry=""
while userEntry!="X" and len(userEntry)<=2: #the len(userEntry) is to prevent somebody trying to rerun the code while in this loop from being stuck, just takes two buttons presses
    userEntry=input("Enter the key of the item/action: ").title() #.title() is to allow for the first letters to be uppercased automatically
    if userEntry=="AI":
        listChoices(store)
    else:
        for x in range(0,len(shorthand),1):
            if shorthand[x]==userEntry:
                print(items[x]+" added to the cart.")
                bill.addItem(store,items[x])
                break
if userEntry=="X":
    bill.returnReceipt()
else:
    sys.exit("\nPlease press the run button again to reset the script!\n")
sys.exit("\nYou checked out!\n")