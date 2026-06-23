import random
# 1. Define the questions, options, and correct answer (Data Structure)
# Format: ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Option Number"]
questions = [
    ["Which language was used to create this game?", "Python", "French", "JavaScript", "C++", 1],
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["Which data type is used to store a sequence of characters?", "Integer", "Float", "String", "Boolean", 3],
    ["what is the name of your host of this game?", "Amitabh Bachchan", "Shahrukh Khan", "Salman Khan", "Akshay Kumar", 1],
    ["what is the name of hosts unemployed son?", "Amitabh Bachchan""Abhishek Bachchan", "Samay Raina", "Imran Khan", 1]
]

# 2. Define the prize money for each level
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money_won = 0
is_50_50_used = False #track if the life line is used or not 
is_phone_a_friend_used = False #track if the life line is used or not

print("Namashkar, adaab, satsri akaal, abhinandan abhaar\n"
      "Deviyon aur sajjano..\n"
      "Aapka swagat hai Kaun Banega Crorepati ke is khel mein\n"
      "Main hoon aapka host, Amitabh Bachahan\n"
        "Chaliye shuru karte hain khel\n")

# 3. Game Loop
for i in range(len(questions)):
    question = questions[i]
    
    print(f"\nQuestion for Rs. {levels[i]}:")
    print(question[0])
    print(f"1. {question[1]}          2. {question[2]}")
    print(f"3. {question[3]}          4. {question[4]}")
    
    # 4. Take Input & Check Logic
    reply = int(input("Enter your answer (1-4),\n 0 to quit,\n or 5 for 50:50 life line,\n 6 for phone a friend: "))
    if reply == 6:
        if is_phone_a_friend_used == False:
            print("\n life line is activeivated --")
            is_phone_a_friend_used = True
            corect_option = question[-1]
            wrong_options = [1,2,3,4]
            wrong_options.remove(corect_option)
            
            random_wrong = random.choice(wrong_options)
            print("\n computer please call your friend !")
            
            random_friend = random.randint(1,100)
            if random_friend <= 75:
                print(f"your friend is 75% correct answer which  {corect_option}")
            else:
                print(f"your friend is 25% correct answer which  {random_wrong}")
            reply = int(input("Enter your final answer :"))
            
            print(f"the correct answer is either option {corect_option} or option {random_wrong}.")
            #stop player to ask for their final guess
            reply = int(input("Enter your final answer :"))
            
        else :
            print("sorry you have already used your phone a friend life line.")
            reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    
    if reply == 5:
        #check is life line is yoused or not 
        if is_50_50_used == False:
            print("\n--Life line is activeivated --")
            
            #set true value so players can trigger it again 
            is_50_50_used = True
            #grab the correct option by using the last index of the question list
            correct_option = question[-1]
            
            #create a list of options to remove the correct option from the list
            wrong_options =[1,2,3,4]
            wrong_options.remove(correct_option)
            #if the correct answer was 2, wrong_option is now(1,3,4])
            
            #randomly select one of the wrong options to remove from the list
            random_wrong= random.choice(wrong_options)
            print("\n computer please remove two wrong options !")
            
            #display the correct options and the randomly  wrong option to the player 
            print(f"the correct answer is either option {correct_option} or option {random_wrong}.")
            #stop player to ask for their final guess
            reply = int(input("Enter your final answer :"))
            
        else:
            print("sorry you have already used your 50:50 life line.")
            reply = int(input("Enter your answer (1-4) or 0 to quit: "))
            
    #check if the player wants to quit the game
    if reply == 0:
        print("You chose to quit the game.")
        break
        
    if reply == question[-1]:
        print(f"Correct answer! You have won Rs. {levels[i]}")
        money_won = levels[i] # Update guaranteed money
    else:
        print("Galat javab!")
        break

print(f"\nGame Over! You are taking home Rs. {money_won}")