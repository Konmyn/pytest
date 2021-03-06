class VCOM(object):

    def __init__(self):
        self.__url = None
        self.__user = None
        self.__pwd = None
        self.__sign = None
        self.__gid = None
        self.__template = None
        # super(VCOM, self).__init__()

    def set(self, url, user, pwd, sign, gid, template):
        m = hashlib.md5()
        m.update(pwd)
        pwd = m.hexdigest().upper()
        print pwd
        self.__url = url
        self.__user = user
        self.__pwd = pwd
        self.__sign = sign
        self.__gid = gid
        self.__template = template

    @staticmethod
    def __send_msg_template(user='', password='', phone='', message='', sendtime='', serial=''):
        if not re.match(r'^1\d{10}$', phone):
            return ''
        # if sendtime is '':
        #     sendtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if serial is '':
            serial = str(uuid.uuid1()).replace('-', '')
        xml_temp = u"""
        <Group Login_Name="{user}" Login_Pwd="{password}" OpKind="0" InterFaceID="0" SerType="VFI">
            <E_Time>{sendtime}</E_Time>
            <Item>
                <Task>
                    <Recive_Phone_Number>{phone}</Recive_Phone_Number>
                    <Content><![CDATA[{message}]]></Content>
                    <Search_ID>{serial}</Search_ID>
                </Task>
            </Item>
        </Group>
        """
        xml_temp = xml_temp
        string = xml_temp.format(user=user, password=password, sendtime=sendtime, phone=phone, message=message,
                                 serial=serial)
        return string.encode('gbk')

    @staticmethod
    def __query_account_template(account=''):
        if account is '':
            return ''
        xml_temp = u"""
        <Root Service_Type="0">
            <Item>
                <Account_Name>{account}</Account_Name>
            </Item>
        </Root>
        """
        string = xml_temp.format(account=account)
        return string.encode('gbk')

    def sendSMS(self, phonenumber, content):
        msg = self.__template.replace("@", content)
        body = self.__send_msg_template(user=self.__user, password=self.__pwd, phone=phonenumber, message=msg)
        print body
        print "sending..."
        response = self.__Post('Opration.aspx', body)
        # if response.status_code == 200:
        #     pass
        # else:
        #     pass
        return response

    def query(self):
        body = self.__query_account_template(self.__user)
        print body
        print "querying..."
        response = self.__Post('GetResult.aspx', body)
        # if response.status_code == 200:
        #     pass
        # else:
        #     pass
        return response

    def __Post(self, address, data):
        url = urlparse.urljoin(self.__url, address)
        headers = {'content-type': 'application/x-www-form-urlencoded', 'Connection': 'close', }
        # headers = {'Content-Type': 'text/html; charset=gbk', 'Connection': 'close',}
        print url
        response = requests.post(url, data, headers=headers)
        print response.status_code
        print response.text
        return response


url = u'http://qdif.vcomcn.com'
user = u'FJSSSM'
# account = u'fjsssm00'
phone = u'15502111710'
template = u'您的订单号：@。'
ob = VCOM()
ob.set(url, user, pwd, None, None, template)
q = ob.query()
s = ob.sendSMS(phone, '123456')
