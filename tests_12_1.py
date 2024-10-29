import runner
import unittest


class RunnerTest(unittest.TestCase):

     def test_walk(self):
         n1 = runner.Runner("Nick")
         for i in range(10):
             n1.walk()
         self.assertEqual(n1.distance, 50)

     def test_run(self):
         n1 = runner.Runner("Nick")
         for i in range(10):
             n1.run()
         self.assertEqual(n1.distance, 100)

     def test_chelleng(self):
         n1 = runner.Runner("Nick")
         n2 = runner.Runner("Ivan")
         for i in range(10):
             n1.walk()
             n2.run()
         self.assertNotEqual(n1.distance, n2.distance)


if __name__ == "__main__":
    unittest.main()