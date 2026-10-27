# ------------------------------------------------------
#        Name: Violet McAuliffe
#       Peers: N/A
#  References: Class Slides
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    #planning in a doc string
    """ 1: create a while loop
        2: take input
        3: create conditions """
    #creating my while loop
    while True:
        #making input
        secret_input = input("Give me a word or sentence: ")
        #creating conditionals
        if secret_word in secret_input:
            print("You used the secret word!")
            break
        elif "dog" in secret_input or "Dog" in secret_input:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else:
            print("Try again")
    
# Task 2
def check_greater():
    #creating docstring
    """ 1: take inputs
        2: create conditions and print statements"""
    #creating a while loop
    while True:
        #creating inputs
        num_1 = int(input("Give me a number: "))
        num_2 = int(input("Give me another number: "))
        #creating conditions
        if num_1 > num_2:
            print("First is Greater")
            break
        elif num_1 < num_2:
            print("Second is Greater")
            break
        else:
            print("Try again")
            continue
    
# Task 3
def get_special_numbers():
    #planning it out
    """ 1: make for loop
        2: create conditions"""
    #making my for loop
    for i in range(41):
        #adding conditions
        if i % 2 == 0:
            continue  #continue lets us skip a number if it doesn't meet the condition
        if i % 3 != 0:
            continue
        if i % 5 == 0:
            continue
        #printing all the numbers that pass
        else:
            print(i)
    
# Task 4.a
def my_for_loop():
    """ 1: make for loop
        2:make conditions"""
    #making a for loop that will run exactly once
    for let in range(1):
        let = input("Give me a word: ")
        length = len(let)
        if length < 2 or length > 5:  #first condition
            print("bad word")
            break
        if " " in let:  #second condition
            print("bad word")
            break
        for num in range(length): #if both conditions are met, we move to another for loop to analyze the letters. 
            num = let[num] #this selects the exact letter we are on
            if num == "a" or num == "e" or num == "i" or num == "o" or num == "u" or num == "A" or num == "E" or num == "I" or num == "O" or num == "U":
                print(f"letter {num} is a vowel")
            else:
                print(f"letter {num} is a consonant")  
    
    #Added another docstring here because I had to organize my thoughts
    '''
    Nested? for loop:
    I want to take each letter and run it through conditionals.
    First I need to pick out the letter.
    '''
            
    
# Task 4.b
def my_while_loop():
    """ 1. make my while True to begin
        2. create conditions for a, b, and c
    """
    
    while True:
        menu = input("Please input a, b, or c: ") #first I take the input
        if menu == "a": #Then I create a's condition
            continue
        if menu == "b": #then I create b's condition
            print("Goodbye")
            break
        if menu == "c": # then I create c's condition
            sys.exit()
        else: #last i reloop if the person didn't select a, b, or c
            print("try again")
            continue

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
