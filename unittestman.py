import unittest
import man
import enum
class FacingDirection(enum.IntEnum):
        North=0
        East=1
        South=2
        West=3
class Test_Gman(unittest.TestCase):
    def setUp(self):
        self.gman1=man.man()
    def test_Assigning_values(self):
        self.assertTrue(self.gman1.assignvalues(1,2,FacingDirection.East,3,4))
    def test_Move_Right(self):
        self.gman1.assignvalues(1,2,FacingDirection.East,4,2)
        self.assertEqual(self.gman1.computePower(),30)
    def test_Move_Left(self):
        self.gman1.assignvalues(3,2,FacingDirection.West,1,2)
        self.assertEqual(self.gman1.computePower(),20)
    def test_Change_direction_and_move_right(self):
         self.gman1.assignvalues(1,2,FacingDirection.South,4,2)
         self.assertEqual(self.gman1.computePower(),35)
    def test_Change_direction_and_move_left(self):
         self.gman1.assignvalues(3,2,FacingDirection.South,1,2)
         self.assertEqual(self.gman1.computePower(),25)
    def test_Change_direction_Two_Times_and_move_left(self):
         self.gman1.assignvalues(3,2,FacingDirection.East,1,2)
         self.assertEqual(self.gman1.computePower(),30)
    def test_Change_direction_Two_Times_and_move_top(self):
         self.gman1.assignvalues(1,5,FacingDirection.North,1,2)
         self.assertEqual(self.gman1.computePower(),40)
    def test_Check_File_upload(self):
         self.gman1.readInputFromFile()
         self.assertEqual(self.gman1.computePower(),45)
         


         
