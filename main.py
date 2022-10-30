import turtle
import random

#SET UP THE GAME BOARD AND PLAYERS

wn=turtle.Screen()
wn.screensize(canvheight=450, canvwidth=850)
wn.bgpic("p1_snail_board.gif")
turtle.register_shape("p1_pink.gif")
pinkT = turtle.Turtle()
pinkT.shape("p1_pink.gif")
pinkT.up()
pinkT.setpos(375, -25)

turtle.register_shape("p1_blue.gif")
blueT = turtle.Turtle()
blueT.shape("p1_blue.gif")
blueT.up()
blueT.setpos(375,-85)

turtle.register_shape("p1_orange.gif")
orangeT = turtle.Turtle()
orangeT.shape("p1_orange.gif")
orangeT.up()
orangeT.setpos(375,-145)

turtle.register_shape("p1_green.gif")
greenT = turtle.Turtle()
greenT.shape("p1_green.gif")
greenT.up()
greenT.setpos(375,25)

turtle.register_shape("p1_yellow.gif")
yellowT = turtle.Turtle()
yellowT.shape("p1_yellow.gif")
yellowT.up()
yellowT.setpos(375,85)

turtle.register_shape("p1_red.gif")
redT = turtle.Turtle()
redT.shape("p1_red.gif")
redT.up()
redT.setpos(375,145)


    
def roll(winners):
  a =random.randrange(1,7)
  if a == 1 and orangeT.pos()[0] > -385:
    orangeT.backward(95)
    if orangeT.pos()[0] <= -385:
      winners.append("orange")
  elif a == 2 and blueT.pos()[0]> -385:
    blueT.backward(95)
    if blueT.pos()[0] <= -385:
      winners.append("blue")
  elif a == 3 and greenT.pos()[0]> -385:
    greenT.backward(95)
    if greenT.pos()[0] <= -385:
      winners.append("green")
  elif a == 4 and yellowT.pos()[0]> -385:
    yellowT.backward(95)
    if yellowT.pos()[0] <= -385:
      winners.append("yellow")
  elif a == 5 and redT.pos()[0]> -385:
    redT.backward(95)
    if redT.pos()[0] <= -385:
      winners.append("red")
  elif pinkT.pos()[0]> -385:
    pinkT.backward(95)
    if pinkT.pos()[0] <= -385:
      winners.append("pink")
  return winners


player_count = int(input("how many players will there be?:"))

def first_roll():
  if player_count == 2:
    for i in range(player_count*2):
      roll('winners')
  elif player_count == 3:
    for i in range(player_count*2):
      roll('winners')
  elif player_count == 4:
    for i in range(player_count*2):
      roll('winners')
  else:
    print('Please enter between 2 and 4 players')
    

def guess_time():
  win = []
  lose = []
  for i in range(player_count):
    guess = input("which color do you think will finish first? ")
    win.append(guess)
    guess = input("which color do you think will finish last? ")
    lose.append(guess)
  return win, lose
  

def main():
  first_roll()

  
  a, b =guess_time()
  winners = []
  winners = roll(winners)
  while len(winners) < 6:
    winners = roll(winners) 
  win=False

  lose=False
  print(winners[0], "snail finished first")
  
  
  print(winners[-1], "snail finished last")
  
  for i in range(len(a)):
    if winners[0] == a[i]:
      print('the winner is player (predicted winner):' , i+1)
      win = True

    if winners[-1] == a[i]:
      print('the winner is player (predicted loser):' , i+1)
      lose = True
      
  if not win:
    print('no one guessed winners correctly')


  if not lose:
    print('no one guessed losers correctly')
  
main()
wn.exitonclick() 

"""
Sravya: 97/100
Great job! 
1) Accepting more than 4 players
2) Accepting wrong guesses. For example, your program accepts "bus" as a valid guess
3) Code is readable
4) Nice job on multiple functions
"""
