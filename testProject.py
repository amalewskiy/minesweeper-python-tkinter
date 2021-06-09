from createMenu import CreateFrame
from tkinter import Tk, StringVar
import unittest


# Before testing disable messagebox in "createMenu" (line 135)
class TestInputValues(unittest.TestCase):
    root = Tk()
    menu = CreateFrame(root)
    menu.origColor = 'green'

    def test_Input_String(self):
        """This test trying run custom program with string value"""
        height = StringVar(self.root, 2)
        width = StringVar(self.root, 'two')
        mines = StringVar(self.root, 3)
        with self.assertRaises(Exception) as context:
            self.menu.createGameWindow('Custom', height, width, mines)
        self.assertTrue('Invalid data type' in str(context.exception))

    def test_Input_Invalid_Data(self):
        """This test trying run custom program with invalid value"""
        height = StringVar(self.root, 0)
        width = StringVar(self.root, -45)
        mines = StringVar(self.root, 3)
        with self.assertRaises(Exception) as context:
            self.menu.createGameWindow('Custom', height, width, mines)
        self.assertTrue('Invalid data' in str(context.exception))

    def test_Empty_Input(self):
        """This test trying run custom program without values"""
        height = StringVar(self.root)
        width = StringVar(self.root)
        mines = StringVar(self.root)
        with self.assertRaises(Exception) as context:
            self.menu.createGameWindow('Custom', height, width, mines)
        self.assertTrue('Invalid data type' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
