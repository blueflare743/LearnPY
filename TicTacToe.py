
print('Welcome to Tic Tac Toe!')
player_one = 'false'

lst = ['X', 'O']
while player_one != 'X' and player_one!='O' and player_one != 'x' and player_one != 'o':
       player_one = input('Player One: Would you like to play as X or O?')
if player_one == 'X':
    player_two = 'O'
elif player_one == 'O':
    player_two = 'X'
def store_inputs():
    g = 'f'
    while g != 'Yes' and 'No' and 'yes' and 'no ':
      g = input('Would you like to start the game?')
store_inputs()    
def display(board):
    for i in range(1,11):
      x = i + 1
      y = i + 1
      if x % 2 != 0:
        u = 'player one'
      else:
        u = 'player_two'
        
      # player one odd player 2 even 
      for x in range(1,  10):
         if board[x] == board[x+1] == board[x + 2]:
          print('Game Over!, {} Won!'.format(u))
          break
         elif  board[x] == board[x+2] == board[x + 4]:
          print('Game Over!, {} Won!'.format(u))
          break
         elif board[x] == board[x+4]  == board[x+8]:
          print('Game Over!, {} Won!'.format(u))
          break
         elif board[x] == board[x+3]  == board[x+6]:
           print('Game Over!, {} Won!'.format(u))
           break
      print( '     |       |     ')
      print('  {}  |  {}    |  {}  '.format(board[7], board[8], board[9]))
      print( '     |       |     ')
      print( '-------------------')
      print( '     |       |     ')
      print('  {}  |  {}    |  {}  '.format(board[4], board[5], board[6]))
      print( '     |       |     ')
      print( '-------------------')
      print( '     |       |     ')
      print('  {}  |  {}    |  {}  '.format(board[1], board[2], board[3]))
      print( '     |       |     ')
      print()
      inp = int(input('Choose your next position: (1-9)'))
      global player_one
      global player_two
      if y  % 2 == 0:
        board[inp] = player_one
      elif y % 2 != 0:
        board[inp] = player_two 
display(['#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])    
        
          