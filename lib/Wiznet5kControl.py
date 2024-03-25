from usocket import socket
from machine import Pin,SPI
import network
import time

class WIZNET5KControl():
    def __init__ (self, _spi, cs_pin=Pin(17), reset_pin=Pin(20)):
           
        self.nic = network.WIZNET5K(_spi, cs_pin,reset_pin) #spi,cs,reset pin
        self.nic.active(True)

    def set_network_info(self, net_info):
        self.nic.ifconfig(net_info)
        print('IP address :', self.nic.ifconfig())
        start_time = time.ticks_ms()
        
        while True:
            if self.nic.isconnected():
                return True
            else:
                time.sleep(1)
                
            elapsed_time = time.ticks_diff(time.ticks_ms(), start_time)
            if elapsed_time > 3000:
                print("failed to network info setting up")
                return False

class WIZNET5K_Tcp:
    
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen_to_client(self, addr, listen_cnt=1):
        self.sock.bind(addr)
        self.sock.listen(listen_cnt)
        print("Listening on", addr)

    def accept_connection(self):
        conn, addr = self.sock.accept()
        print("Connected to:", addr)
        return conn, addr

    def send_data(self, conn, data):
        conn.send(data)

    def receive_data(self, conn, bufsize=2048):
        return conn.recv(bufsize)

    def loopback_server(self):
        conn, addr = self.accept_connection()
        while True:
            data = self.receive_data(conn)
            if not data:
                break
            self.send_data(conn, data)
        conn.close()

    def loopback_client(self, data_to_send):
        self.send_data(self.sock, data_to_send)
        received_data = self.receive_data(self.sock)
        print("Received back:", received_data)

class WIZNET5K_Udp():
    def __init__ (self):
        self._sock= None
        
    def connect_to_udp(self, addr):
        self.udp_sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_sock.bind(addr)
        
    #def loopback_udp(self):   



