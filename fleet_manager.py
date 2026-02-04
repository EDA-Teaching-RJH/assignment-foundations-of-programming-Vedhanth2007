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
