import unittest
class TestClass(unittest.TestCase):

    def testIsEquals(self):
        self.assertTrue(2==2,"Si")
        self.assertEqual(3,3,"no")


    if __name__ == "__main__":
        unittest.main()


    