import paramiko
import response

ip = "100.100.202.245"
username = "root"
password = "dell_123"
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(ip,port,username,password)

if response.status == 200:
    print("connected to the esxi system")
else:
    print("system is not connected to esxi system")

stdin, stdout, stderr = ssh.exec_command("ls")
outlines = stdout.readlines()
result=''.join(outlines)
print(result)
