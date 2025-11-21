from CC import CC 

class DnsVhost:
    def __init__(self, cc : CC):
        print("DnsVhost init start")
        self.cc = cc 

    def test(self):
        cc.run("touch test_py.txt")
    def install(self):
        ## Rocky
        cmd = "dnf -y install httpd ; systemctl enable --now httpd"
        self.cc.run(cmd)        