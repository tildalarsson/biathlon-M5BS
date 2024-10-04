from random import randint
"I love Ponsimlouma"

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t      Biathlon\n\n\ta hit or miss game\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nYou got 5 shots")

prob = 60
r = 1
shots = 5
tavla = ["*","*","*","*","*"]

'''
def hit_prob(): #hit probability
    global tf_count
    tf = randint(0,10+tf_count)
    if tf > 4:
        tf_count=tf_count+1
        #print(tf_count)
        return True
    else:
        return False
'''
    
def hit_prob(x): #hit probability
    tf = randint(0,100)
    if tf < x:
        x = x+5
        return x
    else:
        return False
    
def sign():
    print("----------\n1 2 3 4 5\n")
    for i in tavla:
        print(i, end=' ')
    print("\n----------")
         
def shoot(n):
    while True:
        s = int(input(f"\nShot nr {n} at target: "))
        if s < 6 and s > 0:
            return s
        else:
            print("\nTargets 1-5")
            
def game_round(x, n, prob):
    s = shoot(n)
    t = tavla[s-1] 
    if x > prob: # det blir träff om sannolikheten för träff ökat
        if t == 0:
            print("\nHit on closed target")
        else: # träff på redan träffad
            print("\nHit on open target")
            tavla[s-1] = 0
        prob = x
    else: # miss
        print("\nMiss")
    

def main(n):
    prob = 60
    while n < 6:
        sign()
        x = hit_prob(prob) # kollar om det blir träff eller miss # tar emot nya sannolikheten
        game_round(x, n, prob)
        n = n+1
    sign()

main(r)  

    
    


#def skott(mål):
#    for i in 