import random


def user_range():
    userRange = input("Please type a number for your range(1-your number): ")
    while not userRange.isdigit():
        print("You must enter a number.")
        break

    secret = random.randint(1, int(userRange)) ## If you want to have it completely random from a set range of numbers, just remove user_range function and enter the max number in range that you want
    count = 0
    
    return int(userRange), secret, count

def user_guess(userRange):
    
    userinp = int(input(f"Please type a guess between 1 and {userRange}: "))
    
    return int(userinp)


def guessing_game():
    usrr, secret, count = user_range()
    
    fun = True

    while fun:

        guess = user_guess(usrr)
        count += 1

        if guess > secret:
            print("Your guess was too high, try again.")
            
        elif guess < secret:
            print("Your guess was too low, try again.")
            
        elif guess == secret:
            if count == 1:
                print("Wow man! firs try! Congratz!!!")
                fun = False
            else:
                print(f"Holy shit you did it dood! in only {count} tries!")   
                fun = False 
        
            

    

if __name__ == "__main__":
    guessing_game()    
