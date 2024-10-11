user_items = {"nisse":["bil", "båt"]}
user = "nisse"

def user_actions(user, user_items):
    print(f'Welcome {user}')
    view(user, user_items) 
    while True:
        action = menu() # kommandot givet av användaren
        if action == "v":
            view(user, user_items)
        elif action == "a":
            add(user, user_items)
            view(user, user_items)
        elif action == "q":
            break # ?
        #else ? loopa för att få ett giltigt kommando?
    
def menu():
    print("\nSelect an option\n\na) Add item\nv) View item\nq) Log out\n")
    option = input("Option: ").lower()
    return option
    
    
def view(user, user_items):
    items = user_items[user]
    n = 1
    print("\nThese are your items\n")
    for i in items:
        print(f'{n}) {i}')
        n = n+1
        
def add(user, user_items):
    new_item = input("\nAdd item: ")
    items = user_items[user]
    items.append(new_item)
    return user_items
    
        
def main(user_password, user_items):
    #user = login()
    user_actions(user, user_items)

