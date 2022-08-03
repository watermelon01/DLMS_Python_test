from logger import Logger,getTimestamp
from serialHandler import SerialHandler,formatHexString
from dlmsErrors import dlmsErrors
from tcpIPHandler import TCPHandler

def sendReadDLMS(interface,logObject,target):
    method = str(type(interface))

    if method == "<class 'tcpIPHandler.TCPHandler'>": 
        print("---------- Method TCP --------------- ")
        print(" IP address ",interface.ip,":",interface.port)
        logObject.write("---------- Method TCP --------------- \n IP address " + interface.ip + ":" + str(interface.port) + "\n")
        print("")

    elif method == "<class 'serialHandler.SerialHandler'>":
        print("---------- Method Serial --------------- ")
        print(" Port : ",interface.comport)
        print(" Baud rate : ",interface.baudrate)
        logObject.write("---------- Method Serial --------------- \n  Port : " + interface.comport + "\n Baud rate : " + str(interface.baudrate) + "\n")
        print("")

    for x in target:
        interface.send(x)
        sendMessage = " > " + getTimestamp() + " Len " + str(int(len(x)/4)) + "\n" + formatHexString(x) 
        logObject.write(sendMessage)
        print(sendMessage)

        response = interface.read()
        if response != "":
            readMessage = " < " + getTimestamp() + " : " + "Len " + str(int(len(response)/4))+ "\n" + formatHexString(response)
            print(readMessage)
            logObject.write(readMessage)
        else: 
            print("Timeout \n")
            log.write("Timeout")

#initialize serial object
AOSserial = SerialHandler(SerialHandler.PROTOCOL_WRAPPER,comport='COM10',baudrate=9600,timeout=15)
AOSTCP = TCPHandler('123.209.69.162',4059,timeout=10)
log = Logger("logs\\NB115_1Ph\\Serial_HC1_tcp_pool_exhaust.txt",tsEnable=False)

object = AOSserial
error = dlmsErrors.HC1_tcp_pool_exhaust

#AOSTCP.connect()
AOSserial.open()

print("")
print("-------------------Sending Error Conditon-------------------")
log.write("\HC1_tcp_pool_exhaust\n")
sendReadDLMS(object,log,error)
print("-------------------Sending normal condition-------------------")
log.write("\n simple and normal \n")
sendReadDLMS(object,log,dlmsErrors.simple_and_normal)

#AOSTCP.disconnect()
AOSserial.close()