from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = 'niojacsmp@nioint.com'
    receivers = ['minghao.cui@nio.com']
    message = MIMEText('用Python发送邮件的示例代码.' , 'plain' , 'utf-8')
    message['From'] = Header('王大锤' , 'utf-8')
    message['To'] = Header('崔明浩' , 'utf-8')
    message['Subject'] = Header('示例代码实验邮件' , 'utf-8')
    smtper = SMTP('smtpint.nioint.com')
    smtper.login(sender, 'MJhSqXd08hGr2dz ')
    smtper.sendmail(sender , receivers, message.as_string())
    print('邮件发送完成')


if __name__ == '__main__':
    main()
