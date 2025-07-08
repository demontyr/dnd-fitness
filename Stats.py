AVERAGE_HEART_RATE= 80
#import yaml

def main(character_sheet="my_character_sheet.txt"):
    strength_score = calculate_strength()
    dexterity_score = calculate_dexterity()
    constitution_score = calculate_constitution()
    intelligence_score = calculate_intelligence()
    wisdom_score = calculate_wisdom()
    charisma_score = calculate_charisma()

     # Print final summary
    # print("\n===== Your Final Stats =====")
    # print(f"STR: {strength_score}")
    # rint(f"DEX: {dexterity_score}")
    # print(f"CON: {constitution_score}")
    # print(f"INT: {intelligence_score}")
    # print(f"WIS: {wisdom_score}")
    # print(f"CHA: {charisma_score}")

    with open(character_sheet, 'w') as f:
        f.write("\n===== Your Final Stats =====\n")
        f.write(f"STR: {strength_score}\n")
        f.write(f"DEX: {dexterity_score}\n")
        f.write(f"CON: {constitution_score}\n")
        f.write(f"INT: {intelligence_score}\n")
        f.write(f"WIS: {wisdom_score}\n")
        f.write(f"CHA: {charisma_score}\n")
    
        

def calculate_strength():
    bench_pr = input("Enter your bench press PR (in pounds): ")
    pushups = input("Enter your max push-ups in one set: ")
    long_jump = input("Enter your standing long jump distance (in feet): ")

    # Check if inputs are valid numbers
    if (bench_pr.replace('.', '', 1).isdigit() and
        pushups.replace('.', '', 1).isdigit() and
        long_jump.replace('.', '', 1).isdigit()):  
        
        # Convert to numbers and round
        bench_pr = round(float(bench_pr))
        pushups = round(float(pushups))
        long_jump = round(float(long_jump))

        #calc Str
        print(f"Inputs accepted: Bench PR = {bench_pr}, Pushups = {pushups}, Long Jump = {long_jump}")
        strength_score = round(((bench_pr / 15) + (pushups / 3) + (long_jump * 1.5)) / 2.5)

        # Ensure the score is between 1 and 20
        strength_score = max(1, min(20, strength_score))

        print(f"Your Strength Score is: {strength_score}")
    else:
        print("Please enter valid numbers in the proper format.")
        return
    
    return strength_score
   
def calculate_dexterity():
    # Get info
    balance = input("Enter how long you can stand on one leg with your eyes closed (in seconds): ")
    mile = input("Enter your mile time (MM:SS format): ")
    burpee = input("Enter how many burpees you can do in one minute: ")

    # Convert balance & burpees to integers
    if balance.isdigit() and burpee.isdigit():
        balance = round(float(balance))
        burpee = round(float(burpee))
    else:
        print("Please enter valid numbers for balance and burpees.")
        return

    # Convert mile time from MM:SS to total minutes
    try:
        minutes, seconds = map(int, mile.split(":"))
        mile = minutes + (seconds / 60)  # Convert to decimal minutes
    except ValueError:
        print("Invalid format. Please enter mile time as MM:SS.")
        
        return

    # Calculate Dexterity score
    dexterity_score = round((balance / 5) + ((12 - (mile * 1.0))) + (burpee / 5))
    dexterity_score = max(1, min(20, dexterity_score))  # Ensure it's between 1-20

    print(f"Inputs accepted: Balance Time = {balance}, Mile Time = {mile}, Burpees = {burpee}")
   
    dexterity_score = max(1, min(20, dexterity_score))

    print(f"Your dexterity Score is: {dexterity_score}")
    return dexterity_score

def calculate_constitution():
    plank_time = input("Enter your max plank hold time (in seconds): ")
    breath_hold = input("Enter your max breath hold time (in seconds): ")
    air_squats = input("Enter your max air squats in one minute: ")

    # Convert inputs to numbers
    try:
        plank_time = round(float(plank_time))
        breath_hold = round(float(breath_hold))
        air_squats = round(float(air_squats))
        print(f"Inputs accepted: Plank Time = {plank_time}, Held Breath Time = {breath_hold}, Squats = {air_squats}")


    except ValueError:
        print("Please enter valid numbers.")
        return

    # Calculate Constitution score
    constitution_score = round(((plank_time / 6) + (10 + breath_hold / 30) + (air_squats / 4)) / 3)
    constitution_score = max(1, min(20, constitution_score))  # Ensure score is between 1 and 20

    print(f"Your Constitution Score is: {constitution_score}")
    return constitution_score

