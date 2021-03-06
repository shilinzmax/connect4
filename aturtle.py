'''
CS 5001
Spring 2020
Project
Aturtle.py
'''

import turtle
from game import Game

s = turtle.Turtle()
s.hideturtle()

t = turtle.Turtle()
t.hideturtle()


Pen = turtle.Turtle()
Pen.hideturtle()
Pen.speed(500)
Pen.speed(0)
Pen._tracer(8, 25)

turtle.setup(800, 800)




class Aturtle:

           def __init__(self):
                      #initialize the window and num(if odd, red, if even, yellow)
                      window = turtle.Screen()
                      window.screensize(800, 400)
                      window.bgcolor("lightgrey")
                      self.num = 0

           

           def draw_grid(self, grid, r, c):
                      '''
                      Method -- draw the grid
                      Parameters:
                      self -- the current object
                      Returns nothing
                      '''
                      
                      Pen.setheading(0)
                      Pen.goto(-350, 130)
                      for rower in range(0, r):
                                 for col in range(0, c):
                                            if grid[rower][col] == 0:
                                                       Pen.fillcolor("white")
                                            elif grid[rower][col] == 2:
                                                       Pen.fillcolor("red")
                                            elif grid[rower][col] == 1:
                                                       Pen.fillcolor("yellow")
                                            Pen.begin_fill()
                                            Pen.circle(25)
                                            Pen.end_fill()

                                            Pen.penup()
                                            Pen.forward(60)
                                            Pen.pendown()
                                 Pen.setheading(270)
                                 Pen.penup()
                                 Pen.forward(60)
                                 Pen.setheading(180)
                                 Pen.forward(60 * c)
                                 Pen.setheading(0)
                                 Pen.getscreen().update()
                                 
           def draw_board(self):
                                 '''
                                 Method -- draw the board
                                 Parameters:
                                 self -- the current object
                                 Returns nothing
                                 '''
                                 Pen.up()
                                 Pen.setheading(0)
                                 Pen.goto(-390, -230)
                                 Pen.begin_fill()
                                 for b in range(4):
                                            Pen.color("blue")
                                            Pen.pendown()
                                            Pen.forward(440)
                                            Pen.left(90)
                                 Pen.up()
                                 Pen.end_fill()
                                 Pen.getscreen().update()

           def draw_game_panel(self):

                                     '''
                                     Method -- draw the game panel
                                     Parameters:
                                     self -- the current object
                                     Returns nothing
                                     '''
                                     Pen.up()
                                     Pen.setheading(0)
                                     Pen.goto(80, 219)
                                     Pen.begin_fill()
                                     for rectangle in range(2):
                                         Pen.color("white")
                                         Pen.down()
                                         Pen.forward(250)
                                         Pen.right(90)
                                         Pen.forward(418)
                                         Pen.right(90)
                                     Pen.end_fill()
                                     Pen.up()
                                     Pen.color("red")
                                     Pen.goto(-150, 280)
                                     Pen.write("Red", True, align="center", font=("Arial", 15, "bold"))


                                     a = 100
                                     Pen.up()
                                     Pen.color("yellow")
                                     Pen.goto(-150, 300)
                                     Pen.write("Yellow", True, align="center", font=("Arial", 15, "bold"))
                                     
                                     
                                     Pen.up()
                                     Pen.setheading(0)
                                     Pen.goto(200, 230)
                                     Pen.color("black")
                                     Pen.write("Winner", True, align="center", font=("Arial", 40, "bold"))
                                     Pen.getscreen().update()
           
           def show_score(self, red, yellow):

                                     
                                     '''
                                     Method -- show the red and yellow scores on the screnn
                                     Parameters:
                                     self -- the current object,
                                     red -- the winning number of red(int),
                                     yellow -- the winning number of yellow,
                                     Returns nothing
                                     '''
                                     Pen.up()
                                     Pen.color("red")
                                     Pen.goto(-100,280)
                                     Pen.write(red, True, align="center", font=("Arial", 15, "bold"))
                                     
                                     Pen.up()
                                     Pen.color("yellow")
                                     Pen.goto(-80, 300)
                                     Pen.write(yellow, True, align="center", font=("Arial", 15, "bold"))
                                     Pen.getscreen().update()



           def check_if_winner(self, grid, color, row, col):

                                     '''
                                     Method -- check which color is the winner
                                     Parameters:
                                     self -- the current object,
                                     grid -- the grid board
                                     color -- the winning number representing the color
                                     Returns the winnning number
                                     '''
                                     lst = []
                                     for r in range(row):
                                         for c in range(col-3):
                                             if grid[r][c] == color and grid[r][c+1] == color and grid[r][c+2] == color and grid[r][c+3] == color:
                                                 lst.append(color)
                                                 return lst[0]
                                     # Horizontal row checking
                                     for x in range(row-3):
                                         for y in range(col):
                                             if grid[x][y] == color and grid[x+1][y] == color and grid[x+2][y] == color and grid[x+3][y] == color:
                                                 lst.append(color)
                                                 return lst[0]
                                     # Diagonal checking
                                     for i in range(row-3):
                                         for z in range(ccol-3):
                                             if grid[i][z] == color and grid[i+1][z+1] == color and grid[i+2][z+2] == color and grid[i+3][z+3] == color:
                                                 lst.append(color)
                                                 return lst[0]
                                     # Diagonal checking
                                     for d in range(row-1, row-4, -1):
                                         for c in range(c-3):
                                             if grid[d][c] == color and grid[d-1][c+1] == color and grid[d-2][c+2] == color and grid[d-3][c+3] == color:
                                                 lst.append(color)
                                                 return lst[0]
                                     return 0


           def is_full(self, grid, r, c):
                      '''
                      Method -- check if the grid is full
                      Parameters:
                      self -- the current object
                      grid -- list of the grid board
                      Returns boolean value
                      '''
                      #if full, return true, else return false
                      for i in range (0,r):
                                 for j in range (0,c):
                                            if grid[i][j] == 0:
                                                       return False
                      return True

           def is_win(self, grid, color, row, col):
                                     

                                     # Vertical row checking
                                     for r in range(row):
                                         for c in range(col-3):
                                             if grid[r][c] == color and grid[r][c+1] == color and grid[r][c+2] == color and grid[r][c+3] == color:
                                                 return True
                                     # Horizontal row checking
                                     for x in range(row-3):
                                         for y in range(col):
                                             if grid[x][y] == color and grid[x+1][y] == color and grid[x+2][y] == color and grid[x+3][y] == color:
                                                 return True
                                     # Diagonal checking
                                     for i in range(row-3):
                                         for z in range(col-3):
                                             if grid[i][z] == color and grid[i+1][z+1] == color and grid[i+2][z+2] == color and grid[i+3][z+3] == color:
                                                 return True
                                     # Diagonal checking
                                     for d in range(row-1, row-4, -1):
                                         for c in range(col-3):
                                             if grid[d][c] == color and grid[d-1][c+1] == color and grid[d-2][c+2] == color and grid[d-3][c+3] == color:
                                                 return True
                                     return False                    
                      



           def color_turn(self, num):
                      '''
                      Method -- change the color after each click
                      Parameters:
                      self -- the current object
                      num -- integer to show which color's turn
                      Returns nothing
                      '''
                      t.clear()
                      if num%2 == 0:
                                 t.penup()
                                 t.fillcolor("red")
                                 t.goto(200, -50)
                                 t.begin_fill()
                                 t.circle(25)
                                 t.end_fill()
                                 t.up()
                                 t.color("red")
                                 t.goto(200, 10)
                                 t.write("Red turn", True, align="center", font=("Arial", 15, "bold"))
 
                      if num%2 == 1:
                                 t.penup()
                                 t.fillcolor("yellow")
                                 t.goto(200, -50)
                                 t.begin_fill()
                                 t.circle(25)
                                 t.end_fill()
                                 t.up()
                                 t.color("yellow")
                                 t.goto(200, 10)
                                 t.write("Yellow turn", True, align="center", font=("Arial", 15, "bold"))
                      t.getscreen().update()

           def display_winner(self, winners):
                                     '''
                                     Method -- show the winner color on the screen
                                     Parameters:
                                     self -- the current object
                                     winner -- the winning color
                                     Returns nothing
                                     '''

                                     s.clear()
                                     if winners == 2:
                                         s.penup()
                                         s.color("red")
                                         s.goto(200, 150)
                                         s.write("RED WINS", True, align="center", font=("Arial", 20, "bold"))
                                         s.getscreen().update()
                                       
                                     elif winners == 1:
                                         s.penup()
                                         s.color("yellow")
                                         s.goto(200, 150)
                                         s.write("YELLOW WINS", True, align="center", font=("Arial", 20, "bold"))
                                         s.getscreen().update()




                                 






























           
