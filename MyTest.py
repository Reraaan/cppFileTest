import HTMLTestRunner
import unittest
import os
import subprocess
import platform
import sys


class Script():
    def c_exe(cppfilePath, execPath):
        # execPath = currentpath + "/" + "printmonth.exe"
        index = execPath.index(".")
        execPath = execPath[0:index]
        # currentpath/test
        # 拼接需在命令行执行的命令
        command = "g++ " + cppfilePath + " -o " + execPath

        # command=g++ currentpath/test.cpp -o currentpath/test

        # 当shell=True时，表示在系统默认的shell环境中执行新的进程，此shell在windows表示为cmd.exe，在linux为/bin/sh。
        # 如果stdout设置为PIPE，此时stdout其实是个file对象，用来保存新创建的子进程的输出；如果stderr设置为PIPE，此时的stderr其实是个file对象，用来保存新创建的子进程的错误输出。
        # .communicate()输入标准输入，输出标准输出和标准出错
        chlid = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res = chlid.communicate()
        out = str(res[0], encoding="gbk")
        err = str(res[1], encoding="gbk")
        if err != None and err != "":
            print(err)
            sys.exit(0)
        print(out)

        _system = platform.system()
        if (_system == "Windows"):
            execPath += ".exe"

    def c_output(execPath, inputCase):
        chlid = subprocess.Popen(execPath, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        chlid.stdin.write(bytes(inputCase, encoding="UTF-8"))
        # chlid.stdin.write(b"10")
        # print (chlid.stdout.read())
        '''poll_seconds = .250
        # 进程是否终止标志
        flag = False
        # .poll()检查是否结束，设置返回值
        # .terminate()方法 终止进程
        while time.time() < deadline and chlid.poll() == None:
            time.sleep(poll_seconds)
        if chlid.poll() == None:
            if float(sys.version[:3]) >= 2.6:
                chlid.terminate()
                flag = True'''

        res = chlid.communicate()
        # res[0] = open("C:\\Users\Administrator\\Desktop\\2018 10.txt",'r');
        # print (res[0])

        out = str(res[0], encoding="utf-8")
        err = str(res[1], encoding="utf-8")
        # os.remove(execPath)
        if err != "":
            for line in err.split():
                print(line)

        # if flag:
        # print("forced out of")

        print(out)
        return (out.strip())

class MyTest(unittest.TestCase):#继承unittest.TestCase

    @classmethod
    def setUpClass(self):
        # 每个测试用例执行之前做操作
        self.test_case01 ="2018 10"
        self.test_case02 = "2018 12"
        self.test_case03 = "2017 06"
        self.test_case04 = "2011 09"
        self.test_case05 = "2100 01"

        self.expectCase01 = ""
        self.expectCase02 = ""
        self.expectCase03 = ""
        self.expectCase04 = ""
        self.expectCase05 = ""

        self.currentpath = os.path.abspath('.')
        self.compileName = "printmonth.cpp"#get_compile(currentpath)
        self.commandName = "test.exe"#get_command(currentpath)
        #self.cpp_caseName = "printmonth_case.cpp"
        self.exec_caseName = "printmonth_case.exe"

        self.cppfilePath = self.currentpath + "/" + self.compileName
        self.execPath = self.currentpath + "/" + self.commandName
        #self.cppcasePath = self.currentpath + "/" + self.cpp_caseName
        self.execcasePath = self.currentpath + "/" + self.exec_caseName

        Script.c_exe(self.cppfilePath,self.execPath)
        #Script.c_exe(self.cppcasePath,self.execcasePath)




    @classmethod
    def tearDownClass(self):
        #每个测试用例执行之后做操作
        os.remove(self.execPath)
        #os.remove(self.execcasePath)
        
        

    def tearDown(self):
        #每个测试用例执行之后做操作
        pass

    def setUp(self):
        # 每个测试用例执行之前做操作
        pass
        
        """
        常用的断言，也就是校验结果
        assertEqual(a, b)     a == b      
        assertNotEqual(a, b)     a != b      
        assertTrue(x)     bool(x) is True      
        assertFalse(x)     bool(x) is False      
        assertIsNone(x)     x is None     
        assertIsNotNone(x)     x is not None   
        assertIn(a, b)     a in b    
        assertNotIn(a, b)     a not in b
        """



    def test_01(self):
        self.outputCase01 = Script.c_output(self.execPath,self.test_case01)
        #print(self.outputCase01)
        self.expectCase01 = Script.c_output(self.execcasePath,self.test_case01)
        self.assertEqual(self.outputCase01,self.expectCase01)
    
    def test_02(self):
        self.outputCase02 = Script.c_output(self.execPath,self.test_case02)
        #print(self.outputCase02)
        self.expectCase02 = Script.c_output(self.execcasePath,self.test_case02)
        self.assertEqual(self.outputCase02,self.expectCase02)
    
    def test_03(self):
        self.outputCase03 = Script.c_output(self.execPath,self.test_case03)
        #print(self.outputCase03)
        self.expectCase03 = Script.c_output(self.execcasePath,self.test_case03)
        self.assertEqual(self.outputCase03,self.expectCase03)

    def test_04(self):
        self.outputCase04 = Script.c_output(self.execPath,self.test_case04)
        #print(self.outputCase04)
        #self.expectCase04 = Script.c_output(self.execcasePath,self.test_case04)
        self.assertEqual(self.outputCase04,self.expectCase04)

    def test_05(self):
        self.outputCase05 = Script.c_output(self.execPath,self.test_case05)
        #print(self.outputCase05)
        self.expectCase05 = Script.c_output(self.execcasePath,self.test_case05)
        self.assertEqual(self.outputCase05,self.expectCase05)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()#创建一个测试集合
    #test_suite.addTest(MyTest('test_01'))#测试套件中添加测试用例
    test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    with open(os.path.abspath('.')+'\\report\\res.html','wb') as f:#打开一个保存结果的html文件
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='cpp单文件测试',description='测试情况')
        #生成执行用例的对象
        runner.run(test_suite)
        #执行测试套件


"""
在目录下创建多个测试用例 遍历文件夹运行每个测试用例
import unittest,HTMLTestRunner
suite = unittest.TestSuite()#创建测试套件
all_cases = unittest.defaultTestLoader.discover('.','test_*.py')
#找到某个目录下所有的以test开头的Python文件里面的测试用例
for case in all_cases:
    suite.addTests(case)#把所有的测试用例添加进来
fp = open('res.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='all_tests',description='所有测试情况')
runner.run(suite)
#运行测试
"""