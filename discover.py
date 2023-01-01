import unittest
import geektrust
import enum
class FacingDirection(enum.IntEnum):
        North=0
        East=1
        South=2
        West=3
class Test_Gman(unittest.TestCase):

     def setUp(self):
        self.gman1=geektrust.man()
     def test_Assigning_values(self):
        self.assertTrue(self.gman1.assignvalues(1,2,FacingDirection.East,3,4))
     def test_Move_Right(self):
        self.gman1.assignvalues(1,2,FacingDirection.East,4,2)
        self.assertEqual(self.gman1.computePower(),170)
     def test_Move_Left(self):
        self.gman1.assignvalues(3,2,FacingDirection.West,1,2)
        self.assertEqual(self.gman1.computePower(),180)
     def test_Change_direction_and_move_right(self):
         self.gman1.assignvalues(1,2,FacingDirection.South,4,2)
         self.assertEqual(self.gman1.computePower(),165)
     def test_Change_direction_and_move_left(self):
         self.gman1.assignvalues(3,2,FacingDirection.South,1,2)
         self.assertEqual(self.gman1.computePower(),175)
     def test_Change_direction_Two_Times_and_move_left(self):
         self.gman1.assignvalues(3,2,FacingDirection.East,1,2)
         self.assertEqual(self.gman1.computePower(),170)
     def test_Change_direction_Two_Times_and_move_top(self):
         self.gman1.assignvalues(2,1,FacingDirection.East,4,3)
         self.assertEqual(self.gman1.computePower(),155)

     def test_Change_direction_Two_Times_and_move_top2(self):

         self.gman1.assignvalues(0,5,FacingDirection.West,6,1)

         self.assertEqual(self.gman1.computePower(),90)

     def test_Change_direction_Two_Times_and_move_top3(self):

         self.gman1.assignvalues(3,6,FacingDirection.North,1,0)

         self.assertEqual(self.gman1.computePower(),110)
unittest.main()


         
