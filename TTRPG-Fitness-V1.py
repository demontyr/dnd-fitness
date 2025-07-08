import random

class FitnessRPG:
    def __init__(self):
        self.xp = 0
        self.end = False
        self.gold = 0
        self.quests = [
            {"text": "Walk 10,000 steps", "xp": 10, "gold": 5},
            {"text": "Drink 2 liters of water", "xp": 5, "gold": 3},
            {"text": "Do 20 push-ups", "xp": 15, "gold": 7},
        ]
        self.encounters = [
            {
                "text": "A bandit ambushes you!",
                "options": [
                    {"text": "Fight! (Do 15 squats)", "xp": 10, "gold": 5},
                    {"text": "Run! (Do 30 seconds of jumping jacks)", "xp": 7, "gold": 3},
                ],
            },
            {
                "text": "You find a treasure chest!",
                "options": [
                    {"text": "Lift it! (Do 10 deadlifts)", "xp": 12, "gold": 6},
                    {"text": "Pick the lock! (Do 15 Russian Twists)", "xp": 8, "gold": 4},
                ],
            },
        ]

    def complete_quest(self, quest):
        self.xp += quest["xp"]
        self.gold += quest["gold"]
        print(f"Completed: {quest['text']} (+{quest['xp']} XP, +{quest['gold']} Gold)")

    def trigger_encounter(self):
        encounter = random.choice(self.encounters)
        print(encounter["text"])
        for i, option in enumerate(encounter["options"], 1):
            print(f"{i}. {option['text']} (+{option['xp']} XP, +{option['gold']} Gold)")
        choice = int(input("Choose an option (1 or 2): ")) - 1
        self.complete_quest(encounter["options"][choice])

    def show_status(self):
        print(f"XP: {self.xp} | Gold: {self.gold}\n")

if __name__ == "__main__":
    game = FitnessRPG()
    while not game.end:
        print("1. Complete a Quest")
        print("2. Trigger a Random Encounter")
        print("3. Show Status")
        print("4. Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            for i, quest in enumerate(game.quests, 1):
                print(f"{i}. {quest['text']} (+{quest['xp']} XP, +{quest['gold']} Gold)")
            q_choice = int(input("Select a quest: ")) - 1
            game.complete_quest(game.quests[q_choice])
        elif choice == "2":
            game.trigger_encounter()
        elif choice == "3":
            game.show_status()
        elif choice == "4":
            game.end = True
        else:
            print("Invalid choice, try again.")

    
        


