# introduction 
print("Hello, and welcome to Oregon Trail! Today is March 1st and you are currently in Independence, Missouri. You have until December 31st with 2,000 miles to go, 500lbs of food, and 5 health to get to Oregon.") 
print("For each turn you will decide to either travel, rest, hunt, status, help, or quit. However, your health will decrease twice each month and you will eat 5lbs of food a day. Good luck!")

# variables 
health = 5
day1 = 4
day2 = 15
food = 500
miles_left = 2000
current_day = 1
current_month = 3
months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
months_with_30_days = [4, 6, 9, 11]
months_with_28_days = [2]
game_over = False
player_name = str(input("Hello! What is your name? "))

# functions
import random 

def update_days(number_of_days):
    while(number_of_days > 0): 
        add_day()
        number_of_days = number_of_days -1

def add_day():
    global food
    global day1 
    global day2 
    global health
    food = food -5
    global current_month
    global current_day
    global months_with_31_days
    
    if day1 == current_day or day2 == current_day: 
        health = health -1
    if current_day == 31 and current_month in months_with_31_days:
        current_day = 1
        current_month = current_month + 1
    elif current_day == 30 and current_month in months_with_30_days:
        current_day = 1
        current_month = current_month +1
    elif current_day == 28 and current_month in months_with_28_days:
        current_day = 1
        current_month = current_month +1
    else:
        current_day = current_day +1 

def travel():
    global miles_left 
    miles_left = miles_left - random.randint(30,60)
    update_days(random.randint(3,7))
    print("You now have " +  str(miles_left) + " miles left to travel.")

def rest():
    global health 
    if health < 5:
        health = health + 1
        print("Your health is now at " + str(health))
    else: 
        health = 5
        print("Your health is now at " + str(health) + ".")
    update_days(random.randint(2,5))

def hunt():
    global food
    food = food + 100
    print("You now have " + str(food) + " food.")
    update_days(random.randint(2,5))

def status():
    print("Health:" , health)
    print("Food:" , food)
    print("Miles traveled:" ,2000-miles_left)
    print("Today's date: " + str(current_month) +  "/" +  str(current_day))

def help():
    print("The commands that you can type are: travel, rest, hunt, status, and quit.")

def quit():
    game_over = True 
    print("Game over")

# game loop
while (game_over == False):
    user_pick = str(input( player_name +", what would you like to do next? "))

    if user_pick == "travel":
        travel()
    elif user_pick == "rest":
        rest()
    elif user_pick == "hunt":
        hunt()
    elif user_pick == "status":
        status()
    elif user_pick == "help":
        help()
    elif user_pick == "quit":
        quit()
    else:
        print("Sorry, that is not an option.")
    
    if health == 0:
        print("Oh no! Your health is at 0... you died! Game over.")
        game_over = True
    elif food == 0 or (food < 0):
        print("Oh no! You ran out of food... you died! Game over.")
        game_over = True
    elif current_month == 13: 
        print("Oh no! It has been a year and you are still not in Oregon... Game over.")
        game_over = True
    elif miles_left == 0:
        print("Congratulations! You made it to Oregon alive! You won!")
        game_over = True