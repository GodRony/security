import paramiko

class CC:
    ## 생성자 __init__
    def __init__(self, ip, user, pw, port=22):
        print("실행")
        self.ip = ip
        self.user = user
        self.pw = pw
        self.port = port
        self.client = None

    def connect(self):
        """SSH 연결"""
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=self.ip,
            username=self.user,
            password=self.pw,
            port=self.port
        )


    def run(self, cmd, print_output=True):
        """명령 실행"""
        if self.client is None:
            self.connect()

        stdin, stdout, stderr = self.client.exec_command(cmd, get_pty=True)

        out = stdout.read().decode()
        err = stderr.read().decode()

        if print_output:
            print(out if out else err)

        return out if out else err

    def close(self):
        """SSH 종료"""
        if self.client:
            self.client.close()
            self.client = None

