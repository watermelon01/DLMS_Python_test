import socket

def StringToHex(strIn):
    numBytes = 2
    hexOut = bytearray()
    for index in range(0,len(strIn),numBytes):
        hexOut.append(int(strIn[index:index+numBytes],16))
    return hexOut

class TCPHandler: 
    def __init__(self,ip,port,timeout=60):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Socket on IPV4 TCP/IP

    def connect(self):
        self.socket.connect((self.ip,self.port))
    
    def disconnect(self): 
        self.socket.close()

    def send(self,message):
        self.socket.send(StringToHex(message))

    def read(self):
        self.socket.settimeout(self.timeout)
        try:
            reply = self.socket.recv(1024).hex().upper()
        except:
            reply = ""
        self.socket.settimeout(None)
        return reply


if __name__ == "__main__":
    ip = '123.209.92.134'
    port = 4059
    AOSTCP = TCPHandler(ip,port)
    AOSTCP.connect()

    AOSTCP.send("0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000")
    print(AOSTCP.read())    
    AOSTCP.disconnect()

