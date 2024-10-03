from random import randint
print("WELCOME tooooooo BIATLONHHHH\n")
print("You have 5 shots\n")


n=1
list_numbers=[1,2,3,4,5]
tavla=["*","*","*","*","*"]


def hlp_list(): #funktion för listan som visar numret på varje "bricka" i tavlan
    for i in list_numbers:
        print(i, end=" ")
    print()

def sign(): #funktion som skriver ut tavlan
    for i in tavla:
        print(i, end=" ")
    print()

hlp_list()
sign() 

def prob(): #funktion för sannorlikheten
    tf=randint(0,10)
    if tf>4:
        return True #träff
    else:
        return False #miss
        
def in_game(n): #funktion som kör spelet 
    shots=5
    while shots > 0: #körs så länge skott finns kvar
        s=int(input(f"Shot nr {n} at target: "))
        
        if s <= 0 or s > len(tavla): #om input är utanför tavlans intervall
            print("Targets 1-5")
            continue #annars fortsätt
        
        if tavla[s-1]==("0"): #Om man skjuter på något redan träffat
            print("Shot at open target")
            shots=shots-1
            n=n+1
            continue
        
        else:
            
            if tavla[s-1]==("*") and prob(): #Om man skjuter på en stängd bricka samt sannorlikheten är träff
                tavla[s-1]=("0") #Ersätt brickan med en open target
                print("Hit\n")
                n=n+1
            else:
                print("Miss\n")
                n=n+1
            
        shots=shots-1
        hlp_list()
        sign()   
        
        
in_game(n)
            

        
   
    