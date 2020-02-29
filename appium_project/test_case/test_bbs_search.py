import sys
from os.path import dirname, abspath
from common.my_test import MyTest
from page.bbs_page import BBSPage
import unittest
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)

class TestBBSSearch(MyTest):
    '''测试查询功能'''
    def test_search_key(self):
        page = BBSPage(self.driver)
        load = page.load_page.click()
        box = page.search_box.send_keys("手机")
        submit = page.search_button.click()

if __name__=="__main__":
    unittest.main()