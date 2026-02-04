def init_database():
    names = ["James Kirk","Jean-Luc Picard","Spock","Kathryn Janeway","Montgomery Scott"]
    divs = ["Command","Command","Science","Command","Engineering"]
    ranks = ["Captain","Captain","Commander","Captain","Lt.Commander"]
    ids = ["176","215","276","304","154"]
    return names,divs,ranks,ids

def display_menu():
    name = input("Enter your full name here: ").strip().title()
    print("You are now logged in as ", name)
    print("1. Add Members\n 2. Remove Memebers\n 3. Update Rank\n 4. Display Roster\n 5. Search Crew\n 6. Filter by Division\n 7. Calculate Payroll\n 8. Count officers\n 9. Exit")
    choice = int(input("Enter your choice here: "))
    return name, choice

def add_member(names, ranks, divs, ids):
    Tng = ["Captain","Commander","Lt.Commander","Lieutenant","Ensign"]
    n = input("Enter name here: ")
    r = input("Enter the rank here: ")
    d = input("Enter the division here: ")
    ids_num = input("Enter ID number here: ")

    if ids_num not in ids and r in Tng:
        names.append(n)
        ranks.append(r)
        divs.append(d)
        ids.append(ids_num)
        print("New crew member added to logs.")
    else:
        print("ID not unique or the rank is not valid")

def remove_member(names, ranks, divs, ids):
    id_num = input("Enter ID number here: ")

    if id_num in ids:
        a = ids.index(id_num)
        names.pop(a)
        ranks.pop(a)
        divs.pop(a)
        ids.pop(a)
        print("Person has been removed.")
    else:
        print("Person not found in list.")
        return names, ranks, divs, ids
    
def update_rank(names, ranks, ids):

    id_num = int(input("Enter ID number here: "))

    if id_num in ids:
        b = ids.index(id_num)
        new_rank = input("Enter new rank here: ")
        names[b] = new_rank
        print("Rank updated")
    else:
        print("ID not found.")
        return ranks, names

