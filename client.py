import socket
from tkinter import filedialog
from tkinter import messagebox
import cv2
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
########## SS1 Client Test ##########
# 2021.10.08
#####################################

class Client_test:

    def send_text(self,ip,port):
        msg = str(input("Send massage : "))
        if msg == "stop":
            return "f"
        if len(msg) > 12:
            print("*** ERROR_MESSAGE_TOO_LONG {0}".format(msg))
            return
        text = "TEXT" + msg
        buffer = text.encode()
        print(buffer)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓을 만든다
        client_socket.connect((ip, port)) # 접속
        client_socket.sendall(buffer)
        client_socket.close()
        return "t"

    def send_file(self,ip,port):

        """
        files = filedialog.askopenfilenames(initialdir="/Users/jyko/Downloads",
                                            title="파일을 선택 해 주세요",
                                            filetypes=(('jpg files','*.jpg'),('png files','*.png')))

        """
        head = bytearray(16)
        head[0] = ord('D')
        head[1] = ord('A')
        head[2] = ord('T')
        head[3] = ord('A')

        x = 1024 # x = sizeX
        b0 = x & 0xff
        b1 = (x >> 8) & 0xff
        b2 = (x >> 16) & 0xff
        b3 = (x >> 24) & 0xff
        head[4] = b0
        head[5] = b1
        head[6] = b2
        head[7] = b3

        y = 512 # Y = sizeY
        c0 = y & 0xff
        c1 = (y >> 8) & 0xff
        c2 = (y >> 16) & 0xff
        c3 = (y >> 24) & 0xff
        head[8] = c0
        head[9] = c1
        head[10] = c2
        head[11] = c3

        """
        img = cv2.imread(files[0])
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_1_d = np.ravel(gray) # 1차원 배열
        body_size = len(gray_1_d)
        print("body_size: ", body_size)
        body = bytearray(body_size)
        for i in range(body_size):
            body[i] = gray_1_d[i]
        """

        files = 'cat.jpg'
        with open(files, "rb") as f:
            body = f.read()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓을 만든다
        client_socket.connect((ip, port)) # 접속
        client_socket.sendall(head)
        client_socket.sendall(body)
        client_socket.close()



def main():
    ip = 'localhost'
    port = 5001
    test = Client_test()

    """
    while True:
        flag = test.send_text(ip,port)
        if flag == "f":
            break
    """
    test.send_file(ip,port)
    #file = test.select_file() # 파일 선택

if __name__ == "__main__":
	main()
