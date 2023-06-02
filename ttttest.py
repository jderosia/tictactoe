import tttlogic as ttt
import unittest

class TestBoardMethods(unittest.TestCase):
    def test_getCurrentState(self):
        board1 = {'1': 'X', '2': 'X', '3': 'X', '4': 'O', '5': 'O', '6': 'O', '7': 'X', '8': 'X', '9': 'X'}
        self.assertEqual(ttt.getCurrentState(board1), 'X')

        emptyBoard = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
        self.assertEqual(ttt.getCurrentState(emptyBoard), 'keep playing')

        board2 = {'1': 'X', '2': 'O', '3': 'X', '4': 'O', '5': 'O', '6': 'X', '7': 'O', '8': 'X', '9': 'O'}
        self.assertEqual(ttt.getCurrentState(board2), 'tie')

    





player1Name = 'Jace'
player2Name = 'Lucas'
player1Turn = False



if __name__ == '__main__':
    unittest.main()
