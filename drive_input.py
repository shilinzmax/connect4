'''
CS 5001
Spring 2020
Project
drive_input.py
This version is tpying the column number into the terminal and show the color ball in the turtle screen
'''

import turtle
from game import Game
from aturtle import Aturtle



#initialize the size of grid:
col = input("please input the number of colum (4--7)")
while ord(col) < 52 or ord(col) > 55:
           col = input("The number is out of the range. please input the number of colum (4--7)")
row = input("please input the number of row (4--8)")
while ord(row) < 52 or ord(row) > 55:
           row = input("The number is out of the range. please input the number of colum (4--7)")


           
col = int(col)
row = int(row)
gridd = [[0 for c in range(col)] for x in range(row)]

#initialize turtle
tur = Aturtle()

#draw the grid board before the game start
tur.draw_board()
tur.draw_grid(gridd, row, col)
tur.draw_game_panel()


gm = Game()

#everytime we play the game and store the score into the file:connect4
gm.initialize_score("connect4")
tur.show_score(gm.red, gm.yellow)


def play_game(num):
                      '''
                      function: play_game
                      parameter: num(int) add one every time in the while loop to change the ball color
                      does: show the color ball on the screen till the winner appear or the board is full
                      
                      '''
                      col = len(gridd[0])
                      row = len(gridd)
                   
                      while tur.is_win(gridd, 1, row, col) == False and tur.is_win(gridd,2, row, col) == False and tur.is_full(gridd,row, col) == False:
                                 tur.color_turn(num+1)
                                 user_input = input("Please enter the column number\n")
                                 while ord(user_input) < 49 or ord(user_input) > ord(str(col)):
                                            user_input = input("Your input is out of the range, please enter the column\n")
                                 
                                 coll = int(user_input)
                                 if gridd[0][coll-1] != 0:
                                            print("This column is full, please enter the column")

                                 else:
                                            roww = row
                                            count = roww-1
                                            while gridd[count][coll-1] != 0:
                                                       count = count - 1
                                            gridd[count][coll-1] = num%2+1
                                            tur.draw_grid(gridd, row, col)
                                 num = num + 1
                      if tur.is_win(gridd,1, row, col) == True:
                                 tur.display_winner(1)
                                 gm.add_score(1)
                                 tur.display_winner(1)
                                 print("The winner is yellow, the game is over")
                                 gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                 return
                                 
                      elif tur.is_win(gridd,2, row, col) == True:
                                 gm.add_score(2)
                                 tur.display_winner(2)
                                 print("The winner is red, the game is over")
                                 gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                 return 
                      elif tur.is_full(gridd, row, col) == True:
                                 print("The game is over")
                                 return 
                      
                      
                      
                                 

def main():
           num = 1
           play_game(num)


main()


