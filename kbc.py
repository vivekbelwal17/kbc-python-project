# 1. Define the questions, options, and correct answer (Data Structure)
# Format: ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Option Number"]
questions = [
    ["Which language was used to create this game?", "Python", "French", "JavaScript", "C++", 1],
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["Which data type is used to store a sequence of characters?", "Integer", "Float", "String", "Boolean", 3]
]

# 2. Define the prize money for each level
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money_won = 0

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
    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    
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