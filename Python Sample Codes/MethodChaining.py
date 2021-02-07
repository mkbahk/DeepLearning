class DBConnect:
    def __init__(self, host=None, port=None, user=None, passwd=None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
    ###end of def:

    def setHost(self, host):
        self.host = host
        return self
    ###end of def:

    def setPort(self, port):
        self.port = port
        return self
    ###end of def:

    def setUser(self, user):
        self.user = user
        return self
    ###end of def:

    def setPasswd(self, passwd):
        self.passwd = passwd
        return self
    ###end of def:

    def connect(self):
        return("host: " + self.host + "\n" + 
            "port: " + self.port + "\n" + 
            "user: " + self.user + "\n" + 
            "passwd: " + self.passwd + "\n")
    ###end of def:
###end of class:

dbc = DBConnect().setHost("127.0.0.1").setPort("8080").setUser("mkbahk").setPasswd("P@ssword").connect()
print(dbc)


