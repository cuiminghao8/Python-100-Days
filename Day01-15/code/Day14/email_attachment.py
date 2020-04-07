from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    #创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    #创建文本内容
    text_content = MIMEText('附件中有本月数据请查收' , 'plain' , 'utf-8')
    message['Subject'] = Header('本月数据' , 'utf-8')
    #将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('D:\\Download\\guido.jpg' , 'rb') as f:
        txt = MIMEText(f.read() , 'base64' , 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Desposition'] = 'attachment; filename=guido.jpg'
        message.attach(txt)

    #读取文件并将文件作为附件添加到邮件消息对象中

