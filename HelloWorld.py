# name = "Uthpalie"
# country = "Australia"

# print(f"Your name is {name}")
# print(f"You live in {country}")

# name = input("Enter your name:")
# age = input("Your age:")


# print(f"Your name is {name}")
# print(f"You are {age} years old")


# name1 = input("What is your name?")
# name2 = input ("What is your neighbours name?")
# duration1 = int(input("How long have you been coding?"))
# duration2 = int(input("How long has your neighbour been coding?"))
# total=duration1+duration2

# print(f"{name1} and {name2} are neighbours")
# print(f"{name1} and {name2} have been coding for {total} years ")

#Initial variable to track if user is playing
user_play ='y'

user_number = int(input("How many numbers?"))

#While Loop followed by For Loop (Nested Loop)
while user_play =='y':
    for number in range(user_number):
        print(number)
    
    user_play = input("Do you wanna still play? (y/n)")
    if user_play == 'y' :

        user_number = int(input("How many numbers?"))
    
    elif user_play == 'n':
        print("Are you sure?")
        user_play = input("Do you wanna still play? (y/n)")
        if user_play == 'y' :

            user_number = int(input("How many numbers?"))
    
    
    

        