#Guessing Number Game
from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work.
answer=randint(1,10)
import sys  #for terminal
answer=randint(int(sys.argv[1]),int(sys.argv[2])) #for terminal

while True:
  try:
    guess=int(input('guess a number 1~10: '))
    guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))  #for terminal
    if 0<guess<11:
      if guess==answer:
        print('you are a genius!')
        break
    else:
      print('hey boze, I said 1~10')
  except ValueError:
    print('please enter a number')
    continue