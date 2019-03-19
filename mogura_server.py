import socket
import threading
import time

HOSTNAME = "192.168.4.154"
PORT = 50000
CLIENTNUM = 1

class ConnClient(threading.Thread):
  def __init__(self,conn,addr):
    threading.Thread.__init__(self)
    self.stop_event = threading.Event()
    self.conn_socket = conn
    self.addr = addr

  def run(self):
    try:
      while (1):
        senddata = raw_input(str(self.addr)+" SendData:")
        self.conn_socket.send(senddata)
        recvdata = self.conn_socket.recv(1024) 
        print "ReciveData:"+recvdata 
        if (recvdata == "quit") or (senddata == "quit"):
          break

    except socket.error:
      print "connect error"

    finally:
      self.conn_socket.close()
      print "connect close"

  def stop(self):
    self.conn_socket.close()

def main():
  s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s_socket.bind((HOSTNAME, PORT))
  #s_socket.bind((socket.gethostname(), PORT))
  s_socket.listen(CLIENTNUM)

  while (1):
    conn, addr = s_socket.accept()
    print("Conneted by"+str(addr))
    connClientThread = ConnClient(conn,addr)
    connClientThread.setDaemon(True)
    connClientThread.start()    

if __name__ == '__main__':
  main()
