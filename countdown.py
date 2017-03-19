#Creating my list of  words to reference

text_file = open("words.txt", "r")
listofwords = text_file.readlines()
text_file.close()
#removing the /n from the end of each word within the list
newlistofwords = [x[:-2] for x in listofwords]

#creating the randomly generated 9 character string
#want to let the player choose number of vowels and consonants
import random
cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vow = ["a","e","i","o","u"]
bigones = [100,75,50,25]
littleones = [1,2,3,4,5,6,7,8,9]

#adding a timer function to the game so that after 30 seconds the game says time up
from threading import Timer
import time
#defining a timeout function- currently just pops up when 30 secs have passed. want to add in input
def timeout():
    print("Ok Times up!")
    
#defining a function that prints the random sample at the beginning of a new round
#below code says the number of vows and cons that the sample will generate
#want player to be ble to change this moving forward - default 6 cons, 3 vows

randomletters = random.sample(cons, 6) + random.sample(vow, 3)

def newround():
    print("Here are your letters, goodluck!")    
    print(randomletters) 
    t = Timer(1 * 30, timeout)
    t.start()

#starting the game
p1name = input("Hi Player 1, what is your name? ")
p2name = input("Hi Player 2, what is your name? ")
print("Ok " + p1name + " and " + p2name +" let's start round 1")
p1points = 0
p2points = 0

#round 1
newround()
#have to put the following line in to delay the following code, because newround takes 30 secs to run
time.sleep(31)
p1guess = input("Ok " + p1name + ", what word have you got? ")
p2guess = input("Ok " + p2name + ", what word have you got? ")
p1guessletters = list(p1guess)
p2guessletters = list(p2guess)
p1guesscorrect = set(p1guessletters).issubset(randomletters)
p2guesscorrect = set(p2guessletters).issubset(randomletters)
#below calculates points for round one - checks against the dict
if p1guess in newlistofwords and p1guesscorrect is True:
    print("Yes! " + p1name + ", " + p1guess + " is a correct answer")
    print(p1name + " that scores " + str(len(p1guess)) + " points!")
    p1points = p1points + len(p1guess)
else:
    if p1guess in newlistofwords and p1guesscorrect is False:
        print("sorry " + p1name + " you didn't use the correct letters")
        p1points = p1points
    elif p1guess not in newlistofwords and p1guesscorrect is True:
        print("sorry " +p1name + " doesn't appear in our dictionary")
    else:
        print(p1name + "You seem to have used random letters to create a word that isn't even in the dictionary, please try harder next time" )
    
if p2guess in newlistofwords and p2guesscorrect is True:
    print("Yes! " + p2name + ", " + p2guess + " is a correct answer")
    print(p2name + " that scores " + str(len(p2guess)) + " points!")
    p2points = p2points + len(p2guess)
else:
    if p1guess in newlistofwords and p2guesscorrect is False:
        print("sorry " + p2name + " you didn't use the correct letters")
        p2points = p2points
    elif p2guess not in newlistofwords and p2guesscorrect is True:
        print("sorry " +p2name + " doesn't appear in our dictionary")
    else:
        print(p2name + "You seem to have used random letters to create a word that isn't even in the dictionary, please try harder next time" )
 
print("So at the end of round 1 " + p1name + " has " + str(p1points) + " points" + " and " + p2name + " has " + str(p2points) + " points")

#round 2
#this pretty much repeats round one but totals the points at the end
time.sleep(5)
print("Ok, now for round 2, are you ready?")
time.sleep(5)
newround()
time.sleep(31)
p1guess = input("Ok " + p1name + ", what word have you got? ")
p2guess = input("Ok " + p2name + ", what word have you got? ")
p1guessletters = list(p1guess)
p2guessletters = list(p2guess)
p1guesscorrect = set(p1guessletters).issubset(randomletters)
p2guesscorrect = set(p2guessletters).issubset(randomletters)
#below calculates points for round one - checks against the dict
if p1guess in newlistofwords and p1guesscorrect is True:
    print("Yes! " + p1name + ", " + p1guess + " is a correct answer")
    print(p1name + " that scores " + str(len(p1guess)) + " points!")
    p1points = p1points + len(p1guess)
else:
    if p1guess in newlistofwords and p1guesscorrect is False:
        print("sorry " + p1name + " you didn't use the correct letters")
        p1points = p1points
    elif p1guess not in newlistofwords and p1guesscorrect is True:
        print("sorry " +p1name + " doesn't appear in our dictionary")
    else:
        print(p1name + "You seem to have used random letters to create a word that isn't even in the dictionary, please try harder next time" )
    
if p2guess in newlistofwords and p2guesscorrect is True:
    print("Yes! " + p2name + ", " + p2guess + " is a correct answer")
    print(p2name + " that scores " + str(len(p2guess)) + " points!")
    p2points = p2points + len(p2guess)
else:
    if p1guess in newlistofwords and p2guesscorrect is False:
        print("sorry " + p2name + " you didn't use the correct letters")
        p2points = p2points
    elif p2guess not in newlistofwords and p2guesscorrect is True:
        print("sorry " +p2name + " doesn't appear in our dictionary")
    else:
        print(p2name + "You seem to have used random letters to create a word that isn't even in the dictionary, please try harder next time" )

