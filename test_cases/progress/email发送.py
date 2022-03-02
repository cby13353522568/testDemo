import smtplib   # 发邮件用的库
from email.mime.text import MIMEText   # 发邮件文本用的库
from email.mime.multipart import MIMEMultipart  # 带附件


# 163邮箱授权密码：NMHFAUOUDPRPWDOC   cby13353522568@163.com   cby@689689

# SMTP 服务器
SMTPServer = "smtp.163.com"
# 发送者地址
sender = "cby13353522568@163.com"
# 发送者授权密码
senderPwd = "NMHFAUOUDPRPWDOC"
# 发送内容-正文
senderMessage = MIMEMultipart()

msgMain = MIMEText("SMTP mail test")  # 将str转化为邮件文本
senderMessage.attach(msgMain)
# 标题
senderMessage['Subject'] = '我想你了'
# 发送者
senderMessage['From'] = sender
# 附件
with open('report.html', 'r', encoding='utf-8') as fp:
    attach = fp.read()
msgAttach = MIMEText(attach, 'text')
msgAttach["Content-Type"] = 'application/octet-stream'
msgAttach["Content-Disposition"] = 'attachment; filename="report.html"'
senderMessage.attach(msgAttach)

# 创建SMTP服务器，25是端口
mailServer = smtplib.SMTP(SMTPServer, 25)
# 登录邮箱
mailServer.login(sender, senderPwd)
# 发送邮件
mailServer.sendmail(sender, ['cby13353522568@163.com', '835871924@qq.com'], senderMessage.as_string())
# 退出邮箱
mailServer.quit()