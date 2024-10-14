user_password = {"nisse":"hej", "misse":"nej", "kisse":"sej"}
user_items = {"nisse":["spik","hammare"], "misse":["katt","hund"], "kisse":["aborre", "regnbåge"]}

def login(user_passwrd): # funktion för inlogg
    while True:
        user = input("\nUser: ").lower() # användare får skriva in användarnamn + lösenord
        password = input("Password: ").lower()
        if user not in user_passwrd or password != user_passwrd[user]: # om lösenordet inte stämmer eller användare inte finns
            print("\nWrong username or password")
            retry = menu(2)
            if retry == "q":
                print("Quitting")
                return retry   
        else:
            return user # return vald användare
        
        
def menu(x): # funktion för alla olika menyer
    if x == 1:
        print("\nl) Login\nq) Quit")
    elif x == 2:
        print("\nr) Try again\nq) Quit")
    elif x == 3:
        print("\nSelect an option\n\na) Add item\nv) View items\nq) Log out")
    option = input("\nOption: ").lower() # för varje möjlig meny får användaren göra ett val
    return option # spara och return gjort val


def view(user, user_itms): # funktion för att "visa" användarens saker
    items = user_itms[user] # items = saker som tillhöt vald användare
    n = 1
    print("\nThese are your items\n")
    for i in items: # printa varje grej
        print(f'{n}) {i}')
        n = n+1
        

def add(user, user_itms): # funktion för att lägga till saker. Tar vald user samt userns saker
    new_item = input("\nAdd item: ")
    items = user_itms[user]
    items.append(new_item)
    return user_itms


def user_actions(user, user_itms): # funktion för "user actions" vid meny 3 
    print(f'Welcome {user}')
    view(user, user_itms) 
    while True:
        action = menu(3) # kommandot givet av användaren
        if action == "v":
            view(user, user_itms)
        elif action == "a":                # utefter valet som användaren görs, kallas olika funktioner
            add(user, user_itms)
            view(user, user_itms)
        elif action == "q":
            break
        
        
def main(user_passwrd, user_itms): # huvudfuktion för programet från start, vid första menyn
    while True:
        print("\nWelcome to Lagra (TM)")
        action = menu(1)
        if action == "q":
            break
        elif action == "l":
            user = login(user_passwrd)
            if user == "q": # om användaren väljer att avsluta direkt
                break
            user_actions(user, user_itms)


main(user_password, user_items)