def calculate_intelligence():
    print("Select your highest level of education:")
    print("1. High School Graduate")
    print("2. Some College / Undergraduate")
    print("3. Bachelor's Degree")
    print("4. Master's Degree")
    print("5. Doctorate (PhD, MD, etc.)")

    edu_choice = input("Enter the number corresponding to your education level: ")
    gpa = input("Enter your GPA at your highest level (0.0 - 4.0): ")

    # Validate education choice
    if edu_choice not in {"1", "2", "3", "4", "5"}:
        print("Invalid selection. Please enter a number between 1 and 5.")
        return

    try:
        gpa = float(gpa)
        if gpa < 0 or gpa > 4:
            print("Invalid GPA. Please enter a number between 0.0 and 4.0.")
            return
    except ValueError:
        print("Please enter a valid GPA number.")
        return

    # Assign base intelligence based on education level
    edu_choice = int(edu_choice)
    base_intelligence = {1: 8, 2: 10, 3: 12, 4: 14, 5: 16}[edu_choice]

    # GPA Modifier
    if gpa >= 4.0:
        gpa_modifier = 2
    elif gpa >= 3.5:
        gpa_modifier = 1
    elif gpa >= 2.5:
        gpa_modifier = 0
    elif gpa >= 2.0:
        gpa_modifier = -1
    else:
        gpa_modifier = -2

    # Calculate final intelligence score
    intelligence_score = base_intelligence + gpa_modifier
    intelligence_score = max(1, min(20, intelligence_score))  # Ensure it stays within 1-20
    
    print(f"Inputs accepted: Education Level = {edu_choice}, GPA = {gpa}")
    print(f"Your Intelligence Score is: {intelligence_score}")
    return intelligence_score

def calculate_wisdom():
    '''
    A function that calculates wisdom

    It should have 3 inpute but instead prompts the user for the following inputs
    :param: deep_sleep: The average deep sleep per night in minutes
    :param: resting_heart_rate: ...
    :param: time_outside: hfueiw
    :returns: None

    '''
    # Get user inputs
    deep_sleep = input("Enter your average deep sleep per night (in minutes): ")
    resting_heart_rate = input("Enter your average resting heart rate (in BPM): ")
    time_outside = input("Enter your average time spent outside per day (in minutes): ")

    # Check if all inputs are valid numbers
    if deep_sleep.isdigit() and resting_heart_rate.isdigit() and time_outside.isdigit():
        deep_sleep = round(float(deep_sleep))
        resting_heart_rate = round(float(resting_heart_rate))
        time_outside = round(float(time_outside))
    else:
        print("Please enter valid numbers for all fields.")
        return

    # Wisdom calculation
    wisdom_score = round((deep_sleep / 15) + ((80 - resting_heart_rate) / 5) + (time_outside / 45))
    
    # Ensure the score is between 1 and 20
    wisdom_score = max(1, min(20, wisdom_score))

    # Print input confirmation
    print(f"Inputs accepted: Deep Sleep = {deep_sleep} minutes, Resting Heart Rate = {resting_heart_rate} BPM, Time Outside = {time_outside} minutes")

    # Print final wisdom score
    print(f"Your Wisdom Score is: {wisdom_score}")
    return wisdom_score

def calculate_charisma():
    # Get user input
    outings_per_week = input("How many times do you hang out with non-roomate friends per week? ")
    daily_interactions = input("How many meaningful social interactions do you have per day? ")
    dates_per_month = input("How many dates have you been on in the last month? ")

    # Validate inputs
    if outings_per_week.isdigit() and daily_interactions.isdigit() and dates_per_month.isdigit():
        outings_per_week = int(outings_per_week)
        daily_interactions = int(daily_interactions)
        dates_per_month = int(dates_per_month)
    else:
        print("Please enter valid whole numbers.")
        return
    
    # Display user inputs
    print(f"Inputs accepted: Outings per week = {outings_per_week}, Daily interactions = {daily_interactions}, Dates per month = {dates_per_month}")

    # Calculate Charisma Score
    charisma_score = round((outings_per_week * 1.5) + (daily_interactions / 2) + (dates_per_month * 3))

    # Ensure score is within D&D limits (1-20)
    charisma_score = max(1, min(20, charisma_score))

    # Display the result
    print(f"Your Charisma stat is: {charisma_score}")
    return charisma_score


if __name__ == "__main__":

    # print("In dunder main")

    # Run the function  
    main()

    #print("After main()")




