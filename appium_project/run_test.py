import time
import unittest
from HTMLTestRunner import  HTMLTestRunner

if __name__=="__main__":
    test_dir = "./test_case"
    suit = unittest.defaultTestLoader.discover(test_dir, "test_*.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = "./test_report/"+now+"result.html"
    with open(test_report,'wb') as fp:
        runner = HTMLTestRunner(stream=fp,title="魅族社区app测试",description="运行环境：小米6A")
        runner.run(suit)