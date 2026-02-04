def init_database():
    names = ["James Kirk","Jean-Luc Picard","Spock","Kathryn Janeway","Montgomery Scott"]
    divs = ["Command","Command","Science","Command","Engineering"]
    ranks = ["Captain","Captain","Commander","Captain","Lt.Commander"]
    ids = ["176","215","276","304","154"]
    return names,divs,ranks,ids

def display_menu(name):
    #name = input("Enter your full name here: ").strip().title()
    print("You are now logged in as ", name)
    print(" 1. Add Members\n 2. Remove Memebers\n 3. Update Rank\n 4. Display Roster\n 5. Search Crew\n 6. Filter by Division\n 7. Calculate Payroll\n 8. Count officers\n 9. Exit")
    while True:
        choice = int(input("Enter your choice here: "))
        #if choice <= 1 or choice >= 9:
        return choice
        #else:
            #print("Invalid input.")

def add_member(names, ranks, divs, ids):
    Tng = ["Captain","Commander","Lt.Commander","Lieutenant","Ensign"]
    divis = ["Command","Operations","Engineering","Medical","Science","Security"]
    n = input("Enter name here: ").strip().title()
    r = input("Enter the rank here: ").strip().title()
    d = input("Enter the division here: ").strip().title()
    ids_num = input("Enter ID number here: ").strip()

    if ids_num not in ids and r in Tng and d in divis:
        names.append(n)
        ranks.append(r)
        divs.append(d)
        ids.append(ids_num)
        print("New crew member added to logs.")
    else:
        print("ID not unique or the rank is not valid or Invalid Division")

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

    id_num = input("Enter ID number here: ")

    if id_num in ids:
        b = ids.index(id_num)
        new_rank = input("Enter new rank here: ")
        ranks[b] = new_rank
        print("Rank updated")
    else:
        print("ID not found.")
        return ranks, names

def display_roster(names, ranks, divs, ids):
    if len(names) == 0:
        print("No names in the list")


    for i in range(len(names)):
        print(f"Names: {names[i]}, Rank: {ranks[i]}, Division: {divs[i]}, ID: {ids[i]}")

def search_crew(names, ranks, divs, ids):

    search = input("Enter name here: ").strip().title()

    for i in range(len(names)):
        if search in names:
            print(f"Names: {names[i]}, Rank: {ranks[i]}, Division: {divs[i]}, ID: {ids[i]}")
        else:
            print("Name not in list.")

def filter_by_division(names, divs):
    divis = ["Command","Operations","Engineering","Medical","Science","Security"]
    div_in = input("Enter division here: ").strip().title()

    for i in range(len(divis)):
        if div_in == divis[i]:
            print(f"Names: {names[i]}")
        else:
            print("Division not in list.")
            return
        
def calculate_payroll(ranks):
    value ={
        "captain": 1000,
        "Commander": 800,
        "Lt.Commander": 600,
        "Lieutenant": 400,
        "Ensign": 200,
    }

    total_payroll = 0
    for rank in ranks:
        total_payroll = total_payroll + value.get(rank,0)
    
    print("Total payroll is ", total_payroll)
    return total_payroll

def count_officers(ranks):
    count = 0

    for rank in ranks:
        if rank == "Commander" or rank == "Captain":
            count = count + 1
    return count

def main ():
    names , divs, ranks, ids = init_database()
    name = input("Enter your full name here: ").strip().title()
    display_menu(name)


    while True:
        option = display_menu(name)

        if option == 1:
            add_member(names, ranks, divs, ids)
        elif option == 2:
            remove_member(names, ranks, divs, ids)
        elif option == 3:
            names , ranks = update_rank(names, ranks, ids)
        elif option == 4:
            display_roster(names, ranks, divs, ids)
        elif option == 5:
            search_crew(names, ranks, divs, ids)
        elif option == 6:
            filter_by_division(names, divs)
        elif option == 7:
            calculate_payroll(ranks)
        elif option == 8:
            count_officers(ranks)
        elif option == 9:
            print("Shutting Down.")
            break
        else:
            print("Invalid option")

main()