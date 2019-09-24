import sys
import webbrowser
from threading import Thread
from socket import *
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QPushButton, )
import time
from PyQt5.QtWidgets import QApplication
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


"""
class IPCThread(Thread):
    """"""
    # ----------------------------------------------------------------------
    def __init__(self):
        #Initialize
        Thread.__init__(self)

        self.HOST = ''
        self.PORT = 55000
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST, self.PORT)

        self.serverSocket = socket(AF_INET, SOCK_STREAM)

        self.serverSocket.bind(self.ADDR)

        self.serverSocket.listen(5)
        self.start()


    # ----------------------------------------------------------------------
    def run(self):
        
         #Run the socket "server"
        
        while True:
                time.sleep(0.001)
                clientSocket, addr_info = self.serverSocket.accept()

                data = clientSocket.recv(65535)
                if (data):
                    print('recieve data : ', data.decode())
                    fire_data = ("화재감지!!\n" + data.decode())
                    is_fire = 1
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.HOST = ''
        
        # Set Port Number 
        self.PORT = 55000
        
        #Set String length to receive
        self.BUFSIZE = 1024
        
        self.ADDR = (self.HOST, self.PORT)
        # Create Socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # Create Socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # Give Address to Socket
        self.serverSocket.bind(self.ADDR)
        #self.toClient = "" 


        self.label = QLabel("Waiting....")
        self.params = dict()
        self.initUI()


    #server
    def server(self):
        self.serverSocket.listen(5)
        while True:
                clientSocket, addr_info = self.serverSocket.accept()

                # get Message
                data = clientSocket.recv(65535)
                if (data):
                    print('recieve data : ', data.decode())
                    fire_data =  "Fire Detected!!\n" + data.decode()
                    self.params['text'] = fire_data
                    self.label.setText(fire_data)
                    clientSocket.close() #Close socket

    #UI
    def initUI(self):

        #Buttons!
        btn1 = QPushButton("Message", self)
        btn2 = QPushButton("Show", self)
        btn3 = QPushButton("Confirm", self)

        #버튼과 action함수 맵핑
        btn1.clicked.connect(self.btn1Action)
        btn2.clicked.connect(self.btn2Action)
        btn3.clicked.connect(self.btn3Action)


        #Message  --------------------------------------------------------------------------------------------------
        #This section is for sending messages to your phone via text
        #May not work in some areas
        
        # set api key, api secret
        #api_key = "" 
        #api_secret = "" 
        
        ## 4 params(to, from, type, text) are mandatory. must be filled
        #self.params['type'] = 'sms'  # Message type ( sms, lms, mms, ata )
        #self.params['to'] = ''  # Recipients Number '01000000000,01000000001'
        #self.params['from'] = ''  # Sender number
        #self.params['text'] = "nothing"  # Message

        #self.cool = Message(api_key, api_secret)
        #Message  end ----------------------------------------------------------------------------------------------


        #Layout(gridLayout)
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        #위취 배정
        self.grid.addWidget(self.label, 1, 1)
        self.grid.addWidget(btn1, 2, 1)
        self.grid.addWidget(btn2, 3, 1)
        self.grid.addWidget(btn3, 4, 1)

        #layout에 gridSetting삽입
        self.setLayout(self.grid)

        #위치설정
        self.setGeometry(300, 300, 350, 300)
        #title제목 설정
        self.setWindowTitle('Fire Recognition system')
        #UI show
        self.show()


        lableChangeThread = Thread(target=self.server, args=())
        lableChangeThread.start()

    def btn1Action(self):
        try:
            response = self.cool.send(self.params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

    # btn2 ACTION(url)
    def btn2Action(self):
        #Change URL to server address
        url = 'http://www.google.com'
        webbrowser.open(url)

    # btn3 ACTION(Confirm.)
    def btn3Action(self):
        self.label.setText("Waiting...")
        is_fire = 0
        #self.grid.addWidget(label1, 1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.exit(app.exec_())