print("So at the end of round 2 " + p1name + " has " + str(p1points) + " points" + " and " + p2name + " has " + str(p2points) + " points")

#round 3
#this round is a numbers round and totals the points at the end
time.sleep(5)
print("Ok, " + p1name + " it's your numbers round. Lets start off.. ")
bigonesinput = input("How many big ones would you like? ")
littleonesinput = 6-int(bigonesinput)
print ("Fab! So that's " + str(bigonesinput) + " big ones and " + str(littleonesinput) + " small ones")
time.sleep(5)

def newnumround():
    print(random.sample(bigones, int(bigonesinput)) + random.sample(littleones, int(littleonesinput)))
    t1 = Timer(1 * 30, timeout)
    t1.start() 
    
targetno = str(random.randint(100,999))
newnumround()
#below calculates the number that they're trying to get to
print("and the number we are trying to get is..." + targetno)
time.sleep(31)
p1guess = input("Ok " + p1name + ", what have you got? ")
p2guess = input("Ok " + p2name + ", what have you got? ")
#below calculates points for round three

#FIRST OUTCOME

#if player one is closer than player 2...
if (int(targetno)-int(p1guess))<(int(targetno)-int(p2guess)):
    print("Yes! " + p1name + " you're the closest!")
#make player 1 prove they did it right
    p1working = input("tell us how you got your answer:")
#if their workings = their guess then points for them
    print(int(eval(p1working)))
    if int(eval(p1working)) == int(p1guess):
        print("Well done! 10 points for " + p1name)
        p1points = p1points + 10
#if not, lets give player 2 a chance
    else:
        print("Unlucky, 0 points for you, " + p2name + " can you do any better?")
        p2working = eval(input("tell us how you got your answer:"))
#if player 2 is correct then points
        if int(eval(p2working)) == int(p2guess):
                print("Well done! 10 points for " + p2name)
                p2points = p2points + 10
#if not then no points for anyone
        else:
                print("no points this time!")
                p1points = p1points
                p2points = p2points

#OUTCOME 2

#if player two is closer than player one...
if (int(targetno)-int(p2guess))<(int(targetno)-int(p1guess)):
    print("Yes! " + p2name + " you're the closest!")
#make player 2 prove they did it right
    p2working = eval(input(" tell us how you got your answer:"))
#if their workings = their guess then points for them
    if int(eval(p2working)) == int(p2guess):
        print("Well done! 10 points for " + p2name)
        p2points = p2points + 10
#if not, lets give player 1 a chance
    else:
        print("Unlucky, 0 points for you, " + p1name + " can you do any better?")
        p1working = eval(input(" tell us how you got your answer:"))
#if player 1 is correct then points
        if eval(p1working) == p1guess:
                print("Well done! 10 points for " + p1name)
                p1points = p1points + 10
#if not then no points for anyone
        else:
                print("no points this time!")
                p1points = p1points
                p2points = p2points
                
 #OUTCOME 3
                
#if both players get to the same number
if (int(targetno)-int(p1guess)) == (int(targetno)-int(p2guess)):
    print("Let's see how you both did it...")
#make players prove they did it right
    p1working = eval(input(p1name + " tell us how you got your answer:"))
    p2working = eval(input(p2name + " tell us how you got your answer:"))
#if their workings = their guess then points for them
    if eval(int(p1working)) == p1guess:
        print("Well done! 10 points for " + p1name)
        p1points = p1points + 10
#lets give player 2 a chance
    else:
        print("Unlucky," + p1name +" 0 points for you, ")
        p1points=p1points
#if their workings = their guess then points for them
    if eval(p2working) == p2guess:
        print("Well done! 10 points for " + p2name)
        p2points = p2points + 10
#if not, lets give player 1 a chance
    else:
        print("Unlucky," + p2name +" 0 points for you, ")
        p2points=p2points     

    

print("So at the end of round 3 " + p1name + " has " + str(p1points) + " points" + " and " + p2name + " has " + str(p2points) + " points")

#round 4
#this round is a numbers round and totals the points at the end
time.sleep(5)
print("Ok, " + p2name + " it's your numbers round. Lets start off.. ")
bigonesinput = input("How many big ones would you like? ")
littleonesinput = 6-int(bigonesinput)
print ("Fab! So that's " + str(bigonesinput) + " big ones and " + str(littleonesinput) + " small ones")
time.sleep(5)

def newnumround():
    print(random.sample(bigones, int(bigonesinput)) + random.sample(littleones, int(littleonesinput)))
    t1 = Timer(1 * 30, timeout)
    t1.start() 
    
targetno = str(random.randint(100,999))
newnumround()
#below calculates the number that they're trying to get to
print("and the number we are trying to get is..." + targetno)
time.sleep(31)
p1guess = input("Ok " + p1name + ", what have you got? ")
p2guess = input("Ok " + p2name + ", what have you got? ")
#below calculates points for round three

#FIRST OUTCOME

