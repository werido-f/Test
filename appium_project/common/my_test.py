import unittest
from appium import webdriver
import sys
from os.path import dirname,abspath
from app_config import CAPS

BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS)
        cls.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
