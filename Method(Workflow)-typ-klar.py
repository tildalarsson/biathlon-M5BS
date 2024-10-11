user_password = {"nisse":"hej", "misse":"nej", "kisse":"sej"}
user_items = {"nisse":["spik","hammare"], "misse":["katt","hund"], "kisse":["aborre", "regnbåge"]}

def login(user_password):
    while True:
        user = input("\nUser: ").lower()
        password = input("Password: ").lower()
        if password != user_password[user]:
            print("\nWrong username or password")
            retry = menu(2)
            if retry == "q":
                print("Quitting")
                break
            elif retry == "r":
                continue    
        else:
            return user
        
        
def menu(x):
    if x == 1:
        print("\nl) Login\nq) Quit")
    elif x == 2:
        print("\nr) Try again\nq) Quit")
    elif x == 3:
        print("\nSelect an option\n\na) Add item\nv) View items\nq) Log out")
    option = input("\nOption: ").lower()
    return option


def user_actions(user, user_items):
    print(f'Welcome {user}')
    view(user, user_items) 
    while True:
        action = menu(3) # kommandot givet av användaren
        if action == "v":
            view(user, user_items)
        elif action == "a":
            add(user, user_items)
            view(user, user_items)
        elif action == "q":
            break


def add(user, user_items):
    new_item = input("\nAdd item: ")
    items = user_items[user]
    items.append(new_item)
    return user_items
    
    
def view(user, user_items):
    items = user_items[user]
    n = 1
    print("\nThese are your items\n")
    for i in items:
        print(f'{n}) {i}')
        n = n+1
        
        
def main(user_password, user_items):
    while True:
        print("\nWelcome to Lagra (TM)")
        action = menu(1)
        if action == "q":
            break
        elif action == "l":
            user = login(user_password,)
            user_actions(user, user_items)


main(user_password, user_items)