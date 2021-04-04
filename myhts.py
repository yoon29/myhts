'''
파이썬으로 배우는 알고리즘 트레이딩 (개정판-2쇄)
https://wikidocs.net/4242
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

########################################################################################################################
'''
Open API+의 TR 처리 순서
1) SetInputValue 메서드를 사용해 TR 입력 값을 설정합니다. 
2) CommRqData 메서드를 사용해 TR을 서버로 송신합니다. 
3) 서버로부터 이벤트가 발생할 때까지 이벤트 루프를 사용해 대기합니다. 
4) CommGetData 메서드를 사용해 수신 데이터를 가져옵니다. 
'''

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Kiwoom Login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        # OpenAPI+ Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        self.setWindowTitle("PyStock")
        self.setGeometry(100, 100, 1280, 800)

        btn_accno = QPushButton("계좌 얻기", self)
        btn_accno.move(20, 20)
        btn_accno.clicked.connect(self.btn_accno_clicked)

        label = QLabel('종목코드: ', self)
        label.move(20, 60)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 60)
        self.code_edit.setText("039490")

        btn_codeSearch = QPushButton("조회", self)
        btn_codeSearch.move(190, 60)
        btn_codeSearch.clicked.connect(self.btn_codeSearch_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 100, 280, 200)
        # self.text_edit.setEnabled(False)

        btn_getcodelist = QPushButton("종목코드 얻기", self)
        btn_getcodelist.move(350, 20)
        btn_getcodelist.clicked.connect(self.btn_getcodelist_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(350, 60, 300, 500)


    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

    def btn_accno_clicked(self):
        account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
        self.text_edit.append("계좌번호: " + account_num.rstrip(';'))

    def btn_codeSearch_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)

        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
        # CommRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")

            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량: " + volume.strip())

    def btn_getcodelist_clicked(self):
        '''
        원형 : BSTR GetCodeListByMarket(LPCTSTR sMarket)
        설명 : 시장구분에 따른 종목코드를 반환한다.
        입력값 : sMarket - 시장구분
        반환값 : 종목코드 리스트, 종목간 구분은 ';'이다.
        비고 : sMarket 0:장내, 3:ELW, 4:뮤추얼펀드, 5:신주인수권, 6:리츠, 8:ETF, 9:하이일드펀드, 10:코스닥, 30:제3시장
        '''
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["3"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
            kospi_code_name_list.append(x + " : " + name)

        self.listWidget.addItems(kospi_code_name_list)

########################################################################################################################
########################################################################################################################

class Main():
  def __init__(self):
    print("Main() start")

    self.app = QApplication(sys.argv) # PyQt5로 실행할 파일명을 자동 설정
    self.MyWindow = MyWindow()
    self.MyWindow.show()
    self.app.exec_() # 이벤트 루프 실행

########################################################################################################################
########################################################################################################################

if __name__ == "__main__":
    Main()

########################################################################################################################
