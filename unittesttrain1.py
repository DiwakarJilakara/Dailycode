import trains1
import unittest
class Test_Trains(unittest.TestCase):
    def setUp(self) -> None:
        TrainA=[]
        TrainB=[]
        TrainAB=[]
        return super().setUp()
    def test_Train_Detach_A_Boggie_For_TrainA(self):
        TrainA=['slm','hyb']
        TrainB=[]
        t=trains1.TrainJourney1()
        t.set_values(TrainA,TrainB)
        p=t.detach_Boggies_of_TrainA()
        self.assertListEqual(p,[])
    def test_Train_Detach_A_Boggie_For_TrainB(self):
        TrainA=['slm','hyb']
        TrainB=['tvc','tvc','mao','hyb','ngp']
        t=trains1.TrainJourney1()
        t.set_values(TrainA,TrainB)
        p=t.detach_Boggies_of_TrainB()
        self.assertListEqual(p,['ngp'])

    def test_Train_AB_With_No_Boggies_To_Travell(self):
        TrainA=['slm','hyb']
        TrainB=['tvc','tvc','mao','hyb']
        t=trains1.TrainJourney1()
        t.set_values(TrainA,TrainB)
        p=t.TrainAB_status()
        self.assertEqual(p,"JOURNEY_ENDED")
    def test_Train_AB_With_Oneormore_Boggies_To_Travell(self):
        TrainA=['slm','hyb','ghy']
        TrainB=['tvc','tvc','mao','hyb','njp','ghy']
        t=trains1.TrainJourney1()
        t.set_values(TrainA,TrainB)
        p=[]
        p+=t.TrainAB_status()
        self.assertListEqual(p,['ghy''ghy','njp'])
    