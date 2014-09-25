import paramiko
execfile('pass.py')#credentials for sshing to my server.
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_host, username=ssh_usr, password=ssh_pw)
# formattedStr = yr youtubes input
stdin, stdout, stderr = \
	ssh.exec_command("python " + rm_path_to_file + formattedStr)
res = stdout.readlines()
print res