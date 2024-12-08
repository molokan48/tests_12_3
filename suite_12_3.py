import unittest
import tests_12_3

newTest = unittest.TestSuite()
newTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.Runner_Test))
newTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(newTest)