
# Name: Thea Dagher       Group: A

# 1. What goes in? 
#    The program receives information from two sources: the player and a CSV file.
# -Player's name: The player enters their name.
# - Difficulty level: The player chooses Easy (E) or Hard (H).
# - Easy: Starting budget of €15,000.
# - Hard: Starting budget of €6,000.
# - Player's decisions: Each day, the player chooses one of three options (A, B or C).
# - Scenario file (scenarios_A.csv): Contains the situations, three possible choices, their budget and reputation changes, and feedback for each choice.

# 2. What happens? 
#The program follows several steps:
# 1. Loads the scenarios: Reads the scenarios from the CSV file and checks that the required information is available.
# 2. Initializes the game: Asks for the player's name and difficulty, then sets the starting budget and reputation (50 points).
# 3. Randomizes the scenarios: Shuffles the scenarios and selects the first 10.
# 4. Runs the game: For each day:
#    - Displays the situation and three possible choices.
#    - Asks the player to choose A, B or C.
#   - Updates the budget and reputation according to the decision.
#   - Displays feedback explaining the consequences.
#   - Records the decision in the game history.
# 5. Checks game over: If the budget or reputation reaches zero or below, the game stops immediately.
# 6. Calculates the final result: Calculates a score based on the remaining budget and reputation and assigns a final title.
#7. Saves the results: Records the player's name, final budget, reputation, title and date in results.csv.

# 3. What comes out? 
#The program produces three main outputs:
#- On-screen information: Daily scenarios, available choices, updated budget and reputation, and feedback.
#- Final results: The player's remaining budget, reputation, final score and title:
#  - Eternal Intern
#  - Growth Hacker
#  - CMO Material
#  - Viral Legend
#  - Fired (if the budget or reputation reaches zero or below).
# - Game history: Displays the best and worst decisions based on their reputation changes.
# It also creates or updates results.csv, storing the final results for future reference.

# 4. What could go wrong? 
# Some possible problems include:
# - Missing CSV file: If scenarios_A.csv is missing, the game stops and displays an error.
# - Incorrect CSV format: If a required column is missing or a budget/reputation value is not a valid number, the program displays an error.
# - Invalid player input: If the player enters something other than E/H or A/B/C, the program asks them to try again.
# - Empty scenario file: If the CSV contains no scenarios, the game could finish without playing any days.
# - Too few scenarios: If there are fewer than 10 scenarios, the game will play fewer than 10 days.
# - Missing results file permissions: If the program cannot create or write to results.csv, saving the results will fail.
#- Unexpected negative values: A choice could reduce the budget or reputation below zero, immediately ending the game.

# Feature chosen: d (Difficulty)
# Why: I chose the difficulty feature because it directly affects the player's starting budget and therefore the overall challenge of the game.
# The player can choose between:
# - Easy mode: €15,000 starting budget.
# - Hard mode: €6,000 starting budget.
# This feature makes the game more flexible and accessible to different players. It also creates different levels of difficulty without changing the scenarios or the game rules.
# =====================================================================
 
import csv
import random
from datetime import date
 
# The game settings, kept in one place so they are easy to change
SCENARIO_FILE = "scenarios_A.csv"
RESULTS_FILE = "results.csv"
STARTING_REPUTATION = 50
MAX_REPUTATION = 100
DAYS = 10
 
def load_scenarios(filename):
    scenarios = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            options = {}
            for letter in ("A", "B", "C"):
                options[letter] = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter],
                )
            scenarios.append({"situation": row["Scenario"], "options": options})
    return scenarios
 
 
# Feature d: asks for the difficulty and returns the starting budget
def ask_difficulty():
    answer = input("Difficulty: (E)asy or (H)ard? ").strip().upper()
    while answer not in ("E", "H"):
        answer = input("Please type E or H: ").strip().upper()
    if answer == "E":
        return 15000
    return 6000
 
 
# Keeps asking until the player types A, B or C (small letters work too)
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in ("A", "B", "C"):
        answer = input("Please type A, B or C: ").strip().upper()
    return answer
 
 
# Shows the day number, both gauges, the situation and the three options
def show_day(day, budget, reputation, scenario):
    print()
    print(f"--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/{MAX_REPUTATION}]")
    print(scenario["situation"])
    for letter in ("A", "B", "C"):
        print(f"  {letter}: {scenario['options'][letter][0]}")
 
 
# Applies one option to the two gauges and returns them as a tuple
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation
 
 
# Turns the final gauges into a title, using the score table
def get_title(budget, reputation):
    if budget <= 0 or reputation <= 0:
        return "Fired"
    score = reputation + budget // 200
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    return "Viral Legend"
 
 
# Shows the best and worst move, using the history.
# Each history tuple starts with the reputation change, so max() and min()
# compare on that first.
def show_best_and_worst(history):
    if not history:
        return
    best = max(history)
    worst = min(history)
    print()
    print(f'Best move:  day {best[1]}, "{best[2]}" ({best[0]:+d})')
    print(f'Worst move: day {worst[1]}, "{worst[2]}" ({worst[0]:+d})')
 
 
# Adds one line at the end of results.csv: name, budget, reputation, title, date
def save_result(name, budget, reputation, title):
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])
 
 
# Runs the whole game from start to end
def main():
    # Load the scenarios, stop cleanly if the file is missing or broken
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print(f"Error: {SCENARIO_FILE} not found. Put it next to this file.")
        return
    except (KeyError, ValueError):
        print(f"Error: {SCENARIO_FILE} has a wrong column or a number that is not a number.")
        return
 
    # Ask the name (ask again if empty) and the difficulty
    name = input("What is your name? ").strip()
    while name == "":
        name = input("Please type your name: ").strip()
    budget = ask_difficulty()
    reputation = STARTING_REPUTATION
 
    # Shuffle and keep the first 10 scenarios
    random.shuffle(scenarios)
    history = []
 
    # Play the days
    for day, scenario in enumerate(scenarios[:DAYS], start=1):
        show_day(day, budget, reputation, scenario)
        letter = ask_choice()
        option = scenario["options"][letter]
        budget, reputation = apply_choice(budget, reputation, option)
        text, budget_change, reputation_change, feedback = option
        print(feedback)
        print(f"Budget {budget_change:+d} EUR, Reputation {reputation_change:+d}")
        history.append((reputation_change, day, text))
 
        # Game over: stop at once
        if budget <= 0 or reputation <= 0:
            break
 
    # Show the result
    print()
    print("=" * 32)
    title = get_title(budget, reputation)
    if title == "Fired":
        print(f"{name}, you are FIRED!")
        if budget <= 0:
            print(f"Why: the budget ran out ({budget} EUR).")
        if reputation <= 0:
            print(f"Why: the reputation hit zero ({reputation}/{MAX_REPUTATION}).")
    else:
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print(f"Final score: {reputation + budget // 200}")
        print(f"{name}, your title: {title}")
 
    show_best_and_worst(history)
    save_result(name, budget, reputation, title)
    print(f"Saved in {RESULTS_FILE}")
 
 
# Start the game only when the file is run directly
if __name__ == "__main__":
    main()
 