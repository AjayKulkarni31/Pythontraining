import paramiko

nbytes = 9999
hostname = '100.100.202.245'
port = 22
username = 'root'
password = 'dell_123'
command = 'zebiversion.sh'

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
print (''.join(stdout_data.decode('utf-8')))
print (''.join(stderr_data.decode('utf-8')))

session.close()
client.close()