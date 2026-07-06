Name = input ("Hello, what's your name?")
print ("Hello ", Name, " welcome to the hacking simulator.")
person = input ("Which person do you want to hack? Level 1: Thomas, Level 2: Noah, Level 2: Maria, Level 3: Elijah, Level 3, Sienna")
if person == ("Thomas"):
    print ("Here is Thomas' profile: Date of birth: 1/5/1998, Favourite colour: Blue, Pet: Dog named Frodo Waggins, Family: Wife (Amelia, 18/11/1999), Child (Oliver, 19/8/2024)")
    Guess = input ("What is your password guess")
    if Guess == ("Frodo"):
        print ("You guessed correctly!")
    else:
        Guess2 = input ("What is your second guess?")
        if Guess2 == ("Frodo"):
            print ("You guessed correctly!")
        else:
            Guess3 = input ("What is your thrird guess?")
            if Guess3 == ("Frodo"):
                print ("You have guessed correctly")
            else:
                Guess4 = input ("What is your fourth guess?")
                if Guess4 == ("Frodo"):
                    print ("You have guessed correctly.")
                else:
                    Guess5 = input ("What is your final guess?")
                    if Guess5 == ("Frodo"):
                        print ("You have guessed correctly.")
                    else:
                        print ("You might need to practice a bit! Try again!")
