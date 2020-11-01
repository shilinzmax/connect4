'''
CS 5001
Spring 2020
Project
test_game.py
'''



import unittest
import os
from game import Game

class TestReverse(unittest.TestCase):
           def test_init(self):
                      g = Game()
                      self.assertEqual(g.red, 0)
                      self.assertEqual(g.yellow,0)

           def test_score1(self):
                      g = Game()
                      g.add_score(1)
                      self.assertEqual(g.yellow, 1)
                      
           def test_score2(self):
                      g = Game()
                      g.add_score(2)
                      self.assertEqual(g.red, 1)

           def test_score3(self):
                      g = Game()
                      if os.path.exists('gamy.txt'):
                                 os.remove('gamy.txt')
                      g.initialize_score('gamy.txt')
                      self.assertEqual(g.red, 0)
                      self.assertEqual(g.yellow,0)

                      with open('testscore.txt', 'w') as outfile:
                                 outfile.write('10\n1\n')
                      g.initialize_score('testscore.txt')
                      self.assertEqual(g.red, 10)
                      self.assertEqual(g.yellow, 1)
                      os.remove('testscore.txt')


                                 

def main():
    unittest.main(verbosity = 3)

main()
