
# 내가 만든 패키지 import 하기
from myclass import classTest  # class파일 import => classTest.testClass()로 샤용

print('===========================')
test1 = classTest.testClass()
print('test =', test1)
print('type =', type(test1))

test1.set_info('test1')
test1.print_info()
print('===========================')

# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))  # 현재 모듈의 절대경로로 상위폴더 참조
# print('os.path.dirname(__file__) =', os.path.dirname(__file__))  # C:/Users/Administrator/PycharmProjects/kiwoom/mykiwoom
# print('os.path.abspath(os.path.dirname(__file__)) =', os.path.abspath(os.path.dirname(__file__)))  # C:\Users\Administrator\PycharmProjects\kiwoom\mykiwoom
# print('os.path.dirname(os.path.abspath(os.path.dirname(__file__))) = ', os.path.dirname(os.path.abspath(os.path.dirname(__file__))))  #C:\Users\Administrator\PycharmProjects\kiwoom
#
# sys.path.append("C:/Users/Administrator/PycharmProjects/kiwoom/mykiwoom/")  # root경로 직접입력
#
# import main  # main.py

from myclass.classTest import testClass  # class명 import => testClass()로 사용

print('===========================')
test2 = testClass()
print(test2)
type(test2)

test2.set_info('test2')
test2.print_info()
print('===========================')


