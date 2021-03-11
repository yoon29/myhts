
class testClass:

    # 생성자
    def __init__(self):
        print('생성자id =', id(self))

    # 소멸자
    def __del__(self):
        print('소멸자id =', id(self))

    # method
    def set_info(self,name):
        self.name = name

    # method
    def print_info(self):
        print('name =', self.name)
