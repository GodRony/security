class DnsVhost:
    def __init__(self):
        print("DnsVhost init start")
        self.VHOST_CONF = ""
        self.SERVER_NAME = ""
        self.Third_domain = []

    def getter_VHOST_CONF(self) :
        return self.VHOST_CONF

    def getter_SERVER_NAME(slef) :
        return self.SERVER_NAME
    
    def getter_Third_domain(self) :
        return self.Third_domain

    def test(self):
        return "touch test.text"

    
    def install_http_R(self):
        ## Rocky
        cmd = "dnf -y install httpd ; systemctl enable --now httpd ; dnf install expect -y"
        return cmd        


    def set_vhostconf_R(self):
        vhost_name = input("VHost 설정 파일을 세팅합니다. 원하는 이름을 입력하세요 (예: vhost.conf): ")
        self.VHOST_CONF = f"/etc/httpd/conf.d/{vhost_name}"
        self.SERVER_NAME = input("ServerName을 입력하세요. (예: test.com , ppp.com): ")
        return f"touch {self.VHOST_CONF}"

    def show_vhostconf_R(self):
        print(f"현재 {self.VHOST_CONF}의 내용은 아래와 같습니다")
        return f"cat {self.VHOST_CONF}"
    
    def mod_vhostconf_R(self):
#        
        
        WEB_DOCUMENT_ROOT = input("사용할 웹 디렉토리를 입력하세요 (예: /home/team1 또는 /var/www/young): ").strip()
        third_domain = input("3차 도메인을 입력해주세요. ServerName 생성시 필요합니다. (예: ns, wp, jl 등..): ")
        self.Third_domain.append(third_domain)
        ERROR_LOG = input("ErrorLog 경로를 입력하세요 (예: /var/log/httpd/test_error.log): ")
        CUSTOM_LOG = input("CustomLog 경로를 입력하세요 (예: /var/log/httpd/test_access.log): ")
        
        cmd = f"""
mkdir -p {WEB_DOCUMENT_ROOT} && chmod 755 {WEB_DOCUMENT_ROOT}
echo '<h1>This is index.html for Test by mk_index func</h1>' > {WEB_DOCUMENT_ROOT}/index.html

cat <<EOF >> "{self.VHOST_CONF}"
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName {third_domain}.{self.SERVER_NAME}
    DocumentRoot {WEB_DOCUMENT_ROOT}
    
    <Directory {WEB_DOCUMENT_ROOT}>
        AllowOverride None
        Options Indexes FollowSymLinks
        Require all granted
    </Directory>

    ErrorLog {ERROR_LOG}
    CustomLog {CUSTOM_LOG} combined
</VirtualHost>
EOF

"""
        return cmd

    def restart_http_R(self):
        print("httpd restart 시작")
        return "systemctl restart httpd"

