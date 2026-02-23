import socket 
target_host="127.0.0.1" #设置只扫描本机
target_port= 80  #设置检查80端口
try :
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建tcpl socket 对象 socket.af_inet使用IPv4地址族。socket.sock_stream使用tcp协议（面向连接的可靠传输） 
  sock.settimeout(1) #设置1秒连接超时
  result=sock.connect_ex((target_host,target_port)) #connect_ex()尝试连接到指定的主机与端口返回值为0即为端口开放
  if result == 0 :
    print(f"端口{target_port}开放")
  else :
    print(f"端口{target_host}关闭")
  sock.close() #关闭socket连接 释放系统资源 ，防止连接泄露
except Exception as e :  #捕获所有异常 Exception是所有异常的基类
  print(f"扫描出错{e}")
  
  
