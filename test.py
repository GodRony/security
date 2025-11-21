from CC import CC

ssh = CC("172.16.12.100", "root", "asd123!@")

ssh.connect()
ssh.run("ls -al")
ssh.close()
