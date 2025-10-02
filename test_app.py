#test_app.py

import unittest #Python’s built-in testing framework (like JUnit in Java)
from app import hello_world #You’re importing hello_world function from app.py so it can be tested.

class TestApp(unittest.TestCase): #Defines a test class. unittest.TestCase gives you a lot of useful test methods (assertEqual, assertTrue, etc.).
    #This is an actual test case.
    def test_hello_world(self): #self is a object
        self.assertEqual(hello_world(), "Hello, World!") #self.assertEqual(A, B) → checks if A == B.

if __name__ == "__main__": #This makes the test file executable directly
    unittest.main()