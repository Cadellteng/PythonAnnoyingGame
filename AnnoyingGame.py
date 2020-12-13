#python 2.7.15
import random

print "Annoying Game"

greetings = ["Hello", "Screw you", "You got no money", "Nice to e-meet you", "You so pretty", "You are brilliant", "You are a genius", "You are Jesus! Bless me"]

name = ""

while name != "exit":
  n = random.randint(0, 7)
  name = raw_input("What is your name? ")
  print(greetings[n] + ", " + str(name))
  
print ("You exit the game, now buzz off")
