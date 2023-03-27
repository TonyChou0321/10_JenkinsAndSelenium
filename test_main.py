'''
python -m unittest test_main.py
'''
import time

from selenium import webdriver
import unittest
import math
driver = webdriver.Chrome()

class selenium_grid (unittest.TestCase):
     def test1(self):
          # driver.get('https://google.com')
          # self.assertEquals('Google', driver.title, 'webpage title are not same')
          # time.sleep(3)
          # driver.close()
          a = 1
          b = 2
          assert a + b == 3

     def test2(self):
          a = 1
          b = 2
          assert a - b == 3

     def test3(self):
          a = 1
          b = 2
          assert a * b == 3

     def test4(self):
          a = 1
          b = 2
          assert a / b == 3

     def test5(self):
          a = 1
          b = 2
          assert a ** b == 1

     def test6(self):
          b = 9
          assert math.sqrt(b) == 3







if __name__ == "__main__":
     unittest.main()