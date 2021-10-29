import random

import time

def displayIntro():
  print(''' Hello explorer, you are in a land full of dragons.In your front you can see two caves. In one cave a dragon is friendly, and will share his treausure with you.In The other cave you will find a  greedy and hungry dragon wich will ate you instantley..... ''')

  print()


def chooseCave():
  cave = ''
  while cave != '1' and cave != '2':

    print("Wich cave you want to go into: 1 or 2")
    print()

    cave = input()
    print()

  return cave 


def checkCave(choosenCave):
  print("You approach the cave...")

  print()

  time.sleep(1.5)

  print("It's dark and spooky....")

  time.sleep(1.5)

  print()

  print(''' Once you choose a cave, then the dragon appears in front of you and asks you: ‘Do you really want my treasure?’ , you have to choose if you really want the treasure or you want to go away and don't take any risk. Answer with yes or no. ''')

  print()

  answer = input()

  print()

  if answer == 'yes':
    print("A large dragon jumps out of the cave! He opens his jaw and....")
    print()
    time.sleep(1.5)
  
    friendlyCave = random.randint(1,2)

    if choosenCave == str(friendlyCave):
     print("Gives you his treasure ! ")
     print()
    else:
      print("You're dead :( ")
      print()
  else:

    friendlyCave = random.randint(1,2)
    print('The dragon sees you and says to you from afar in a very somber tone ')
    if choosenCave == str(friendlyCave):
      print('  -Too bad, cause I don’t want my treasure !')
      print()
    else:
     print('   -Good, cause I don’t like greedy people.')
     print()




displayIntro()
caveNumber = chooseCave()
checkCave(caveNumber)
print()

print('Do you want to play again? yes or no ?')

print()

playAgain = input()

print()

if playAgain == 'no':
  print("Have a nice day, see you next time ! ")

while playAgain == 'yes' or playAgain == 'y':
  displayIntro()
  caveNumber = chooseCave()
  checkCave(caveNumber)
  print()
  print('Do you want to play again ? yes or no ? ')
  again = input()
  print()
  if again == 'no':
    print("See you next time ! ")
    break

#The End !