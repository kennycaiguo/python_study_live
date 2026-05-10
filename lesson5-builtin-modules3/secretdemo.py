def secret_demo1():
    import secrets
    import string

    def generate_password(length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    # 生成12字符的随机密码
    password = generate_password()
    print(password)

def secret_demo2():
    import random
    import string

    def generate_password(length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(alphabet) for _ in range(length))
        return password

    # 生成12字符的随机密码
    password = generate_password()
    print(password)

#  生成只包含特殊字符的密码
def secret_demo3():
    import secrets
    import string

    def generate_alpha_password(length=12):
        alphabet = string.ascii_letters
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    # 生成12字符的只包含字母的随机密码
    alpha_password = generate_alpha_password()
    print(alpha_password)

# 自定义密码生成函数
def secret_demo4():
    import secrets
    import string

    def generate_custom_password(length=12):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    # 生成12字符的自定义随机密码
    custom_password = generate_custom_password()
    print(custom_password)


if __name__ == '__main__':
    # secret_demo1()
    # secret_demo2()
    # secret_demo3()
    secret_demo4()

 