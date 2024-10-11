user_password={"nisse":"hej", "misse":"nej", "kisse":"sej"}
user_items={"nisse":["spik","hammare"], "misse":["katt","hund"], "kisse":["aborre", "regnbåge"]}

def start_menu(user_password):
    print("Welcome to Lagra (TM)")
    print("1) Login\n","2) Quit")
    fchoice=input("Choose an option: ") #fixa f-sträng din stolle
    fchoice=int(fchoice)
    if fchoice == 1: 
        return True #if is not digit
    else:
        return False

def login(user_password,user_items):
    user=input("User: ").lower()
    password=input("Password: ").lower()
    if password != user_password[user]:
        print("Fel användarnamn eller lösenord")
        print("r) Try again\n", "q) Quit")
        retry=input("Chose and option: ")
        if retry == "q":
            print("Spelet avslutas")
            break
        else:
            continue
    else:
        items=user_item[user]
        print(f"Welcome {user}\n")
        print(f"These are your items, {items}")
        
        


    
#login(user_password)