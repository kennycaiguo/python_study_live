import base64

# 原始数据
data = b"Sensitive data with + and / characters"

# 标准 Base64 编码
standard_b64 = base64.b64encode(data).decode('ascii')
print(f"标准 Base64: {standard_b64}") # 可能包含 + 和 /

# URL 安全 Base64 编码
urlsafe_b64 = base64.urlsafe_b64encode(data).decode('ascii')
print(f"URL 安全 Base64: {urlsafe_b64}") # 使用 - 和 _

# 解码 URL 安全的字符串
decoded_data = base64.urlsafe_b64decode(urlsafe_b64)
print(f"解码后数据: {decoded_data}")

assert data == decoded_data
print("✅ URL 安全编码解码成功！")
