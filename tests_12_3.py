import unittest
from unittest import TestCase
from for_test_12_2 import Tournament
from for_test_12_1 import Runner


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    @unittest.skipIf(is_frozen , 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.useyn = Runner('Усейн' , 10)
        self.andrey = Runner('Андрей' , 9)
        self.nic = Runner('Ник' , 3)

    @unittest.skipIf(is_frozen , 'Тесты в этом кейсе заморожены')
    def test_Tour_1(self):
        tour_1 = Tournament(90 , self.useyn , self.nic)
        self.all_result[1] = tour_1.start()
        self.assertTrue(self.all_result[1][max(self.all_result[1].keys())] == self.nic)

    @unittest.skipIf(is_frozen , 'Тесты в этом кейсе заморожены')
    def test_Tour_2(self):
        tour_2 = Tournament(90, self.andrey, self.nic)
        self.all_result[2] = tour_2.start()
        self.assertTrue(self.all_result[2][max(self.all_result[2].keys())] == self.nic)

    @unittest.skipIf(is_frozen , 'Тесты в этом кейсе заморожены')
    def test_Tour_3(self):
        tour_3 = Tournament(90, self.useyn, self.andrey, self.nic)
        self.all_result[3] = tour_3.start()
        self.assertTrue(self.all_result[3][max(self.all_result[3].keys())] == self.nic)

    @classmethod
    def tearDownClass(cls):
        tt_1 = {}
        for key in cls.all_result.keys():
            tt_1[key] = {}
            for k in cls.all_result[key].keys():
                tt_1[key][k] = cls.all_result[key][k].__str__()
            print(tt_1[key])

class Runner_Test(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        tester = Runner("tester")
        for _ in range(10):
            tester.walk()
        self.assertEqual(tester.distance , 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        tester = Runner("tester")
        for _ in range(10):
            tester.run()
        self.assertEqual(tester.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        tester_1 = Runner("tester_1")
        tester_2 = Runner("tester_2")
        for _ in range(10):
            tester_1.walk()
            tester_2.run()
        self.assertNotEqual(tester_1.distance, tester_2.distance)


if __name__ == "__main__":
    unittest.main()