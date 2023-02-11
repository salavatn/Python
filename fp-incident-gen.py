'''import paramiko

# Create object of SSHClient and
# connecting to SSH
ssh = paramiko.SSHClient()

# Adding new host key to the local
# HostKeys object(in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('77.79.188.93', port=53859, username='svc-forcepoint',
            password='qaz123Z', timeout=3)

# Execute command on SSH terminal
# using exec_command
stdin, stdout, stderr = ssh.exec_command('hostname')
print(stdout)
#
#
#
# import os
#
# os.system(r'cmd /k "PolicyEngineClient.exe -o Test -src IPAddress "172.30.3.23" -i 17 -file c:\tmp\1.txt -dst DeviceName "\\FileServer\Docs"')'''

import paramiko

command = "hostname"

host = "77.79.188.93"
username = "svc-admin"
password = "WzR79ONltGKZ"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password, port=30322)
_stdin, _stdout, _stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()
