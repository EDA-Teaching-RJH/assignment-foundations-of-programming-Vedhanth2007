def init_database():
    names = ["James Kirk","Jean-Luc Picard","Spock","Kathryn Janeway","Montgomery Scott"]
    divs = ["Command","Command","Science","Command","Engineering"]
    ranks = ["Captain","Captain","Commander","Captain","Lt.Commander"]
    ids = ["176","215","276","656","754"]
    return names,divs,ranks,ids

def display_menu(name):
    print("You are now logged in as ", name)
    print(" 1. Add Members\n 2. Remove Memebers\n 3. Update Rank\n 4. Display Roster\n 5. Search Crew\n 6. Filter by Division\n 7. Calculate Payroll\n 8. Count officers\n 9. Exit")
    while True:
        choice = input("Enter your choice here: ")
        return choice
  

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
        print("------------------------------")
        print("New crew member added to logs.")
        print("------------------------------")
    else:
        print("----------------------------------------------------------")
        print("ID not unique or the rank is not valid or Invalid Division")
        print("----------------------------------------------------------")

def remove_member(names, ranks, divs, ids):
    id_num = input("Enter ID number here: ")

    if id_num in ids:
        a = ids.index(id_num)
        names.pop(a)
        ranks.pop(a)
        divs.pop(a)
        ids.pop(a)
        print("------------------------")
        print("Person has been removed.")
        print("------------------------")
    else:
        print("-------------------------")
        print("Person not found in list.")
        print("-------------------------")
        return names, ranks, divs, ids
    
def update_rank(names, ranks, ids):

    id_num = input("Enter ID number here: ")

    if id_num in ids:
        b = ids.index(id_num)
        new_rank = input("Enter new rank here: ").strip().title()
        ranks[b] = new_rank
        print("------------")
        print("Rank updated")
        print("------------")
    else:
        print("-------------")
        print("ID not found.")
        print("-------------")
        return ranks, names

def display_roster(names, ranks, divs, ids):
    if len(names) == 0:
        print("--------------------")
        print("No names in the list")
        print("--------------------")


    for i in range(len(names)):
        print("------------------------------------------------------------------------------")
        print(f"Name: {names[i]}, Rank: {ranks[i]}, Division: {divs[i]}, ID: {ids[i]}")
        print("------------------------------------------------------------------------------")

def search_crew(names, ranks, divs, ids):

    search = input("Enter name here: ").strip().title()

    if search in names:
        i = names.index(search)
        print("-----------------------------------------------------------------------------")
        print(f"Name: {names[i]}, Rank: {ranks[i]}, Division: {divs[i]}, ID: {ids[i]}")
        print("-----------------------------------------------------------------------------")
    else:
        print("-----------------")
        print("Name not in list.")
        print("-----------------")

def filter_by_division(names, divs):
    div_in = input("Enter division here: ").strip().title()

    
    c = 0
    for i in range(len(divs)):
        if divs[i] == div_in:
            print("----------------------")
            print(f"Name: {names[i]}")
            print("----------------------")
            c = c + 1
        i = i + 1
    if c == 0:
        print("----------------------------")
        print("No members of that division.")
        print("----------------------------")
        
def calculate_payroll(ranks):
    value ={
        "Captain": 1000,
        "Commander": 800,
        "Lt.Commander": 600,
        "Lieutenant": 400,
        "Ensign": 200,
    }

    total_payroll = 0
    for rank in ranks:
        total_payroll = total_payroll + value.get(rank,0)
        
    print("--------------------------------")
    print("Total payroll is ", total_payroll)
    print("--------------------------------")
    return total_payroll

def count_officers(ranks):
    count = 0

    for rank in ranks:
        if rank == "Commander" or rank == "Captain":
            count = count + 1
    print("-----------------------------")
    print("number of officers are:",count)
    print("-----------------------------")
    return count

def main ():
    names , divs, ranks, ids = init_database()
    name = input("Enter your full name here: ").strip().title()
    


    while True:
        option = display_menu(name)

        if option == "1":
            add_member(names, ranks, divs, ids)
        elif option == "2":
            remove_member(names, ranks, divs, ids)
        elif option == "3":
            update_rank(names, ranks, ids)
        elif option == "4":
            display_roster(names, ranks, divs, ids)
        elif option == "5":
            search_crew(names, ranks, divs, ids)
        elif option == "6":
            filter_by_division(names, divs)
        elif option == "7":
            calculate_payroll(ranks)
        elif option == "8":
            count_officers(ranks)
        elif option == "9":
            print("Shutting Down.")
            break
        else:
            print("--------------")
            print("Invalid option")
            print("--------------")

main()