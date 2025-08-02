import serial.tools.list_ports

def list_serial_ports():

    ports = serial.tools.list_ports.comports()
    rawPortList = [port.device for port in ports]

    portList = []
    for port in rawPortList:
        if port.upper().startswith("COM") and int(port[3:]) >= 10:
             portList.append('\\\\.\\' + port)
        else:
            portList.append(port)
    
    return portList
                    
# Example usage
if __name__ == "__main__":

    ports = list_serial_ports()
    print(ports)
    if ports:
        print("Available serial ports:")
        for port in ports:
            print(f"  - {port}")
            print(type(port))
    else:
        print("No serial ports found.")
