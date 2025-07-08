import sys

AVERAGE_HEART_RATE = 80
strength_score = None
dexterity_score = None
constitution_score = None
intelligence_score = None
wisdom_score = None
charisma_score = None

def main():
    print("\nSelect an option to continue")
    print("1. Calculate Stats")
    print("2. Check Stats")
    print("3. Change Stat")
    print("4. Export Stats")
    print("5. Exit")

    MenuChoice = input("Enter the number of the option you would like: ")

    try:
        MenuChoice = int(MenuChoice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        main()
        return

    if MenuChoice == 1:
        calculate_strength()
        calculate_dexterity()
        calculate_constitution()
        calculate_intelligence()
        calculate_wisdom()
        calculate_charisma()
        main()

    elif MenuChoice == 2:
        print_stats()
        main()

    elif MenuChoice == 3:
        if None in (
            strength_score,
            dexterity_score,
            constitution_score,
            intelligence_score,
            wisdom_score,
            charisma_score,
        ):
            print("Stats not calculated yet.")
            print("Please select option 1 from the main menu to calculate your stats first.")
            main()
            return
        print("\nSelect a stat to change:")
        print("1. Strength")
        print("2. Dexterity")
        print("3. Constitution")
        print("4. Intelligence")
        print("5. Wisdom")
        print("6. Charisma")
        print("7. Return to Main Menu")

        change_stat = input("Enter the number of the stat you would like to change: ")

        if change_stat == "1":
            calculate_strength()
        elif change_stat == "2":
            calculate_dexterity()
        elif change_stat == "3":
            calculate_constitution()
        elif change_stat == "4":
            calculate_intelligence()
        elif change_stat == "5":
            calculate_wisdom()
        elif change_stat == "6":
            calculate_charisma()
        elif change_stat == "7":
            main()
            return
        else:
            print("Invalid input.")
        main()

    elif MenuChoice == 4:
        export_stats()
        main()

    elif MenuChoice == 5:
        sys.exit()
    else:
        print("Invalid selection.")
        main()

def export_stats(character_sheet="my_character_sheet.txt"):
    if None in (
        strength_score,
        dexterity_score,
        constitution_score,
        intelligence_score,
        wisdom_score,
        charisma_score,
    ):
        print("\nStats not calculated yet.")
        print("Please select option 1 from the main menu to calculate your stats first.")
        return
        
    with open(character_sheet, 'w') as f:
        f.write("\n===== Your Final Stats =====\n")
        f.write(f"STR: {strength_score}\n")
        f.write(f"DEX: {dexterity_score}\n")
        f.write(f"CON: {constitution_score}\n")
        f.write(f"INT: {intelligence_score}\n")
        f.write(f"WIS: {wisdom_score}\n")
        f.write(f"CHA: {charisma_score}\n")

def print_stats():
    if None in (
    strength_score,
    dexterity_score,
    constitution_score,
    intelligence_score,
    wisdom_score,
    charisma_score,
    ):
        print("\nStats not calculated yet.")
        print("Please select option 1 from the main menu to calculate your stats first.")
        return
     
    print("\n===== Your Final Stats =====")
    print(f"STR: {strength_score}")
    print(f"DEX: {dexterity_score}")
    print(f"CON: {constitution_score}")
    print(f"INT: {intelligence_score}")
    print(f"WIS: {wisdom_score}")
    print(f"CHA: {charisma_score}")

def calculate_strength():
    global strength_score
    bench_pr = get_valid_number("Enter your bench press PR (in pounds): ")
    pushups = get_valid_number("Enter your max push-ups in one set: ")
    long_jump = get_valid_number("Enter your standing long jump distance (in feet): ")

    bench_pr = round(bench_pr)
    pushups = round(pushups)
    long_jump = round(long_jump)

    print(f"Inputs accepted: Bench PR = {bench_pr}, Pushups = {pushups}, Long Jump = {long_jump}")
    strength_score = round(((bench_pr / 15) + (pushups / 3) + (long_jump * 1.5)) / 2.5)
    strength_score = max(1, min(20, strength_score))
    print(f"Your Strength Score is: {strength_score}")

def calculate_dexterity():
    global dexterity_score
    balance = get_valid_integer("Enter how long you can stand on one leg with your eyes closed (in seconds): ")
    mile = get_valid_mile_time("Enter your mile time (MM:SS format): ")
    burpee = get_valid_integer("Enter how many burpees you can do in one minute: ")

    dexterity_score = round((balance / 5) + (12 - mile) + (burpee / 5))
    dexterity_score = max(1, min(20, dexterity_score))

    print(f"Inputs accepted: Balance = {balance}, Mile = {mile:.2f} minutes, Burpees = {burpee}")
    print(f"Your Dexterity Score is: {dexterity_score}")

def calculate_constitution():
    global constitution_score
    plank = get_valid_number("Enter plank time (in seconds): ")
    breath = get_valid_number("Enter breath-hold time (in seconds): ")
    squats = get_valid_number("Enter air squats in a minute: ")

    plank = round(plank)
    breath = round(breath)
    squats = round(squats)

    print(f"Inputs accepted: Plank = {plank}, Breath = {breath}, Squats = {squats}")

    constitution_score = round(((plank / 6) + (10 + breath / 30) + (squats / 4)) / 3)
    constitution_score = max(1, min(20, constitution_score))
    print(f"Your Constitution Score is: {constitution_score}")

def calculate_intelligence():
    global intelligence_score
    while True:
        print("Education Level:")
        print("1. High School")
        print("2. Some College")
        print("3. Bachelor's")
        print("4. Master's")
        print("5. Doctorate")
        edu = input("Enter number: ")
        if edu in {"1", "2", "3", "4", "5"}:
            break
        else:
            print("Invalid selection. Please enter 1-5.")

    gpa = None
    while True:
        gpa_input = input("Enter GPA (0.0 - 4.0): ")
        try:
            gpa = float(gpa_input)
            if 0 <= gpa <= 4:
                break
            else:
                print("GPA must be between 0.0 and 4.0.")
        except ValueError:
            print("Invalid GPA. Please enter a valid number.")

    base = {1: 8, 2: 10, 3: 12, 4: 14, 5: 16}[int(edu)]
    modifier = 2 if gpa >= 4 else 1 if gpa >= 3.5 else 0 if gpa >= 2.5 else -1 if gpa >= 2.0 else -2
    intelligence_score = max(1, min(20, base + modifier))
    print(f"Your Intelligence Score is: {intelligence_score}")

def calculate_wisdom():
    global wisdom_score
    sleep = get_valid_integer("Deep sleep per night (minutes): ")
    heart = get_valid_integer("Resting heart rate (BPM): ")
    outside = get_valid_integer("Time outside per day (minutes): ")

    wisdom_score = round((sleep / 15) + ((AVERAGE_HEART_RATE - heart) / 5) + (outside / 45))
    wisdom_score = max(1, min(20, wisdom_score))
    print(f"Your Wisdom Score is: {wisdom_score}")

def calculate_charisma():
    global charisma_score
    outings = get_valid_integer("Average outings a week: ")
    interactions = get_valid_integer("Meaningful interactions/day: ")
    dates = get_valid_integer("Average dates per month: ")

    charisma_score = round((outings * 1.5) + (interactions / 2) + (dates * 3))
    charisma_score = max(1, min(20, charisma_score))
    print(f"Your Charisma Score is: {charisma_score}")

# Helper functions

def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.replace('.', '', 1).isdigit():
            return float(value)
        else:
            print("Invalid input. Please enter a valid number.")

def get_valid_integer(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a valid whole number.")

def get_valid_mile_time(prompt):
    while True:
        mile = input(prompt)
        try:
            minutes, seconds = map(int, mile.split(":"))
            if 0 <= minutes and 0 <= seconds < 60:
                return minutes + seconds / 60
            else:
                print("Minutes must be >= 0 and seconds must be between 0 and 59.")
        except ValueError:
            print("Invalid format. Please enter mile time as MM:SS.")

if __name__ == "__main__":
    main()




