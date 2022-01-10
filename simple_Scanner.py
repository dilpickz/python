import socket
import sys

def scanHost(x):
    try:
        for port in range (1, 1024):
            target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            response = target.connect_ex((x, port))
            if response == 0:
                print("Port %d is open"%port)
            else:
                pass
            target.close()
    except:
         print("Something went wrong...")

if __name__=="__main__":
    scanHost(sys.argv[1])