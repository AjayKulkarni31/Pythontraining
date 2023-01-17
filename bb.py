import paramiko

nbytes = 9999
hostname = '100.100.197.149'
port = 22
username = 'Administrator'
password = 'Cota@123'
command = 'dsu /v'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break
print ('exit status: ', session.recv_exit_status())
#print(stdout_data)
for x in stdout_data:
    print (''.join(x.decode('utf-8')))
#print (''.join(stderr_data.decode('utf-8')))

session.close()
client.close()