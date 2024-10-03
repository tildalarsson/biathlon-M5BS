from random import randint
"I love Ponsimlouma"

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t      Biathlon\n\n\ta hit or miss game\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nYou got 5 shots")

n = 1
shots = 5
tavla = ["*","*","*","*","*"] 

def hit_prob(): #hit probability
    tf = randint(0,10)
    if tf > 4:
        return True
    else:
        return False
    
def sign():
    print("\n1 2 3 4 5\n")
    for i in tavla:
         print(i, end=' ')
         
def shoot(n):
    while True:
        s = int(input(f"\n\nShot nr {n} at target: "))
        if s < 6 and s > 0:
            return s
        else:
            print("\nTargets 1-5")

def game_round(n):
    while n < 6:
        sign()
        s = shoot(n)
        t = tavla[s-1] 
        x = hit_prob() # träff eller miss
        if x:
            print("\nHit on open target")
            tavla[s-1] = 0
            n = n+1
        else:
            print("\nMiss")
            n = n+1
        

game_round(n)  
           
    
    


#def skott(mål):
#    for i in 