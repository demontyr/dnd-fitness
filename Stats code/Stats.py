import sys
import test2

AVERAGE_HEART_RATE = 80
strength_score = None
dexterity_score = None
constitution_score = None
intelligence_score = None
wisdom_score = None
charisma_score = None

def main():
    while True:
        print("\nSelect an option to continue")
        print("1. Calculate Stats")
        print("2. Check Stats")
        print("3. Change Stat")
        print("4. Export Stats")
        print("5. Run Test")
        print("6. Exit")

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

        elif MenuChoice == 2:
            print_stats()

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
            while True:
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
            

        elif MenuChoice == 4:
            export_stats()
            

        elif MenuChoice ==5:
            test2.run_all_tests()
            
        elif MenuChoice == 6:
            break
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
        f.write(f"STR: {strength_score} {get_stat_mod(strength_score)}\n")
        f.write(f"DEX: {dexterity_score} {get_stat_mod(dexterity_score)}\n")
        f.write(f"CON: {constitution_score} {get_stat_mod(constitution_score)}\n")
        f.write(f"INT: {intelligence_score} {get_stat_mod(intelligence_score)}\n")
        f.write(f"WIS: {wisdom_score} {get_stat_mod(wisdom_score)}\n")
        f.write(f"CHA: {charisma_score} {get_stat_mod(charisma_score)}\n")
        
    print("\n Stats exported to my_character_sheet.txt")

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
    print(f"STR: {strength_score} {get_stat_mod(strength_score)}")
    print(f"DEX: {dexterity_score} {get_stat_mod(dexterity_score)}")
    print(f"CON: {constitution_score} {get_stat_mod(constitution_score)}")
    print(f"INT: {intelligence_score} {get_stat_mod(intelligence_score)}")
    print(f"WIS: {wisdom_score} {get_stat_mod(wisdom_score)}")
    print(f"CHA: {charisma_score} {get_stat_mod(charisma_score)}")

def calculate_strength(bench_pr=None, pushups=None, long_jump=None):
    global strength_score
    if bench_pr is None:
        bench_pr = get_valid_number("Enter your bench press PR (in pounds): ")
    if pushups is None:
        pushups = get_valid_number("Enter your max push-ups in one set: ")
    if long_jump is None:
        long_jump = get_valid_number("Enter your standing long jump distance (in feet): ")

    bench_pr = round(bench_pr)
    pushups = round(pushups)
    long_jump = round(long_jump)

    strength_score = round(((bench_pr / 15) + (pushups / 3) + (long_jump * 1.5)) / 2.5)
    strength_score = max(1, min(20, strength_score))
    print(f"Your Strength Score is: {strength_score} {get_stat_mod(strength_score)}")

def calculate_dexterity(balance=None, mile=None, burpee=None):
    global dexterity_score
    if balance is None:
        balance = get_valid_integer("Enter how long you can stand on one leg with your eyes closed (in seconds): ")
    if mile is None:
        mile = get_valid_mile_time("Enter your mile time (MM:SS format): ")
    if burpee is None:
        burpee = get_valid_integer("Enter how many burpees you can do in one minute: ")

    dexterity_score = round((balance / 5) + (12 - mile) + (burpee / 5))
    dexterity_score = max(1, min(20, dexterity_score))

    print(f"Your Dexterity Score is: {dexterity_score} {get_stat_mod(dexterity_score)}")

def calculate_constitution(plank=None, breath=None, squats=None):
    global constitution_score
    if plank is None:
        plank = get_valid_number("Enter plank time (in seconds): ")
    if breath is None:
        breath = get_valid_number("Enter breath-hold time (in seconds): ")
    if squats is None:
        squats = get_valid_number("Enter air squats in a minute: ")

    plank = round(plank)
    breath = round(breath)
    squats = round(squats)

    constitution_score = round(((plank / 6) + (10 + breath / 30) + (squats / 4)) / 3)
    constitution_score = max(1, min(20, constitution_score))
    print(f"Your Constitution Score is: {constitution_score} {get_stat_mod(constitution_score)}")

def calculate_intelligence(edu=None, gpa=None):
    global intelligence_score
    if edu is None:
        while True:
            print("Education Level:")
            print("1. High School")
            print("2. Some College")
            print("3. Bachelor's")
            print("4. Master's")
            print("5. Doctorate")
            edu_input = input("Enter number: ")
            if edu_input in {"1", "2", "3", "4", "5"}:
                edu = int(edu_input)
                break
            else:
                print("Invalid selection. Please enter 1-5.")

    if gpa is None:
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

    base = {1: 8, 2: 10, 3: 12, 4: 14, 5: 16}[edu]
    modifier = 2 if gpa >= 4 else 1 if gpa >= 3.5 else 0 if gpa >= 2.5 else -1 if gpa >= 2.0 else -2
    intelligence_score = max(1, min(20, base + modifier))
    print(f"Your Intelligence Score is: {intelligence_score} {get_stat_mod(intelligence_score)}")

def calculate_wisdom(sleep=None, heart=None, outside=None):
    global wisdom_score
    if sleep is None:
        sleep = get_valid_integer("Deep sleep per night (minutes): ")
    if heart is None:
        heart = get_valid_integer("Resting heart rate (BPM): ")
    if outside is None:
        outside = get_valid_integer("Time outside per day (minutes): ")

    wisdom_score = round((sleep / 15) + ((AVERAGE_HEART_RATE - heart) / 5) + (outside / 45))
    wisdom_score = max(1, min(20, wisdom_score))
    print(f"Your Wisdom Score is: {wisdom_score} {get_stat_mod(wisdom_score)}" )

def calculate_charisma(outings=None, interactions=None, dates=None):
    global charisma_score
    if outings is None:
        outings = get_valid_integer("Average outings a week: ")
    if interactions is None:
        interactions = get_valid_integer("Meaningful interactions/day: ")
    if dates is None:
        dates = get_valid_integer("Average dates per month: ")

    charisma_score = round((outings * 1.5) + (interactions / 2) + (dates * 3))
    charisma_score = max(1, min(20, charisma_score))
    print(f"Your Charisma Score is: {charisma_score} {get_stat_mod(charisma_score)}")


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

def get_stat_mod(stat_score = 0):
    if stat_score <= 0:
        return "(-5)"
    else:
        modifier = (stat_score - 10) // 2
        if modifier >= 0:
            return f"(+{modifier})"
        else:
            return f"({modifier})"
    
if __name__ == "__main__":
    main()



