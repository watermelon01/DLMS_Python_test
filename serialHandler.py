import serial

def StringToHex(strIn):
    numBytes = 2
    hexOut = bytearray()
    for index in range(0,len(strIn),numBytes):
        hexOut.append(int(strIn[index:index+numBytes],16))
    return hexOut

def formatHexString(strIn,length=4):
    format_spacing = ' '.join(strIn[i:i+length] for i in range(0,len(strIn),length)).upper()
    formated_newLine = '\n'.join(format_spacing[i:i+(length+1)*10] for i in range(0,len(format_spacing),(length+1)*10)).split('\n')

    strOut = ''
    address = 0
    for hexString in formated_newLine:
        strOut = strOut + str(int(address)).zfill(8) + ":  "+ hexString + "\n" 
        address = address + ((length)*10)/4

    return strOut

class SerialHandler:
    #Protocols 
    PROTOCOL_HDLC = 0
    PROTOCOL_WRAPPER = 1
    PROTOCOL_NONE = 2

    #Status Codes
    READ_SUCCESS            = 'Success'
    READ_BUFFER_EMPTY       = 'Buffer is Empty'
    READ_INVALID_PROTOCOL   = 'Invalid Protocol'
    READ_TIMEOUT            = 'Read Timeout'
    STATUS_NONE             = 'None'
    
    def __init__(self,protocol,comport,baudrate,timeout=60):
        self.comport = comport
        self.baudrate = baudrate
        self.timeout = timeout
        self.protocol = protocol
        self.status = "None"
        
        self.ser = serial.Serial(
            port = self.comport,
            baudrate = self.baudrate,
            parity='N',
            stopbits=1,
            bytesize=8,
            timeout=self.timeout 
        )

    def open(self):
        try: 
            self.ser.open()
        except IOError:
            self.ser.close()
            self.ser.open()
        except: 
            print("Port does not exist")

    def close(self):
        try: 
            self.ser.close()
        except IOError:
            print("Port access denied")
        except:
            print("Port port already closed")
    
    def send(self,message):
        hexData = StringToHex(message)
        self.ser.write(hexData)
        return hexData

    def read(self):
        response = ""

        if self.protocol == SerialHandler.PROTOCOL_WRAPPER:
            header=self.ser.read(8).hex().upper()
            if header != "":
                byteLength = int(header[-4:],16)
                try:
                    self.status = SerialHandler.READ_SUCCESS
                    response = header + self.ser.read(byteLength).hex().upper()
                except: 
                    self.status = SerialHandler.READ_TIMEOUT
            else: 
                self.status = SerialHandler.READ_TIMEOUT

        elif self.PROTOCOL_NONE == SerialHandler.PROTOCOL_NONE or self.protocol == SerialHandler.PROTOCOL_HDLC: 
            self.ser.timeout = 2
            response = self.ser.read(1024)
        else:
            self.status = SerialHandler.READ_INVALID_PROTOCOL
       
        try:
            response = response.hex().upper()
        except: 
            pass

        return response