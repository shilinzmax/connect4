'''
CS 5001
Spring 2020
Project
drive_arrow.py

I write two drive versions: this one is click arrow then drop the ball
in drive_input.py file, that one is input the column number and then drop the
ball

Once get winner, click the screen will exit the program
'''

import turtle
from game import Game
from tturtle import Tturtle


#initialize the 6*7 grid:
gridd = [[0 for c in range(7)] for x in range(6)]
#initialize turtle
tur = Tturtle()
tur.draw_board()
tur.draw_grid(gridd)
tur.draw_game_panel()
tur.get_arrow()
tur.show_instruction()
#tur.color_turn(tur.get_num()+1)

#initialize Game class
gm = Game()
gm.initialize_score("connect4")
tur.show_score(gm.get_red(), gm.get_yellow())
tur.color_turn(tur.get_num()%2+1)
def click(x,y):
                                '''
                                Click the arrow above the grid board to drop the color ball into the grid
                                '''
                                if -360 < x < -340 and 230 < y < 250:
                                           col = 0
                                           if gridd[0][0] == 0:
                                                      count = 5
                                                      while gridd[count][0] != 0:
                                                                 count = count - 1
                                                      t = tur.get_num()%2+1
                                                      tur.color_turn(t+1)
                                                      gridd[count][0] = t       
                                                      tur.store_num()
                                                      tur.draw_grid(gridd)
                                                      if tur.is_win(gridd, t) == True or tur.is_full(gridd):
                                                                 if tur.is_win(gridd, t) == True:
                                                                            gm.add_score(t)
                                                                            tur.display_winner(t)
                                                                            gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                                                 turtle.Screen().exitonclick()
                                                                 
                                                               
                                                                 
                                                       
                                                                 
                                if -300 < x < -280 and 230 < y < 250:
                                           col = 1
                                           if gridd[0][1] == 0:
                                                      count = 5
                                                      while gridd[count][1] != 0:
                                                                 count = count - 1
                                                      t = tur.get_num()%2+1
                                                      tur.color_turn(t+1)
                                                      gridd[count][1] = t
                                                      tur.store_num()
                                                      tur.draw_grid(gridd)
                                                      if tur.is_win(gridd, t) == True or tur.is_full(gridd):
                                                                 if tur.is_win(gridd,t) == True:
                                                                            gm.add_score(t)
                                                                            tur.display_winner(t)
                                                                            gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                                                 turtle.Screen().exitonclick()

                                if -240 < x < -220 and 230 < y < 250:
                                           col = 2
                                           if gridd[0][2] == 0:
                                                      count = 5
                                                      while gridd[count][2] != 0:
                                                                 count = count - 1
                                                      t = tur.get_num()%2+1
                                                      tur.color_turn(t+1)
                                                      gridd[count][2] = t
                                                      tur.store_num()
                                                      tur.draw_grid(gridd)
                                                      if tur.is_win(gridd, t) == True or tur.is_full(gridd):
                                                              if tur.is_win(gridd,t) == True:
                                                                            gm.add_score(t)
                                                                            tur.display_winner(t)
                                                                            gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                                                
                                                              turtle.Screen().exitonclick()

                                if -180 < x < -160 and 230 < y < 250:
                                           col = 3
                                           if gridd[0][3] == 0:
                                                      count = 5
                                                      while gridd[count][3] != 0:
                                                                 count = count - 1
                                                      t = tur.get_num()%2+1
                                                      tur.color_turn(t+1)
                                                      gridd[count][3] = t
                                                      tur.store_num()
                                                      tur.draw_grid(gridd)
                                                      if tur.is_win(gridd, t) == True or tur.is_full(gridd):
                                                              if tur.is_win(gridd,t) == True:
                                                                            gm.add_score(t)
                                                                            tur.display_winner(t)
                                                                            gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                                                
                                                              turtle.Screen().exitonclick()



                                if -120 < x < -100 and 230 < y < 250:
                                           col = 4
                                           if gridd[0][4] == 0:
                                                      count = 5
                                                      while gridd[count][4] != 0:
                                                                 count = count - 1
                                                      t = tur.get_num()%2+1
                                                      tur.color_turn(t+1)
                                                      gridd[count][4] = t
                                                      tur.store_num()
                                                      tur.draw_grid(gridd)
                                                      if tur.is_win(gridd, t) == True or tur.is_full(gridd):
                                                              if tur.is_win(gridd,t) == True:
                                                                            gm.add_score(t)
                                                                            tur.display_winner(t)
                                                                            gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                                                
                                                              turtle.Screen().exitonclick()


                                                       
                                if -60 < x < -40 and 230 < y < 250:
                                           col = 5
                                           if gridd[0][5] == 0:
                                                      count = 5
                                                      while gridd[count][5] != 0:
                                                                 count = count - 1
                                                      t = tur.get_num()%2+1
                                                      tur.color_turn(t+1)
                                                      gridd[count][5] = t
                                                      tur.store_num()
                                                      tur.draw_grid(gridd)
                                                      if tur.is_win(gridd, t) == True or tur.is_full(gridd):
                                                              if tur.is_win(gridd,t) == True:
                                                                            gm.add_score(t)
                                                                            tur.display_winner(t)
                                                                            gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                                                
                                                              turtle.Screen().exitonclick()


                                                                                                                        
                                if 0 < x < 20 and 230 < y < 250:
                                           col = 6
                                           if gridd[0][6] == 0:
                                                      count = 5
                                                      while gridd[count][6] != 0:
                                                                 count = count - 1
                                                      t = tur.get_num()%2+1
                                                      tur.color_turn(t+1)
                                                      gridd[count][6] = t
                                                      tur.store_num()
                                                      tur.draw_grid(gridd)
                                                      if tur.is_win(gridd, t) == True or tur.is_full(gridd):
                                                              if tur.is_win(gridd,t) == True:
                                                                            gm.add_score(t)
                                                                            tur.display_winner(t)
                                                                            gm.store_score("connect4",gm.get_red(), gm.get_yellow())
                                                                
                                                              turtle.Screen().exitonclick()

                                                              
                                     
   

def main():

           turtle.onscreenclick(click, 1)
main()
                                            
                                           
























           

