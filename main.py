import time 
 
import requests	 
 
import random 
 
RANDOM_IP_POOL=['192.168.10.222/0']
def __generateRandomIP__():
  str_ip = RANDOM_IP_POOL[random.randint(0,len(RANDOM_IP_POOL) - 1)]
  str_ip_addr = str_ip.split('/')[0]
  str_ip_mask = str_ip.split('/')[1]
  ip_addr = struct.unpack('>I',socket.inet_aton(str_ip_addr))[0]
  mask = 0x0
  for i in range(31, 31 - int(str_ip_mask), -1):
    mask = mask | ( 1 << i)
  ip_addr_min = ip_addr & (mask & 0xffffffff)
  ip_addr_max = ip_addr | (~mask & 0xffffffff)
  return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

 
def generateIP(): 
 
	blockOne = random.randrange(0, 255, 1) 
	 
	blockTwo = random.randrange(0, 255, 1) 
	 
	blockThree = random.randrange(0, 255, 1) 
	 
	blockFour = random.randrange(0, 255, 1) 
 
	# print 'Random IP: ' + str(blockOne) + '.' + str(blockTwo) + '.' + str(blockThree) + '.' + str(blockFour) 
 
	# if blockOne == 10: 
 
	# 	return self.generateIP() 
 
	# elif blockOne == 172: 
 
	# 	return self.generateIP() 
 
	# elif blockOne == 192: 
 
	# 	return self.generateIP() 
 
	# else: 
 
	return str(blockOne) + '.' + str(blockTwo) + '.' + str(blockThree) + '.' + str(blockFour) 
 
 
 
 
 
f =  open('proxyList_cn.txt', 'r') 
 
test_time = 1  
 
for line in f: 
 
	ipList = list(f) 
 
	for ip in ipList: 
 
		proxy = ip[:-1]#if there is \n end 
	 
		proxies = {	"http":str(proxy),	} 
	 
		headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding":"gzip, deflate", "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3", "Connection":"keep-alive", "X-Forwarded-For": "::" + generateIP() , "Content-Length":"31", "Content-Type":"application/x-www-form-urlencoded", "User-Agent":"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko/20100101 Firefox/11.0" } 
	 
	 	print headers
		print proxies 
	 
		url = 'http://xfqxk.jujiaonet.com/ysy_xfqxk/ip.php' 

		payload = {"ip":ip,"cid":2,"tid":4112}
	 
		try: 
	 
			r = requests.post(url, data=payload, proxies = proxies, headers = headers) 
	 
			print(r.text); 
	 
		except: 
	 
			print "the proxy is down" 
	 
		if test_time == 50: 
	 
			break 
	 
		test_time +=1 
	 
		time.sleep(1) 
 
 
 
 
 