import random

def get_level_settings(level):
    """
    Determines the range of the secret number and the chances allowed
    based on the current level number.
    """
    if 1 <= level <= 5:
        #Levels 1-5: Guess range 1-5, 2 chances
        guess_range = (1, 5)
        chances = 2
    elif 6 <= level <= 10:
        #Levels 6-10: Guess range 6-10, 1 chance
        guess_range = (6, 10)
        chances = 1
    else:
        #Should not happen if main loop is correctly implemented
        raise ValueError("Invalid level number.")
        
    return guess_range, chances

def play_level(level, guess_range, chances):
    min_num, max_num = guess_range
    #Generate the secret number for the current round
    secret_number = random.randint(min_num, max_num)
    
    print(f"\n--- Level {level} ---")
    print(f"You need to guess a number between {min_num} and {max_num}.")
    print(f"You have {chances} chance(s).")
    
 
    for attempt in range(1, chances + 1):
        try:
            #Input/Output for the user
            guess = int(input(f"Attempt {attempt}/{chances}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue #Go to the next attempt

        if guess == secret_number:
            print(f"CORRECT! You guessed the number {secret_number}!")
            return True  #Win
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
    #If the loop finishes without a correct guess
    print(f"Failed! The secret number was {secret_number}.")
    return False #Loss

def main():

    #Initialize game state
    current_level = 1
    TOTAL_LEVELS = 10
    
    print("Welcome to the Guessing Game!")
    
    #Main game loop
    while current_level <= TOTAL_LEVELS:
        
        #Get level parameters
        guess_range, chances = get_level_settings(current_level)
        
        #Play the level and get the result
        level_won = play_level(current_level, guess_range, chances)
        
        #Update the level based on the result
        if level_won:
            #Advance to the next level
            current_level += 1
            if current_level > TOTAL_LEVELS:
                print("\nCONGRATULATIONS! You have completed all 10 levels and won the game!")
                break
        else:
            #Go back one level, but stop at level 1
            if current_level > 1:
                current_level -= 1
                print(f"Moving back to Level {current_level}.")
            else:
                print("You stay at Level 1.")
                
        print("-" * 30)

if __name__ == "__main__":
    main()