#if player one is closer then player 2...
if (int(targetno)-int(p1guess))<(int(targetno)-int(p2guess)):
    print("Yes! " + p1name + " you're the closest!")
#make player 1 prove they did it right
    p1working = input("tell us how you got your answer:")
#if their workings = their guess then points for them
    print(int(eval(p1working)))
    if int(eval(p1working)) == int(p1guess):
        print("Well done! 10 points for " + p1name)
        p1points = p1points + 10
#if not, lets give player 2 a chance
    else:
        print("Unlucky, 0 points for you, " + p2name + " can you do any better?")
        p2working = eval(input("tell us how you got your answer:"))
#if player 2 is correct then points
        if int(eval(p2working)) == int(p2guess):
                print("Well done! 10 points for " + p2name)
                p2points = p2points + 10
#if not then no points for anyone
        else:
                print("no points this time!")
                p1points = p1points
                p2points = p2points

#OUTCOME 2

#if player two is closer then player one...
if (int(targetno)-int(p2guess))<(int(targetno)-int(p1guess)):
    print("Yes! " + p2name + "you're the closest!")
#make player 2 prove they did it right
    p2working = eval(input("tell us how you got your answer:"))
#if their workings = their guess then points for them
    if eval(int(p2working)) == int(p2guess):
        print("Well done! 10 points for " + p2name)
        p2points = p2points + 10
#if not, lets give player 1 a chance
    else:
        print("Unlucky, 0 points for you, " + p1name + " can you do any better?")
        p1working = eval(input("tell us how you got your answer:"))
#if player 1 is correct then points
        if eval(p1working) == p1guess:
                print("Well done! 10 points for " + p1name)
                p1points = p1points + 10
#if not then no points for anyone
        else:
                print("no points this time!")
                p1points = p1points
                p2points = p2points
                
 #OUTCOME 3
                
#if both players get to the same number
if (int(targetno)-int(p1guess)) == (int(targetno)-int(p2guess)):
    print("Let's see how you both did it...")
#make players prove they did it right
    p1working = eval(input(p1name + " tell us how you got your answer:"))
    p2working = eval(input(p2name + " tell us how you got your answer:"))
#if their workings = their guess then points for them
    if eval(int(p1working)) == p1guess:
        print("Well done! 10 points for " + p1name)
        p1points = p1points + 10
#lets give player 2 a chance
    else:
        print("Unlucky," + p1name +" 0 points for you, ")
        p1points=p1points
#if their workings = their guess then points for them
    if eval(p2working) == p2guess:
        print("Well done! 10 points for " + p2name)
        p2points = p2points + 10
#if not, lets give player 1 a chance
    else:
        print("Unlucky," + p2name +" 0 points for you, ")
        p2points=p2points     

print("So at the end of round 4 " + p1name + " has " + str(p1points) + " points" + " and " + p2name + " has " + str(p2points) + " points")
time.sleep(5)
print("This is the final  round...")

#round 5
newround()
#have to put the following line in to delay the following code, because newround takes 30 secs to run
time.sleep(31)
p1guess = input("Ok " + p1name + ", what word have you got? ")
p2guess = input("Ok " + p2name + ", what word have you got? ")
p1guessletters = list(p1guess)
p2guessletters = list(p2guess)
p1guesscorrect = set(p1guessletters).issubset(randomletters)
p2guesscorrect = set(p2guessletters).issubset(randomletters)
#below calculates points for round one - checks against the dict
if p1guess in newlistofwords and p1guesscorrect is True:
    print("Yes! " + p1name + ", " + p1guess + " is a correct answer")
    print(p1name + " that scores " + str(len(p1guess)) + " points!")
    p1points = p1points + len(p1guess)
else:
    if p1guess in newlistofwords and p1guesscorrect is False:
        print("sorry " + p1name + " you didn't use the correct letters")
        p1points = p1points
    elif p1guess not in newlistofwords and p1guesscorrect is True:
        print("sorry " +p1name + " doesn't appear in our dictionary")
    else:
        print(p1name + "You seem to have used random letters to create a word that isn't even in the dictionary, please try harder next time" )
    
if p2guess in newlistofwords and p2guesscorrect is True:
    print("Yes! " + p2name + ", " + p2guess + " is a correct answer")
    print(p2name + " that scores " + str(len(p2guess)) + " points!")
    p2points = p2points + len(p2guess)
else:
    if p1guess in newlistofwords and p2guesscorrect is False:
        print("sorry " + p2name + " you didn't use the correct letters")
        p2points = p2points
    elif p2guess not in newlistofwords and p2guesscorrect is True:
        print("sorry " +p2name + " doesn't appear in our dictionary")
    else:
        print(p2name + "You seem to have used random letters to create a word that isn't even in the dictionary, please try harder next time" )

#end of the game
print("So at the end of the game " + p1name + " has " + str(p1points) + " points" + " and " + p2name + " has " + str(p2points) + " points")
if p1points>p2points:
    print("Congratulations " + p1name + " you are the winner with " + p1points + " points")
elif p1points<p2points:
    print("Congratulations " + p2name + " you are the winner with " + p2points + " points")
else:
    print("It's a draw! ")
