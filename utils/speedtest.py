import socket
import time


def tcp_ping(host, port):

	alt=0 # 平均值
	suc=0 # 丢包率
	fac=0 # 超时时间
	_list = []
	while True:
		if fac >= 3 or (suc != 0 and fac + suc >= 10):
			break
		try:
			s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			st=time.time()
			s.settimeout(3)
			s.connect((host,port))
			s.close()
			deltaTime = time.time()-st
			alt += deltaTime
			suc += 1
			_list.append(deltaTime)
		except (socket.timeout):
			fac+=1
			_list.append(0)
			print("TCP Ping Timeout %d times." % fac)
		except Exception:
			_list.append(0)
			fac+=1
	if suc==0:
		return (0,0,_list)
	return (alt/suc,suc/(suc+fac),_list)

def google_ping(address, port=443):

	alt=0
	suc=0
	fac=0
	_list = []
	while True:
		if fac >= 3 or (suc != 0 and fac + suc >= 10):
			break
		try:
			s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(3)
			s.connect((address,port))
			st=time.time()
			s.send(b"\x05\x01\x00")
			s.recv(2)
			s.send(b"\x05\x01\x00\x03\x0agoogle.com\x00\x50")
			s.recv(10)
			s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\nUser-Agent: curl/11.45.14\r\n\r\n")
			s.recv(1)
			s.close()
			deltaTime = time.time()-st
			alt += deltaTime
			suc += 1
			_list.append(deltaTime)
		except (socket.timeout):
			fac += 1
			_list.append(0)
		except Exception:
			_list.append(0)
			fac += 1
	if (suc == 0):
		return (0,0,_list)
	return (alt/suc,suc/(suc+fac),_list)

a = tcp_ping('192.186.129.66', 443)
b = google_ping('198.41.212.234')
print(a)
print(b)