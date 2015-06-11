__author__ = 'JJW'

from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
from_addr = '1012109715@qq.com'
password = 'jjw1010238110'
to_addr = 'jiangjinwen999@live.com'
smtp_server = 'smtp.qq.com'

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


