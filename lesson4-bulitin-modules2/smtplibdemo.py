import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. 邮件服务器配置
host = 'smtp.gmail.com'
port = 465 # SSL端口
user = 'kenny@example.com'
password = 'your_authorization_code' # 应用授权码

# 2. 构建邮件内容
msg = MIMEMultipart()
msg['From'] = user
msg['To'] = 'restgenwong@gmail.com'
msg['Subject'] = 'Python 自动化测试邮件'
msg.attach(MIMEText('<h1>这是一封邮件测试</h1>', 'html', 'utf-8'))

# 3. 发送邮件
try:
    # 使用SSL加密连接
    server = smtplib.SMTP_SSL(host, port)
    server.login(user, password)
    server.sendmail(user, ['recipient@example.com'], msg.as_string())
    server.quit()
    print("邮件发送成功")
except Exception as e:
    print(f"发送失败: {e}")

### 不要把真实邮箱和密码写在这里，只作为参考代码