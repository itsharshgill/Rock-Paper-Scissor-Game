import random
import sys

print('Welcome To My Game!')
# Show Options to User And Take Input.
print('Rock = R, Scissor = S, Paper = P')
print( 'For Quit Enter = Q')
UserChoice = input()
Move = UserChoice

while True:
  
 if UserChoice == 'Q':
   sys.exit()
 elif UserChoice == 'R':
   print('Your Choice = Rock')
  
 elif UserChoice == 'S':
   print('Your Choice = Scissor')
 
 elif UserChoice == 'P':
   print('Your Choice = Paper')

 else:
   print('Wrong Choice')

 break

# Computer Choice

RandomNumber = random.randint(1,3)

if RandomNumber == 1:
  ComputerChoice = 'P'
  print('Computer Choice = Paper')

elif RandomNumber == 2:
  ComputerChoice = 'R'
  print('Computer Choice = Rock')

elif RandomNumber == 3:
  ComputerChoice = 'S'
  print('Computer Choice = Scissor')

# Result

while True:
  if Move == ComputerChoice:
    print('Tie')

  elif Move == 'R' and ComputerChoice =='P':
    print('You Loose!')
    
  elif Move == 'R' and ComputerChoice =='S':
    print('You Won!')

  elif Move == 'S' and ComputerChoice =='P':
    print('You Won')

  elif Move == 'S' and ComputerChoice =='R':
    print('You loose!')

  elif Move == 'P' and ComputerChoice =='S':
    print('You Loose!')

  elif Move == 'P' and ComputerChoice =='R':
    print('You Won')

  break
 
  print('Game End')
