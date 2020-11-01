'''
CS 5001
Spring 2020
Project
game.py
'''

class Game:
           '''class: Game
           Attributes:red(int) yellow(int)
           Methods: initialize_score,store_score,add_score,get_red,get_yellow
           '''
           def __init__(self):
                      '''
                      Constructor -- creates an new instance of a Game
                      Parameters:
                      self -- the current object
                      red -- the number of the game win for red color
                      yellow -- the number of the game win for the yellow color
                      '''
                      self.red = 0
                      self.yellow = 0
                      
           def initialize_score(self, newFile):
                      '''
                      Method -- read the file and initialize the start red and yellowscore
                      Parameters:
                      self -- the current object
                      newFile -- the file name
                      Returns nothing
                      '''
                      try:
                                 with open(newFile, 'r') as infile:
                                            lines = infile.readlines()
                                            red = lines[0].split()
                                            self.red = int(red[0])
                                            yellow = lines[1].split()
                                            self.yellow = int(yellow[0])
                                            
                      except OSError:
                                 self.red = 0
                                 self.yellow = 0
                      
           def store_score(self, File_name, red, yellow):
                      '''
                      Method -- store the score after the game
                      Parameters:
                      self -- the current object
                      Fille_name -- the file name
                      red -- the score of red
                      yellow -- the score of yellow
                      Returns nothing
                      '''
                      try:
                                 with open(File_name, 'w') as outfile:
                                            a = str(red) + "\n"
                                            outfile.write(a)
                                            b = str(yellow) + "\n"
                                            outfile.write(b)
                      except OSError:
                                 print("Sorry, can not store your scores")

           def add_score(self, winner):
                      '''
                      Method -- add one point to the winner's color
                      Parameters:
                      self -- the current object
                      winner -- the winner's color
                      Returns nothing
                      '''
                    
                      if(winner == 2):
                                 self.red = self.red + 1
                
                      if(winner == 1):
                                 self.yellow = self.yellow + 1
           def get_red(self):
                      '''
                      Method -- get the scores of red
                      Parameters:
                      self -- the current object
                      Returns red scores
                      '''
                      return self.red

           def get_yellow(self):
                      '''
                      Method -- get the scores of yellow
                      Parameters:
                      self -- the current object
                      Returns yellow scores
                      '''                      
                      return self.yellow

           
                                 

           



                                 



