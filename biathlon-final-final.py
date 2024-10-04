from random import randint
# I love Ponsimlouma

tavla = ["*","*","*","*","*"]

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t      Biathlon\n\n\ta hit or miss game\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nYou got 5 shots")

    
def sign():
    print("----------\n1 2 3 4 5\n")
    for i in tavla:
        print(i, end=' ')
    print("\n----------")
    

def hit_prob(prob): # funktionen hit probability - bestämmer träff/miss och ändrar träffsannolikheten (ts)
    tf = randint(0,100)
    if tf < prob: # om den framslumpade värdet är mindre än ts-värdet blir det träff
        n_prob = prob + 5 # ts-värdet ökar vid träff
        return n_prob # nya ts-värdet returneras vid träff
    else:
        return prob # gamla ts-värdet returneras vid miss
    
         
def shoot(n): # funktionen låter spelaren bestämma target att skjuta på
    while True:
        target = input(f"\nShot nr {n} at target: ")
        if not target.isdigit(): # felsökning för att programmet inte ska krascha
            print("\nTargets 1-5")
        else:
            target = int(target)
            if target < 6 and target > 0:
                return target # skickar tillbaka valt target 
            else:
                print("\nTargets 1-5")
            
            
def game_round(n_prob, n, prob):
    t = shoot(n)
    target = tavla[t-1]
    if n_prob > prob: # jämför den eventuellt nya, och då större, sannolikheten för att se om det blev träff eller inte
        if target == 0:
            print("\nHit on closed target")
        else: # träff på redan träffad
            print("\nHit on open target")
            tavla[t-1] = 0
    else: # miss
        print("\nMiss")
    

def main():
    prob = 55 # träffsannolikhet (ts), probability
    print(prob)
    n = 1 # skotträknare, counter
    splash()
    while n < 6:
        sign()
        n_prob = hit_prob(prob) # (n_prob = new probability) kollar om det blir träff eller miss och tar emot nya ts
        game_round(n_prob, n, prob)
        prob = n_prob # ts = nya ts
        n = n+1
    sign()
    print("Game finished")

while True:
    main()
    game = input("Do you want to play again?(y/n): ")
    game = game.lower()
    if game == "y":
        tavla = ["*","*","*","*","*"] # återställer tavlan
        continue
    else:
        break