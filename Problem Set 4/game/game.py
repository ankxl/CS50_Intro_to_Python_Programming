import random
import sys

def main():
    n = get_input("Level: ")
    ch = random.randint(1,n)
    check_guess("Guess: ",ch)


def get_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
        except ValueError:
            pass

def check_guess(prompt,ch):

    while True:
        guess = get_input(prompt)
        
        if guess < ch:
            print("Too small!")
        elif guess > ch:
            print("Too large!")
        else:
            sys.exit("Just right!")


main()
