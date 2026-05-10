# 57. hmac

## Python的 `hmac` 模块用于实现 **[RFC 2104](https://docs.python.org/zh-cn/3/library/hmac.html)** 定义的基于哈希的消息认证码（Hash-based Message Authentication Code，简称 HMAC）算法，主要用于验证消息的完整性和认证消息的发送者 [5.3, 5.4, 5.6]。它结合了密钥和哈希函数（如 MD5, SHA256）来生成防篡改的签名

参考文档：

在当今数字化时代，数据的安全性成为重中之重，而Hash-based Message Authentication Code（[HMAC](https://zhida.zhihu.com/search?content_id=237671192&content_type=Article&match_order=1&q=HMAC&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg0MjMzNjgsInEiOiJITUFDIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjM3NjcxMTkyLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.-RS3XvuVnN9eib02G4T1ljhObC7R_d1hsA_p-HPqdIM&zhida_source=entity)）作为一种强大的加密技术，在保障数据完整性和安全性方面发挥着至关重要的作用。本篇博客将带领读者深入探索Python中HMAC模块的高级应用，通过丰富的示例代码和详细的解释，揭示HMAC在实际应用场景中的多面光芒。从基础概念到密码存储、文件完整性验证、[API安全](https://zhida.zhihu.com/search?content_id=237671192&content_type=Article&match_order=1&q=API安全&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg0MjMzNjgsInEiOiJBUEnlronlhagiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzc2NzExOTIsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.lBNfvQyR53ySCjz4i4OLw7qSm1tWbh6cxZzi634WouM&zhida_source=entity)，再到与加密算法的巧妙结合。

## **HMAC基础知识**

HMAC利用哈希函数（如[SHA-256](https://zhida.zhihu.com/search?content_id=237671192&content_type=Article&match_order=1&q=SHA-256&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg0MjMzNjgsInEiOiJTSEEtMjU2IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjM3NjcxMTkyLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.cJ0bG0lbBxHCi9GrnmBge-iHL_NLn-t9HpldE4hSFjU&zhida_source=entity)）对输入数据进行摘要计算，然后通过与密钥的结合，生成一个唯一的签名。这个签名不仅与数据内容相关，还受密钥的影响，因此即便是微小的数据变化也会导致不同的签名。这种方式保障了数据的完整性，防止因篡改而导致的安全风险。

通过使用Python的`hmac`模块，可以轻松地生成HMAC签名：

```text
import hmac
import hashlib

# 输入数据和密钥
message = b"Hello, HMAC!"
key = b"secret_key"

# 使用SHA-256哈希算法生成HMAC签名
hmac_signature = hmac.new(key, message, hashlib.sha256).digest()
```

## **HMAC的应用场景**

HMAC在实际应用中扮演着不可或缺的角色，其重要性体现在多个关键领域，包括网络通信、API验证和密码存储。通过深入探讨这些应用场景，我们能更好地理解HMAC在保障数据安全和完整性方面的强大作用。

### **1. 网络通信**

在网络通信中，数据传输的完整性至关重要。HMAC通过在数据上生成唯一的签名，可以确保发送和接收双方能够验证数据在传输过程中是否受到篡改。这种方式有效防范了[中间人攻击](https://zhida.zhihu.com/search?content_id=237671192&content_type=Article&match_order=1&q=中间人攻击&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg0MjMzNjgsInEiOiLkuK3pl7TkurrmlLvlh7siLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzc2NzExOTIsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.oYGrgvJGw98Nu6ngX31AurWxXCZeFI1JE3xY7sFMcEs&zhida_source=entity)和数据劫持，为网络通信提供了安全的保障。

```text
# 网络通信中的HMAC签名生成和验证
# 发送端
message = b"Hello, HMAC!"
key = b"secret_key"
hmac_signature = hmac.new(key, message, hashlib.sha256).digest()

# 将数据和HMAC签名一同发送

# 接收端
received_message = b"Hello, HMAC!"
received_signature = hmac.new(key, received_message, hashlib.sha256).digest()

if hmac.compare_digest(received_signature, hmac_signature):
    print("Message integrity verified.")
else:
    print("Message integrity compromised!")
```

### **2. API验证**

在API的安全性方面，HMAC常用于验证请求的真实性和合法性。通过在API请求中包含HMAC签名，服务端可以使用相同的密钥进行验证，确保请求的来源可信。这在防止伪造请求和保护API端点免受恶意攻击方面发挥着关键作用。

```text
# API请求中的HMAC签名生成和验证
# 请求端
import requests

api_url = "https://api.example.com/data"
api_params = {'param1': 'value1', 'param2': 'value2'}
api_signature = hmac.new(api_key, str(api_params).encode('utf-8'), hashlib.sha256).hexdigest()

response = requests.get(api_url, params={**api_params, 'signature': api_signature})
```

### **3. 密码存储**

在密码存储方面，HMAC结合哈希算法用于安全存储用户密码。通过将用户密码与随机生成的盐值结合，然后生成HMAC签名，可以有效防止[彩虹表攻击](https://zhida.zhihu.com/search?content_id=237671192&content_type=Article&match_order=1&q=彩虹表攻击&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg0MjMzNjgsInEiOiLlvanombnooajmlLvlh7siLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzc2NzExOTIsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.q0UxbqsskpRvDzihmP8UTkWlK7I81VBH9QYRS8NdJ8c&zhida_source=entity)和密码破解。

```text
# 密码存储中的HMAC签名生成
import bcrypt

user_password = "secure_password".encode('utf-8')
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(hmac.new(key, user_password, hashlib.sha256).digest(), salt)
```

## **HMAC与不同哈希算法的搭配**

HMAC与不同哈希算法的搭配为开发者提供了灵活性和选择余地，以适应不同的安全需求和性能要求。在实际应用中，选择合适的哈希算法与HMAC结合，涉及到权衡安全性、性能和兼容性等多个因素。

### **1. MD5与HMAC的搭配**

MD5算法在过去广泛使用，但由于其易受碰撞攻击的弱点，现已不推荐在安全性要求较高的场景中使用。然而，在一些特定情境下，如非安全性要求严格的数据完整性验证，仍可选择MD5与HMAC的搭配。

```text
# 使用MD5哈希算法生成HMAC签名
hmac_md5_signature = hmac.new(key, message, hashlib.md5).digest()
```

### **2. SHA-1与HMAC的搭配**

SHA-1在一段时间内也是常用的哈希算法，但随着安全性漏洞的被发现，逐渐不再被推荐。然而，在某些旧系统或特殊场景下，仍可选择SHA-1与HMAC的搭配。

```text
# 使用SHA-1哈希算法生成HMAC签名
hmac_sha1_signature = hmac.new(key, message, hashlib.sha1).digest()
```

### **3. SHA-256与HMAC的搭配**

SHA-256是目前广泛应用于安全领域的哈希算法，提供较高的安全性和抗碰撞能力。对于大多数安全性要求较高的场景，推荐选择SHA-256与HMAC的搭配。

```text
# 使用SHA-256哈希算法生成HMAC签名
hmac_sha256_signature = hmac.new(key, message, hashlib.sha256).digest()
```

在实际选择时，需要根据具体的安全需求来决定使用哪种哈希算法。SHA-256通常被认为是一个均衡性良好的选择，提供足够的安全性，并在性能上有着较好的表现。随着安全标准的不断演进，确保选择符合最新安全建议的哈希算法搭配，以维护系统的整体安全性。

## **HMAC的安全性考虑**

HMAC的安全性考虑至关重要，涉及防范各种攻击手段，确保数据的完整性和保密性。以下是深入研究HMAC安全性时需要考虑的关键因素：

### **1. 防范[时序攻击](https://zhida.zhihu.com/search?content_id=237671192&content_type=Article&match_order=1&q=时序攻击&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg0MjMzNjgsInEiOiLml7bluo_mlLvlh7siLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzc2NzExOTIsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.S-sfu1k4jXoFvOTVMcM5pXBN91d0hsipx8oOIYaPUQQ&zhida_source=entity)**

时序攻击（Timing Attacks）是一种利用计算机系统处理时间的差异来推断密码或密钥的攻击手段。在HMAC的应用中，防范时序攻击尤为重要。为了有效抵御时序攻击，可以采取以下措施：

- **使用`hmac.compare_digest`：** 在比较HMAC签名时，使用`hmac.compare_digest`而非简单的相等比较，以防止攻击者通过观察计算时间来推断签名的正确性。

```text
if hmac.compare_digest(received_signature, hmac_signature):
    print("Message integrity verified.")
else:
    print("Message integrity compromised!")
```

### **2. 密钥长度的选择**

密钥的长度直接关系到HMAC的安全性。过短的密钥容易受到暴力破解攻击，因此选择足够长的密钥是必要的。通常，密钥的长度应当满足哈希函数的输出长度，以确保密钥的强度。

```text
# 选择足够长的密钥
key = secrets.token_bytes(32)
```

### **3. 定期更换密钥**

定期更换密钥是一项良好的安全实践，即使密钥泄露，也能限制潜在的损害。通过定期更换密钥，可以提高系统的整体安全性。

```text
# 定期更换密钥
if need_to_change_key():
    key = generate_new_key()
```

### **4. 防止信息泄露**

在代码和系统中，避免将敏感信息（如密钥）写入日志或其他不安全的位置，以防止信息泄露导致的潜在攻击。

```text
# 避免将密钥写入不安全的位置
key = get_secure_key_from_environment()
```

通过综合考虑这些安全性因素，可以提高HMAC的抗攻击能力，确保系统在数据完整性和安全性方面表现出色。定期审查和更新安全策略，以适应不断变化的安全威胁，是保障系统长期安全性的必要步骤。

## **HMAC与API安全**

HMAC在API安全中扮演着关键的角色，通过为每个API请求生成独特的签名，确保请求的完整性和真实性。以下是HMAC在API安全中的应用步骤：

### **1. 生成HMAC签名**

在客户端发起API请求之前，需要使用密钥对请求数据生成唯一的HMAC签名。这个签名将随API请求一同发送到服务器端。

```text
import hmac
import hashlib
import requests

api_url = "https://api.example.com/data"
api_params = {'param1': 'value1', 'param2': 'value2'}
api_key = b"api_secret_key"

# 生成HMAC签名
api_signature = hmac.new(api_key, str(api_params).encode('utf-8'), hashlib.sha256).hexdigest()

# 发起API请求并携带HMAC签名
response = requests.get(api_url, params={**api_params, 'signature': api_signature})
```

### **2. 服务器端验证**

服务器端接收到API请求后，通过相同的密钥和算法，使用接收到的参数重新生成HMAC签名。然后，将服务器生成的签名与客户端发送过来的签名进行比较。

```text
# 服务器端验证HMAC签名
received_signature = request.params['signature']  # 假设从请求中获取到了签名
server_signature = hmac.new(api_key, str(received_params).encode('utf-8'), hashlib.sha256).hexdigest()

if hmac.compare_digest(server_signature, received_signature):
    print("API Request verified.")
else:
    print("API Request verification failed!")
```

通过这种方式，服务器端能够验证请求的来源，并确保请求在传输过程中没有被篡改。HMAC签名的使用有效地防止了伪造请求和中间人攻击，提高了API的安全性。

### **3. 密钥管理**

密钥的安全管理是HMAC在API安全中的关键一环。确保密钥的安全存储和定期更换是维护系统安全性的必要步骤。密钥泄露将导致潜在的安全风险，因此在密钥的生成、存储和使用过程中要谨慎处理。

```text
# 安全生成密钥
import secrets

api_key = secrets.token_bytes(32)  # 生成安全的随机密钥
```

通过HMAC的应用，API能够实现身份验证和数据完整性的双重保障。这种安全机制使得API在开放网络中能够更可靠地提供服务，同时为开发者和终端用户提供了更高层次的信任和安全性。

## **HMAC的性能优化**

HMAC的性能优化对于提高系统的效率和响应速度至关重要。以下是一些HMAC性能优化的策略：

### **1. 批量处理**

在一些场景中，可以考虑对多个数据同时进行HMAC签名计算，从而利用批量处理提高性能。这对于需要高吞吐量的系统尤其有效。

```text
import hmac
import hashlib

# 批量生成HMAC签名
data_to_process = [b"data1", b"data2", b"data3"]
key = b"secret_key"

hmac_signatures = [hmac.new(key, data, hashlib.sha256).digest() for data in data_to_process]
```

### **2. 并行计算**

利用并行计算的方式，通过多线程或多进程同时计算多个HMAC签名，从而提高计算效率。这对于大规模数据的情况下尤为有效。

```text
from concurrent.futures import ThreadPoolExecutor

# 使用线程池进行HMAC计算
def calculate_hmac(data):
    return hmac.new(key, data, hashlib.sha256).digest()

data_to_process = [b"data1", b"data2", b"data3"]

with ThreadPoolExecutor() as executor:
    result = list(executor.map(calculate_hmac, data_to_process))
```

### **3. 选择合适的哈希算法**

在实际应用中，选择合适的哈希算法也能够影响HMAC的性能。通常，SHA-256是一个良好的折衷选择，提供了较高的安全性和相对较快的计算速度。

```text
# 选择合适的哈希算法
hmac_signature = hmac.new(key, data, hashlib.sha256).digest()
```

### **4. 使用专用硬件**

对于高性能要求的场景，可以考虑使用专用的硬件加速器，如HSM（[硬件安全模块](https://zhida.zhihu.com/search?content_id=237671192&content_type=Article&match_order=1&q=硬件安全模块&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg0MjMzNjgsInEiOiLnoazku7blronlhajmqKHlnZciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzc2NzExOTIsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.25QYul3tXMpInqkPuFgg4wgm4PlkN-EMAkgEHTUWFT8&zhida_source=entity)）来进行HMAC计算。这将在硬件层面上提供更高效的计算能力。

通过这些性能优化策略，可以有效提高HMAC的计算速度，使其更适用于大规模和高性能的应用场景。在选择和实施这些策略时，需要根据具体的系统需求和性能要求进行权衡，确保在安全性和性能之间取得适当的平衡。

通过这些深入而丰富的示例代码，我们更全面地探讨了Python中HMAC模块的高级应用。读者将从基础概念到实际应用场景，了解HMAC在数据安全领域的广泛应用。希望这篇博客成为读者在HMAC学习之路上的有力助手，让他们能够更加自信地应对数据安全的挑战，保护用户和系统的隐私和完整性。在数字化时代，数据安全至关重要，而HMAC正是Python开发者的得力伙伴，共同守护着数据的安全边界。

## **总结**

总的来说，HMAC作为一种保障数据完整性和安全性的重要工具，在多个领域都发挥着关键作用。通过深入探讨HMAC的基础概念，安全性考虑，以及在API安全、文件完整性验证等方面的应用，我们更好地理解了如何利用HMAC构建安全可靠的系统。

在实际应用中，分享了如何生成HMAC签名，选择合适的哈希算法，并通过密钥管理、定期更换密钥等措施加强安全性。探讨了HMAC在网络通信、API验证、密码存储、文件完整性验证等场景中的实际应用，展示了它在保障数据传输和存储过程中的全面性能。此外，也深入研究了HMAC的性能优化策略，包括批量处理、并行计算等方法，以确保在高负载和大规模数据场景下仍能保持高效率。

在数字化时代，数据安全是至关重要的，而HMAC作为一个强大而灵活的工具，为开发者提供了一种可靠的手段来应对不断演进的安全挑战。通过合理应用HMAC的基础概念和实际场景，我们能够构建更加安全、高效的系统，为用户和开发者提供信心和便利。在未来的数字化发展中，深化对HMAC的理解和应用将成为保障数据安全的关键一环。

# 58. contextlib

今天在逛stackoverflow的时候，发现了contextlib这个模块的的作用！而且今天成功将这个模块应用到了项目中，简直爽的飞起！特此整理一篇博客，分享给大家！

一.引言

　　  我们在操作文件时最常用的就是使用with上下文管理器，这样会让代码的可读性更强而且错误更少，例如：

```
with open('/tmp/a.txt', a) as file_obj:
    file_obj.write("hello carson")
```

 

　　　 按照上述这样写的好处在于，在执行完毕缩进代码块后会自动关闭文件。同样的例子还有threading.Lock，如果不使用with，需要这样写：

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import threading
lock = threading.Lock()

lock.acquire()
try:
    my_list.append(item)
finally:
    lock.release()
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

如果使用with，那就会非常简单：

```
with lock:
    my_list.append(item)
```

创建上下文管理实际就是创建一个类，添加__enter__和__exit__方法。下面我们来实现open的上下文管理功能：

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
class OpenContext(object):

    def __init__(self, filename, mode):
        self.fp = open(filename, mode)

    def __enter__(self):
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

        
with OpenContext('/tmp/a.txt', 'a') as file_obj:
    file_obj.write("hello 6666")
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

上面我们自定义上下文管理器确实很方便，但是Python标准库还提供了更加易用的上下文管理器工具模块contextlib，它是通过生成器实现的，我们不需要再创建类以及__enter__和__exit__这两个特俗的方法：

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from contextlib import contextmanager

@contextmanager
def make_open_context(filename, mode):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()

with make_open_context('/tmp/a.txt', 'a') as file_obj:
    file_obj.write("hello carson666")
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

在上文中，yield关键词把上下文分割成两部分：yield之前就是__init__中的代码块；yield之后其实就是__exit__中的代码块，yield生成的值会绑定到with语句as子句中的变量，例如在上面的例子中，yield生成的值是文件句柄对象fp，在下面的with语句中，会将fp和file_obj绑定到一起，也就是说file_obj此时就是一个文件句柄对象，那么它就可以操作文件了，因此就可以调用file_obj.write("hello carson666")，另外要注意的是如果yield没有生成值，那么在with语句中就不需要写as子句了，后面会结合具体的例子详解。

案例一：

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# _*_ coding:utf-8 _*_
from contextlib import contextmanager

"""
contextmanager给了我们一个机会，即将原来不是上下文管理器的类变成了一个
上下文管理器，例如这里的MyResource类
"""
class MyResource:
    def query(self):
        print("query data")
@contextmanager
def make_myresource():
    print("connect to resource")
    yield MyResource()
    print("connect to resource")

with make_myresource() as r:
    r.query()
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

上面的例子就充分体现了contextmanager的强大作用，将一个不是上下问管理器的类 MyResource变成了一个上下文管理器，这样做的好处在于，我们就可以在执行真正的核心代码之前可以执行一部分代码，然后在执行完毕后，又可以执行一部分代码，这种场景在实际需求中还是很常见的。上面yield MyResource() 生成了一个实例对象，然后我们可以在with语句中调用类中的方法。看看最终的打印结果：

![img](https://images2018.cnblogs.com/blog/1220824/201804/1220824-20180413135803056-1156323241.png)

上面这样写的好处还有：假如MyResource是Flask或者其他第三方插件提供给我们的类库，如果使用自定义上下文管理器，那么就要使用手动去修改源码，在原代码的基础上添加enter和exit方法，这样做肯定不合适；现在我们可以在类MyResource的外部使用contextmanager将该类包装成为一个上下文管理器，这样既可以调用类中的方法，又可以在执行核心代码前后再执行一些相关的语句。

案例二需求

　　  我现在想打印 《且将生活一饮而尽》 也就是说我们要打印《 和 》；这就体现了上下文管理器的一个用法：我仅仅就是需要在我的核心代码前面和后面各执行一段代码而已：

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# _*_ coding:utf-8 _*_

from contextlib import contextmanager

@contextmanager
def book_mark():
    print('《', end="")
    yield
    print('》', end="")

with book_mark():
    # 核心代码
    print('且将生活一饮而尽', end="")
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

打印结果：

![img](https://images2018.cnblogs.com/blog/1220824/201804/1220824-20180413140556571-1015025662.png)

看看实际的例子，我们通常在SQLAlchemy中使用db.session.commit()，既然有commit，那就需要做一个事务的处理。因此我们需要使用try except来处理异常，如下图所示：

![img](https://images2018.cnblogs.com/blog/1220824/201804/1220824-20180424093201459-2014822094.png)

一般在应用程序中，我们都有很多个db.session.commit(),那如果都要使用try来处理异常，那就太麻烦了。我们需要做的是在核心代码之前使用try,然后在核心代码执行完毕之后，加上except。因此这就使用到了上下文管理器，此时这个db是一个第三方类库SQLAlchemy，那我们如何去为它新增加一个方法呢？那我们就继承SQLAlchemy，首先导入，然后取名字：

![img](https://images2018.cnblogs.com/blog/1220824/201804/1220824-20180424094052945-128007587.png)

![img](https://images2018.cnblogs.com/blog/1220824/201804/1220824-20180424095442483-529661114.png)

 

上面我们就为SQLAlchemy新增了一个auto_commit方法，主要实现的是自动commit()和rollback()；并将其变成了一个上下文管理器。

那么原始的代码就可以变成如下的：

![img](https://images2018.cnblogs.com/blog/1220824/201804/1220824-20180424094545546-1865653220.png)

如下，我们在保存user的时候也使用到了db.session.commit()；所以也可以改写：

![img](https://images2018.cnblogs.com/blog/1220824/201804/1220824-20180424094801963-963921214.png)

修改如下：

![img](https://images2018.cnblogs.com/blog/1220824/201804/1220824-20180424094836767-2067723397.png)

 不是上下文管理器的类，是不能使用with语句调用的。

# 59. html（parser.HTMLParser）

## 什么是 Python HTML 模块？

python中的HTML模块是专门为支持希望使用HTML的编码者而建立的。这个模块定义了HTML操作的工具。

你不需要在你的系统中安装 Python HTML 模块，因为它是内置的。要利用Python HTML模块，使用*import* 关键字来导入HTML模块。

在 Python HTML 模块中，我们有一个标准而清晰的 HTML 代码用于编码和解码。[[参考资料](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Fpython%2Fcpython%2Ftree%2F3.10%2FLib%2Fhtml)]

Python 中的*html* 模块包含两个函数：*escape()* 和*unescape(*)。

## html.escape()

使用*html.escape()* 函数，我们可以通过用 ASCII 字符替换字符串中的特殊字符来将 HTML 脚本变成一个字符串。

- **语法：**html.escape(String)
- 它从HTML中返回一个ASCII字符的字符串。

例如，考虑下面的HTML代码。

```xml
xml 体验AI代码助手 代码解读复制代码<!DOCTYPE html>
<html>
    <head>
        <title>Python HTML Module</title>
    </head>
    <body>
        <h2 style="text-align:center;">Hi , I am the HTML code</h2>
    </body>
</html>
```

我们来看看如何使用*html.escape()*函数对HTML代码进行编码。

```xml
xml 体验AI代码助手 代码解读复制代码import html

html_code = '<!DOCTYPE html> <html> <head> <title>Python HTML Module</title></head><body><h2 style="text-align:center;">Hi , I am the HTML code</h2></body></html>'

encoded_code = html.escape(html_code)
print(encoded_code)
```

输出。

![HTML encoded code](https://pythonistaplanet.com/wp-content/uploads/2022/05/image-14-1024x81.png)

Python html 模块中的*escape()* 函数被用来对 HTML 代码进行编码。它将特殊字符 (<, >,&, 等等) 改为 HTML 安全的序列。

如果可选的标志*quote*被设置为 true (默认值)，引号字符，以及双引号 (") 和单引号 (')，将被额外翻译。

你也可以手动将引号标志改为*"假*"。

```css
css 体验AI代码助手 代码解读复制代码import html

html_code = '<&!DOCTYPE html> <html> <head> <title>Python HTML Module</title></head><body><h2 style="text-align:center;">Hi , I am the HTML code</h2></body></html>'

encoded_code = html.escape(html_code,quote=False)
print(encoded_code)
```

输出。

![img](https://pythonistaplanet.com/wp-content/uploads/2022/05/Screenshot-2022-05-17-120900-1024x79.png)

## html.unescape()

简单地说，通过使用*html.unescape()* 函数，我们可以将一个 ASCII 字符串变成一个 HTML 脚本，用特殊字符代替 ASCII 字符。

- **语法：**html.unescape(String)
- 它返回一个HTML脚本。

*html.unescape()*函数只接受一个参数，即一个编码的字符串。它将字符串中所有命名的和数字的字符引用转换为相应的Unicode字符。

例如，让我们考虑以下编码的HTML代码。

```xml
xml

 体验AI代码助手
 代码解读
复制代码&lt;&amp;!DOCTYPE html&gt; &lt;html&gt; &lt;head&gt; &lt;title&gt;Python HTML Module&lt;/title&gt;&lt;/head&gt;&lt;body&gt;&lt;h2 style=&quot;text-align:center;&quot;&gt;Hi , I am the HTML code&lt;/h2&gt;&lt;/body&gt;&lt;/html&gt;
```

让我们用 *unescape()* 方法将其转换为HTML。

```xml
xml 体验AI代码助手 代码解读复制代码import html

encoded_code = '&lt;&amp;!DOCTYPE html&gt; &lt;html&gt; &lt;head&gt; &lt;title&gt;Python HTML Module&lt;/title&gt;&lt;/head&gt;&lt;body&gt;&lt;h2 style=&quot;text-align:center;&quot;&gt;Hi , I am the HTML code&lt;/h2&gt;&lt;/body&gt;&lt;/html&gt;'

html_code = html.unescape(encoded_code)
print(html_code)
```

输出。

![HTML decoding using Python unescape()](https://pythonistaplanet.com/wp-content/uploads/2022/05/image-15-1024x54.png)

*unescape()\*方法应用了HTML5标准的有效和无效字符引用准则，以及\*html.entities.html5*中指定的HTML5命名字符引用列表

## Python HTML模块中的子模块

HTML 包中的子模块有。

- 解析器
- 实体

### html.解析器

HTML 解析器是一个用于解析结构化标记的工具。它被用来解析HTML文件。

这些是该子模块中可用的一些解析器方法。

| 方法                                   | 使用案例                                                     |
| -------------------------------------- | ------------------------------------------------------------ |
| HTMLParser.handle_data(data)           | 这个方法是用来处理HTML标签之间包含的数据。                   |
| HTMLParser.handle_comment(data)        | 这个方法用来处理HTML注释。                                   |
| HTMLParser.handle_starttag(tag, attrs) | 这个方法用来处理HTML的起始标签。起始标签被包含在参数标签中，该标签的属性被包含在attrs参数中。 |
| HTMLParser.handle_endtag(tag, attrs)   | 这个方法用来处理HTML结束标签。结束标签被包含在参数标签中，该标签的属性被包含在attrs参数中。 |
| HTMLParser.feed(data)                  | 这个方法可以用来向HTML解析器提供数据。                       |

下面是一个HTML解析器应用的例子。

```xml
xml 体验AI代码助手 代码解读复制代码from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Found a start tag:", tag)

    def handle_endtag(self, tag):
        print("Found an end tag :", tag)

    def handle_data(self, data):
        print("Found some data  :", data)

parserObject = MyParser()
parserObject.feed('<!DOCTYPE html><html><head><title>Python HTML Module</title></head><body><h2 style="text-align:center;">Hi , I am the HTML code</h2></body></html>')
```

输出。

![python html parser example](https://pythonistaplanet.com/wp-content/uploads/2022/05/image-16.png)

### html.entities

html.entities 子模块包括 HTML 通用实体定义。这个模块中定义了 4 个字典，分别是*html5*、*name2codepoint*、*codepoint2name* 和*entitydefs*。

| 词典                         | 描述                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| html.entities.html5          | 一个字典，用于将HTML5命名的字符引用1转换为相应的Unicode字符，例如，html5['lt;'] == '<'。 |
| html.entities.entitydefs     | 一个字典，用于将XHTML 1.0实体定义映射为ISO Latin-1替代文本。 |
| html.entities.name2codepoint | 一个将HTML实体名称转换为Unicode代码点的字典。                |
| html.entities.codepoint2name | 一个将Unicode代码点与HTML实体名称联系起来的字典              |



# 60 .base64

# [Python 内置模块 base64：编码与解码的艺术](https://www.cnblogs.com/yuziyue/p/19032160)

在现代软件开发中，数据传输和存储无处不在。然而，并非所有系统都能安全地处理任意的二进制数据。文本协议（如电子邮件、JSON、XML）或某些网络传输层可能只支持特定的字符集。这时，就需要一种机制将二进制数据转换为纯文本格式，同时保证数据在传输后可以被完整还原。Python 的内置模块 `base64` 正是为此而生。

`base64` 模块提供了在二进制数据和 ASCII 文本之间进行编码和解码的功能。它广泛应用于数据嵌入（如将图片嵌入 HTML）、安全传输（如 HTTP Basic Auth）、以及配置文件中存储二进制信息等场景。

本文将带你深入理解 `base64` 模块，掌握其核心函数的使用方法，并了解其工作原理和实际应用。

参考文章：[Python 内置模块 base64 | 简单一点学习 easyeasy.me](https://easyeasy.me/135eb2c/)

## 一、什么是 Base64 编码？

Base64 是一种**编码（Encoding）**方案，而不是加密（Encryption）。它的主要目的是将任意的二进制数据（如图片、音频、可执行文件）转换成由 64 个可打印 ASCII 字符组成的字符串。这 64 个字符包括：

- 大写字母 A-Z (26 个)
- 小写字母 a-z (26 个)
- 数字 0-9 (10 个)
- 加号 `+` 和斜杠 `/` (2 个)

此外，`=` 字符用作填充符，确保编码后的字符串长度是 4 的倍数。

**核心原理**：

1. 将输入的二进制数据按每 3 个字节（24 位）分组。
2. 将这 24 位数据重新划分为 4 个 6 位的组。
3. 每个 6 位组的值（范围 0-63）对应 Base64 字符表中的一个字符。
4. 如果输入数据的字节数不是 3 的倍数，则使用 `=` 进行填充。

> **重要提示**：Base64 编码会增加数据量。编码后的数据大小约为原始数据的 4/3 倍（增加了约 33%）。

## 二、核心函数详解

`base64` 模块提供了多个函数用于编码和解码。最常用的是针对标准 Base64 的函数。

### 1. 编码函数

- **`base64.b64encode(s, altchars=None)`**:
  - `s`: 要编码的**字节串（bytes）**。
  - `altchars`: 可选参数，用于指定替代字符（主要用于 URL 安全的 Base64）。标准编码中通常不需要。
  - **返回值**: 一个表示编码后数据的**字节串（bytes）**。
- **`base64.b64decode(s, altchars=None, validate=False)`**:
  - `s`: 要解码的**字节串或字符串**（包含 Base64 编码的数据）。
  - `altchars`: 用于替代字符的解码。
  - `validate`: 如果为 `True`，函数会严格检查输入是否只包含有效的 Base64 字符（`A-Z`, `a-z`, `0-9`, `+`, `/`, `=`, 换行符），否则会抛出 `ValueError`。默认为 `False`，允许忽略非 Base64 字符（如空格、换行符）。
  - **返回值**: 一个表示解码后原始数据的**字节串（bytes）**。

### 2. URL 和文件名安全的变体

标准 Base64 使用的 `+` 和 `/` 在 URL 或文件名中可能需要转义。为此，Base64 提供了 URL 安全的变体：

- `base64.urlsafe_b64encode(s)`

  :

  - 与 `b64encode` 类似，但将 `+` 替换为 `-`，`/` 替换为 `_`。

- `base64.urlsafe_b64decode(s, validate=False)`

  :

  - 解码 URL 安全的 Base64 字符串。

## 三、实战应用：代码示例

让我们通过具体的代码示例来掌握 `base64` 模块的使用。

### 示例 1：基本编码与解码

```python
import base64

# 原始文本数据
original_text = "Hello, 世界! This is a test."
print(f"原始文本: {original_text}")

# 1. 将字符串编码为字节串 (UTF-8)
text_bytes = original_text.encode('utf-8')
print(f"UTF-8 字节串: {text_bytes}")

# 2. 使用 base64 编码字节串
encoded_bytes = base64.b64encode(text_bytes)
print(f"Base64 编码 (字节串): {encoded_bytes}")

# 3. 将编码后的字节串转换为字符串以便显示和传输
encoded_str = encoded_bytes.decode('ascii') # Base64 编码结果是 ASCII 安全的
print(f"Base64 编码 (字符串): {encoded_str}")

# 4. 解码过程
# 4.1 将 Base64 字符串转换回字节串
decoded_bytes = base64.b64decode(encoded_str)
print(f"解码后的字节串: {decoded_bytes}")

# 4.2 将字节串解码回原始文本
decoded_text = decoded_bytes.decode('utf-8')
print(f"解码后的文本: {decoded_text}")

# 验证
assert original_text == decoded_text
print("✅ 编码和解码成功，数据一致！")
```

**输出**：

```vbnet
原始文本: Hello, 世界! This is a test.
UTF-8 字节串: b'Hello, \xe4\xb8\x96\xe7\x95\x8c! This is a test.'
Base64 编码 (字节串): b'SGVsbG8sIOS4lueVjCEgVGhpcyBpcyBhIHRlc3Qu'
Base64 编码 (字符串): SGVsbG8sIOS4lueVjCEgVGhpcyBpcyBhIHRlc3Qu
解码后的字节串: b'Hello, \xe4\xb8\x96\xe7\x95\x8c! This is a test.'
解码后的文本: Hello, 世界! This is a test.
✅ 编码和解码成功，数据一致！
```

### 示例 2：处理二进制文件（图片）

```python
import base64

def image_to_base64(image_path):
    """将图片文件转换为 Base64 编码的字符串"""
    try:
        with open(image_path, "rb") as image_file:
            # 读取图片的二进制数据
            binary_data = image_file.read()
            # 编码为 Base64 字节串，再转为字符串
            base64_encoded = base64.b64encode(binary_data).decode('ascii')
            return base64_encoded
    except FileNotFoundError:
        print(f"错误：找不到文件 {image_path}")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

def base64_to_image(base64_string, output_path):
    """将 Base64 字符串解码并保存为图片文件"""
    try:
        # 将 Base64 字符串解码为字节串
        binary_data = base64.b64decode(base64_string)
        # 将字节串写入文件
        with open(output_path, "wb") as output_file:
            output_file.write(binary_data)
        print(f"图片已成功保存为 {output_path}")
    except Exception as e:
        print(f"保存文件时发生错误: {e}")

# --- 使用示例 ---
# 假设当前目录下有一张名为 'example.jpg' 的图片
# image_path = "example.jpg"
# output_path = "decoded_example.jpg"

# # 编码图片
# base64_str = image_to_base64(image_path)
# if base64_str:
#     print(f"图片已编码为 Base64 字符串 (长度: {len(base64_str)} 字符)")
#     # 你可以将 base64_str 存储到数据库或嵌入到 HTML/CSS 中
#     # 例如：data:image/jpeg;base64,{base64_str}

#     # 解码并保存图片
#     base64_to_image(base64_str, output_path)
```

### 示例 3：URL 安全的 Base64

```python
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
```

### 示例 4：在 HTML 中嵌入图片

```python
# 假设你已经通过 image_to_base64 函数得到了 base64_str
# base64_str = image_to_base64("logo.png")

# 构建 Data URL
# data_url = f"data:image/png;base64,{base64_str}"

# 你可以在 HTML 中直接使用
html_snippet = f"""
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg==" alt="Embedded Image">
"""
# 注意：上面的 data URL 是一个极小的 PNG 图片的 Base64 编码示例。
```

## 四、重要注意事项

1. **数据类型**: `b64encode` 的输入必须是 `bytes` 类型。字符串需要先用 `.encode()` 方法（通常是 `'utf-8'`）转换为字节串。`b64decode` 的输出是 `bytes`，通常需要用 `.decode()` 方法转换回字符串。
2. **性能**: Base64 编码/解码会增加 CPU 开销和数据大小。对于大量数据，应考虑是否真的需要 Base64。
3. **安全性**: Base64 不是加密！任何人都可以轻松地解码 Base64 数据。它只用于编码，不提供任何保密性。如果需要保密，请使用真正的加密算法（如 AES）。
4. **填充**: 标准 Base64 编码结果通常以 `=` 结尾（填充符）。在某些场景（如 JWT），可能会省略填充。解码时，`base64` 模块通常能处理省略填充的情况，但明确处理更好。
5. **错误处理**: 解码无效的 Base64 字符串会抛出 `binascii.Error`。使用 `validate=True` 可以进行更严格的输入检查。

## 五、总结

`base64` 模块是 Python 标准库中一个简单而强大的工具，它解决了二进制数据在文本环境中的传输和存储难题。通过 `b64encode` 和 `b64decode` 这两个核心函数，我们可以轻松地在二进制数据和 ASCII 文本之间转换。

**关键要点回顾**：

- Base64 是一种**编码**，不是加密。
- 编码增加约 33% 的数据量。
- 输入 `b64encode` 必须是 `bytes`。
- 输出 `b64decode` 是 `bytes`。
- 使用 `urlsafe_b64encode/decode` 处理 URL 和文件名。
- 广泛应用于数据嵌入、配置文件、API 认证等领域

# 61. platform

###  获取一些操作系统平台信息

### 参考文档：https://developer.aliyun.com/article/1640003

### 参考文档2：https://cloud.tencent.com/developer/article/1477107

# 62 . codecs

### 参考链接：https://tedboy.github.io/python_stdlib/generated/codecs.html

# 63 . cmath

### 参考链接： https://www.w3schools.com/python/module_cmath.asp

### 参考链接2：https://www.tutorialspoint.com/python/python_cmath_module.htm

# 64 . **statistics**

## statistics 模块是 Python 标准库中用于数学统计计算的模块，提供了常用的统计函数，如均值、中位数、方差、标准差等。

## 主要功能概览

### 1. 集中趋势度量

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import statistics as stats

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 算术平均数
mean = stats.mean(data)
print(f"平均数: {mean}")  # 5.0

# 中位数
median = stats.median(data)
print(f"中位数: {median}")  # 5

# 众数
data2 = [1, 2, 2, 3, 4, 4, 4, 5]
mode = stats.mode(data2)
print(f"众数: {mode}")  # 4

# 分位数
quartiles = stats.quantiles(data, n=4)
print(f"四分位数: {quartiles}")  # [3.0, 5.0, 7.0]
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

### 2. 离散程度度量

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 方差
variance = stats.variance(data)
print(f"方差: {variance}")  # 7.5

# 标准差
stdev = stats.stdev(data)
print(f"标准差: {stdev}")  # 约 2.738

# 总体方差和标准差
pvariance = stats.pvariance(data)
pstdev = stats.pstdev(data)
print(f"总体方差: {pvariance}, 总体标准差: {pstdev}")
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

### 3. 高级统计函数

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 调和平均数
harmonic_mean = stats.harmonic_mean([1, 2, 4])
print(f"调和平均数: {harmonic_mean}")  # 约 1.714

# 几何平均数
geometric_mean = stats.geometric_mean([1, 2, 4])
print(f"几何平均数: {geometric_mean}")  # 2.0

# 协方差和相关系数
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
covariance = stats.covariance(x, y)
correlation = stats.correlation(x, y)
print(f"协方差: {covariance}, 相关系数: {correlation}")
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

## 实际应用示例

### 示例1：学生成绩分析

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import statistics as stats

# 学生成绩数据
scores = [85, 92, 78, 96, 88, 76, 91, 84, 79, 87]

# 基本统计信息
print(f"平均分: {stats.mean(scores):.2f}")
print(f"中位数: {stats.median(scores)}")
print(f"最高分: {max(scores)}")
print(f"最低分: {min(scores)}")
print(f"分数范围: {max(scores) - min(scores)}")
print(f"标准差: {stats.stdev(scores):.2f}")

# 成绩分布分析
q1, q2, q3 = stats.quantiles(scores, n=4)
print(f"第一四分位数 (Q1): {q1}")
print(f"第二四分位数 (中位数, Q2): {q2}")
print(f"第三四分位数 (Q3): {q3}")
print(f"四分位距 (IQR): {q3 - q1}")
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

### 示例2：数据异常值检测

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
def detect_outliers(data):
    """使用IQR方法检测异常值"""
    q1, q3 = stats.quantiles(data, n=4)[0], stats.quantiles(data, n=4)[2]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return outliers

# 测试数据（包含一个异常值）
test_data = [10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 50]
outliers = detect_outliers(test_data)
print(f"异常值: {outliers}")  # [50]
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

### 示例3：投资组合分析

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 模拟两只股票的收益率
stock_a_returns = [0.02, 0.03, -0.01, 0.05, 0.02]
stock_b_returns = [0.01, 0.04, 0.02, -0.02, 0.03]

# 计算基本统计量
def analyze_returns(returns, name):
    print(f"\n{name}分析:")
    print(f"平均收益率: {stats.mean(returns):.3f}")
    print(f"收益率标准差: {stats.stdev(returns):.3f}")
    print(f"收益率方差: {stats.variance(returns):.6f}")

analyze_returns(stock_a_returns, "股票A")
analyze_returns(stock_b_returns, "股票B")

# 计算相关性
corr = stats.correlation(stock_a_returns, stock_b_returns)
print(f"\n两只股票的相关系数: {corr:.3f}")
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

## 错误处理

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import statistics as stats

# 处理空数据
try:
    empty_data = []
    result = stats.mean(empty_data)
except stats.StatisticsError as e:
    print(f"错误: {e}")

# 处理单一数据点
single_point = [5]
try:
    result = stats.stdev(single_point)
except stats.StatisticsError as e:
    print(f"错误: {e}")  # 需要至少两个数据点来计算标准差
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

## 与第三方库对比

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import statistics as stats
import numpy as np

data = [1, 2, 3, 4, 5]

# statistics 模块
stats_mean = stats.mean(data)
stats_std = stats.stdev(data)

# NumPy
np_mean = np.mean(data)
np_std = np.std(data, ddof=1)  # ddof=1 对应样本标准差

print(f"statistics - 均值: {stats_mean}, 标准差: {stats_std}")
print(f"NumPy - 均值: {np_mean}, 标准差: {np_std}")
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

## 总结

# `statistics`模块的特点：优点：

- Python 标准库，无需额外安装
- 接口简单易用
- 适合基本的统计计算需求
- 对初学者友好

# 局限性：

- 功能相对基础
- 性能不如 NumPy、pandas 等专业库
- 不支持多维数组操作

# 适用场景：

- 简单的数据分析任务
- 学习统计概念
- 小型项目或脚本
- 不需要复杂数据结构的场景

###  对于更复杂的统计分析，建议使用 NumPy、pandas、SciPy 等专业的数据科学库

#### 参考网址1：https://www.cnblogs.com/ityouknow/p/12987666.html

#### 参考网址2：https://github.com/JustDoPython/python-100-day/tree/master/day-040



# 65 . ssl

### ssl —套接字对象的 TLS/SSL 包装器

此模块提供对 Client 端和服务器端网络套接字的传输层安全性(通常称为“安全套接字层”)加密和对等身份验证Function的访问。该模块使用 OpenSSL 库。只要在该平台上安装了 OpenSSL，它就可以在所有现代 Unix 系统，Windows，Mac OS X 以及可能的其他平台上使用。

###### Note

由于对 os 套接字 API 进行了调用，因此某些行为可能取决于平台。安装的 OpenSSL 版本也可能导致行为变化。例如，TLSv1.1 和 TLSv1.2 随附 openssl 版本 1.0.1.

###### Warning

请勿在未阅读Security considerations的情况下使用此模块。这样做可能会导致错误的安全感，因为 ssl 模块的默认设置不一定适合您的应用程序。

#### 开始

本节记录了ssl模块中的对象和Function；有关 TLS，SSL 和证书的更多常规信息，请参阅底部“另请参阅”部分中的文档。

此模块提供了一个类ssl.SSLSocket，该类派生自socket.socket类型，并提供类似于套接字的包装器，该包装器还使用 SSL 对pass套接字的数据进行加密和解密。它支持其他方法，例如*getpeercert()*(用于检索连接另一侧的证书)和*cipher()*(用于检索用于安全连接的密码)。

对于更复杂的应用程序，ssl.SSLContext类有助于 Management 设置和证书，然后可以passpass *SSLContext.wrap_socket()* 方法创建的 SSL 套接字继承这些设置和证书。

在版本 3.5.3 中进行了更改：已更新以支持与 OpenSSL 1.1.0 链接

在版本 3.6 中更改：不建议使用 OpenSSL 0.9.8、1.0.0 和 1.0.1，并且不再支持。将来，ssl 模块将至少需要 OpenSSL 1.0.2 或 1.1.0.

#### 函数，常量和异常

Socket creation
从 Python 3.2 和 2.7.9 开始，建议使用SSLContext实例的 SSLContext.wrap_socket() 将套接字包装为SSLSocket对象。辅助函数 create_default_context() 返回具有安全默认设置的新上下文。不推荐使用旧的 wrap_socket() 函数，因为它既效率低下，也不支持服务器名称指示(SNI)和主机名匹配。

具有默认上下文和 IPv4/IPv6 双栈的 Client 端套接字示例：

```python
import socket
import ssl

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

```

具有自定义上下文和 IPv4 的 Client 端套接字示例：

```python
hostname = 'www.python.org'
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('path/to/cabundle.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

```

侦听 localhost IPv4 的服务器套接字示例：

```python
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/path/to/certchain.pem', '/path/to/private.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('127.0.0.1', 8443))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        ...

```

#### Context creation

便利Function可帮助创建SSLContext对象以用于常见目的。

> ssl. create_default_context(* purpose = Purpose.SERVER_AUTH ， cafile = None ， capath = None ， cadata = None *)
> /////
> 返回具有给定用途的默认设置的新 SSLContext 对象。这些设置由ssl模块选择，通常代表比直接调用SSLContext构造函数更高的安全级别。
> ////
> cafile ， capath ， cadata * 代表可选的 CA 证书，可信任该证书以进行证书验证，如SSLContext.load_verify_locations()。如果所有三个均为None，则此函数可以选择信任系统的默认 CA 证书。

设置为： 具有高加密密码套件的 PROTOCOL_TLS ，OP_NO_SSLv2 和 OP_NO_SSLv3 ，而 RC4 和未经身份验证的密码套件。将SERVER_AUTH用作目的会将verify_mode设置为CERT_REQUIRED并加载 CA 证书(当至少给出* cafile ， capath 或 cadata * 之一时)或使用SSLContext.load_default_certs()加载默认的 CA 证书。

如果支持keylog_filename并且设置了环境变量 SSLKEYLOGFILE，则create_default_context()启用键记录。

###### Note

协议，选项，密码和其他设置可以随时更改为更具限制性的值，而无需事先弃用。这些值表示兼容性和安全性之间的合理平衡。

如果您的应用程序需要特定的设置，则应创建一个SSLContext并自己应用设置。

###### Note

如果您发现某些较旧的 Client 端或服务器try与此Function创建的SSLContext进行连接时收到错误消息，指出“协议或密码套件不匹配”，则可能是它们仅支持 SSL3.0，但此Function不使用OP_NO_SSLv3。 SSL3.0 被广泛认为是completely broken。如果您仍然希望 continue 使用此Function但仍允许 SSL 3.0 连接，则可以使用以下方法重新启用它们：

```python
ctx = ssl.create_default_context(Purpose.CLIENT_AUTH)
ctx.options &= ~ssl.OP_NO_SSLv3

```

版本更替：

> 3.4 版的新Function。
> 在版本 3.4.4 中更改：从默认密码字符串中删除了 RC4.
> 在版本 3.6 中更改：ChaCha20/Poly1305 已添加到默认密码字符串。
> 从默认密码字符串中删除了 3 DES。
> 在 3.8 版中进行了更改：添加了对到 SSLKEYLOGFILE的密钥记录的支持。

##### Exceptions

###### exception ssl. SSLError

> 引发 signal 以指示来自基础 SSL 实现的错误(当前由 OpenSSL 库提供)。这表示在底层网络连接上叠加的更高级别的加密和身份验证层中存在一些问题。此错误是OSError的子类型。 OpenSSL 库提供了SSLError个实例的错误代码和消息。

在版本 3.3 中更改：SSLError曾经是socket.error的子类型。

```
library
AI写代码1
```

> 一个字符串助记符，指定发生错误的 OpenSSL 子模块，例如SSL，PEM或X509。可能值的范围取决于 OpenSSL 版本。

版本 3.3 中的新Function。

```
reason
AI写代码1
```

> 一个字符串助记符，指示发生此错误的原因，例如CERTIFICATE_VERIFY_FAILED。可能值的范围取决于 OpenSSL 版本。

版本 3.3 中的新Function。

exception ssl. SSLZeroReturnError
try读取或写入时引发了SSLError的子类，并且 SSL 连接已完全关闭。请注意，这并不意味着基础传输(读取 TCP)已关闭。
版本 3.3 中的新Function。

###### exception ssl. SSLWantReadError

try读取或写入数据时，由非阻塞 SSL 套接字引发的SSLError子类，但是在满足请求之前，需要在基础 TCP 传输上接收更多数据。

版本 3.3 中的新Function。

###### exception ssl. SSLWantWriteError

try读取或写入数据时由非阻塞 SSL 套接字引发的SSLError子类，但是在满足请求之前，需要在基础 TCP 传输上发送更多数据。
版本 3.3 中的新Function。

###### exception ssl. SSLSyscallError

try在 SSL 套接字上执行操作时遇到系统错误时，将引发SSLError的子类。不幸的是，没有简单的方法来检查原始的 errno 号。
版本 3.3 中的新Function。

###### exception ssl. SSLEOFError

SSL 连接突然终止时引发的SSLError子类。通常，遇到此错误时，您不应try重用基础传输。
版本 3.3 中的新Function。

###### exception ssl. SSLCertVerificationError

证书验证失败时引发的SSLError子类。
3.7 版中的新Function。

verify_code
表示验证错误的数字错误编号。
verify_message
可读的验证错误字符串。
exception ssl. CertificateError

SSLCertVerificationError的别名。
在版本 3.7 中更改：现在，exception 是SSLCertVerificationError的别名。

Random generation
ssl. RAND_bytes(* num *)
返回* num *个加密强度高的伪随机字节。如果 PRNG 尚未填充足够的数据或当前 RAND 方法不支持该操作，则引发SSLError。 RAND_status()可用于检查 PRNG 的状态，而RAND_add()可用于播种 PRNG。
对于几乎所有应用程序os.urandom()都是可取的。

阅读 Wikipedia 文章加密安全的伪随机数生成器(CSPRNG)，以获取密码生成器的要求。

版本 3.3 中的新Function。

ssl. RAND_pseudo_bytes(* num *)
返回值(字节，is_cryptographic)：字节是* num *个伪随机字节，如果生成的字节在密码上很强，则 is_cryptographic 为True。如果当前 RAND 方法不支持该操作，则引发SSLError。
如果生成的伪随机字节序列具有足够的长度，则它们将是唯一的，但不一定是不可预测的。它们可以用于非加密目的，也可以用于加密协议中的某些目的，但通常不用于密钥生成等。

对于几乎所有应用程序os.urandom()都是可取的。

版本 3.3 中的新Function。

从 3.6 版开始弃用：OpenSSL 已弃用ssl.RAND_pseudo_bytes()，而改用ssl.RAND_bytes()。

ssl. RAND_status ( )

如果已经为 SSL 伪随机数生成器提供了“足够”的随机性，则返回True，否则返回False。您可以使用ssl.RAND_egd()和ssl.RAND_add()来增加伪随机数生成器的随机性。
ssl. RAND_egd(* path *)

如果您在某个地方运行熵收集守护程序(EGD)，并且* path *是向其打开的套接字连接的路径名，则它将从套接字读取 256 个字节的随机性，并将其添加到 SSL 伪随机数中生成器以增加生成的 Secret 密钥的安全性。通常只有在没有更好随机性的系统上才需要这样做。
有关熵收集守护程序的来源，请参见http://egd.sourceforge.net/或http://prngd.sourceforge.net/。

Availability：不适用于 LibreSSL 和 OpenSSL> 1.1.0.

ssl. RAND_add(* bytes ， entropy *)
将给定的* bytes 混合到 SSL 伪随机数生成器中。参数 entropy *(浮点数)是字符串中包含的熵的下限(因此您可以始终使用0.0)。有关熵来源的更多信息，请参见 RFC 1750。
在版本 3.5 中更改：现在接受可写bytes-like object。

Certificate handling
ssl. match_hostname(* cert ， hostname *)
验证* cert (以SSLSocket.getpeercert()返回的解码格式)匹配给定的 hostname *。所应用的规则是 RFC 2818， RFC 5280和 RFC 6125中概述的用于检查 HTTPS 服务器身份的规则。除 HTTPS 之外，此Function还应适用于检查各种基于 SSL 的协议(例如 FTPS，IMAPS，POPS 等)中服务器的身份。
失败时引发CertificateError。成功时，该函数不返回任何内容：

> > > cert = {‘subject’: (((‘commonName’, ‘example.com’),),)}
> > > ssl.match_hostname(cert, “example.com”)
> > > ssl.match_hostname(cert, “example.org”)
> > > Tra

# 66 . ftplib

### 简单ftp客户端代码ftpclient_demo.py，需要自己搭建ftp站点（现在浏览器不允许访问ftp站点了）,自己创建一个用户kencai

```
from ftplib import FTP


def main(host='192.168.100.138', port=21, user='你的用户名', passwd='你的密码', start_dir=''):
    ftp = FTP()
    ftp.connect(host=host, port=port)
    ftp.login(user=user, passwd=passwd)
    ftp.cwd(start_dir)
    L = ftp.nlst()
    print(L)


if __name__ == '__main__':
    main()
```





# 67 . **imaplib**

`imaplib` 是 Python 标准库中的一个模块，提供了用于连接、管理和读取 IMAP（Internet Message Access Protocol）邮件服务器的客户端功能 [5.1, 5.3]。它通常与 `email` 模块配合使用，以解析邮件内容 [5.6]。

1. `imaplib` 核心功能概述

- **连接服务器**：支持加密（SSL/TLS）和非加密连接 [5.2]。
- **邮箱管理**：选择、创建、删除、重命名文件夹（Mailbox）[5.3]。
- **邮件操作**：搜索（Search）、获取（Fetch）、标记（Flag）、移动（Copy）和删除（Store）邮件 [5.5, 5.9]。
- **支持协议**：实现了 RFC 2060 中定义的 IMAP4rev1 协议 [5.3]。
- 核心类与连接方式

`imaplib` 定义了三个主要类 [5.3]：

- `imaplib.IMAP4(host, port)`: 非加密连接。
- `imaplib.IMAP4_SSL(host, port)`: SSL/TLS 加密连接（**推荐，最安全**）[5.2]。
- `imaplib.IMAP4_stream(command)`: 通过流连接。

**示例：使用 SSL 连接到 Gmail**

python

```
import imaplib

# 建议使用IMAP4_SSL
mail = imaplib.IMAP4_SSL('://gmail.com')
mail.login('your_email@gmail.com', 'your_password_or_app_token')
```

请谨慎使用此类代码。

3. `imaplib` 常用操作方法详解

3.1 登录与选择邮箱 (Login & Select)

python

```
# 登录
mail.login('user@example.com', 'password')

# 选择收件箱（只读方式）
mail.select('INBOX', readonly=True) 

# 选择其他文件夹，例如草稿箱
# mail.select('"[Gmail]/Drafts"')
```

请谨慎使用此类代码。

3.2 搜索邮件 (Search)

使用 `search` 方法查找符合条件的邮件 ID。

python

```
# 搜索所有邮件
status, messages = mail.search(None, 'ALL')

# 搜索未读邮件
status, messages = mail.search(None, 'UNSEEN')

# 搜索发件人为特定地址的邮件
status, messages = mail.search(None, 'FROM', '"sender@example.com"')

# 获取邮件ID列表
email_ids = messages[0].split()
```

请谨慎使用此类代码。

3.3 获取与解析邮件 (Fetch & Parse)

使用 `fetch` 获取原始邮件数据，随后用 `email` 模块解析 [5.6, 5.9]。

python

```
import email

# 获取最新一封邮件
latest_email_id = email_ids[-1]
status, data = mail.fetch(latest_email_id, '(RFC822)')

# 解析邮件内容
raw_email = data[0][1]
msg = email.message_from_bytes(raw_email)
print("Subject:", msg['Subject'])
print("From:", msg['From'])
```

请谨慎使用此类代码。

3.4 标记邮件 (Store)

python

```
# 将邮件标记为已读（添加 \\Seen 标记）
mail.store(latest_email_id, '+FLAGS', '\\Seen')

# 永久删除邮件（将邮件标记为已删除，然后执行expunge）
mail.store(latest_email_id, '+FLAGS', '\\Deleted')
mail.expunge()
```

请谨慎使用此类代码。

3.5 关闭连接 (Close & Logout)

python

```
mail.close()
mail.logout()
```

请谨慎使用此类代码。

4. `imaplib` + `email` 处理邮件内容

`imaplib` 获取的是原始字节流，通常需要用 `email` 模块解析主体和附件 [5.10]。

python

```
for part in msg.walk():
    if part.get_content_type() == "text/plain":
        # 获取纯文本内容
        body = part.get_payload(decode=True).decode()
        print(body)
    elif part.get_content_type() == "text/html":
        # 获取 HTML 内容
        html_body = part.get_payload(decode=True).decode()
```

请谨慎使用此类代码。

5. 注意事项

- **安全性**：许多邮箱服务（如 Gmail, Outlook）需要使用“应用专用密码”或开启两步验证，而不能直接使用登录密码 [5.9]。
- **缺少超时**：`imaplib` 默认没有超时设置，如果服务器响应慢，可能会导致程序长时间挂起 [5.11]。
- **字符编码**：解析邮件头（如主题）时，注意使用 `email.header.decode_header` 处理中文等特殊字符编码。
- 总结流程 [5.9]

1. `imaplib.IMAP4_SSL` 连接。
2. `login` 登录。
3. `select` 选择文件夹。
4. `search` 查找邮件 ID。
5. `fetch` 获取邮件内容。
6. `email.message_from_bytes` 解析邮件。
7. `logout` 退出。

# 68. **shelve**

 一、定义

```
Shelve是对象持久化保存方法，将对象保存到文件里面，缺省（即默认）的数据存储文件是二进制的。
```



### 二、用途

```
可以作为一个简单的数据存储方案。
```



### 三、用法

```
使用时，只需要使用open函数获取一个shelf对象，然后对数据进行增删改查操作，在完成工作、并且将内存存储到磁盘中，最后调用close函数变回将数据写入文件。
```



### 四、关联模块dbm

```
相同点：
1.dbm, shelve 都是对象持久化保存方法，将对象保存到文件里面，缺省的数据存储文件是二进制的。这两个模块允许我们将一个磁盘上的文件与一个”dict-like”对象（类字典对象）关联起来，操作这个“dict-like”对象，就像操作dict对象一项，最后可以将“dict-like”的数据持久化到文件。
2.都可以使用open函数。

区别：
dbm的key和value的类型必须都是字符串，而shelve的key要求必须是字符串，value则可以是任意合法的python数据类型。
```



### 五、方法

```
1.shelve.open(filename, flag=’c’, protocol=None, writeback=False):创建或打开一个shelve对象。shelve默认打开方式支持同时读写操作。
filename是关联的文件路径。
可选参数flag，默认为‘c’，如果数据文件不存在，就创建，允许读写；可以是: ‘r’: 只读；’w’: 可读写; ‘n’: 每次调用open()都重新创建一个空的文件，可读写。
protocol：是序列化模式，默认值为None。具体还没有尝试过，从pickle的资料中查到以下信息【protocol的值可以是1或2，表示以二进制的形式序列化】

2.shelve.close()
同步并关闭shelve对象。
注意：每次使用完毕，都必须确保shelve对象被安全关闭。同样可以使用with语句
with shelve.open('spam') as db:
    db['eggs'] = 'eggs'
```



### 六、writeback参数

```
writeback：默认为False。当设置为True以后，shelf将会将所有从DB中读取的对象存放到一个内存缓存。当我们close()打开的shelf的时候，缓存中所有的对象会被重新写入DB。
writeback方式有优点也有缺点。
优点是减少了我们出错的概率，并且让对象的持久化对用户更加的透明了；但这种方式并不是所有的情况下都需要，首先，使用writeback以后，shelf在open()的时候会增加额外的内存消耗，并且当DB在close()的时候会将缓存中的每一个对象都写入到DB，这也会带来额外的等待时间。因为shelve没有办法知道缓存中哪些对象修改了，哪些对象没有修改，因此所有的对象都会被写入。

注意：为了保存增、删、改的内容，建议显示的标明writeback=True。
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 七、代码示例
# 1.创建一个shelf对象，直接使用open函数即可

import shelve
s = shelve.open('test_shelf.db')         #
try:
    s['kk'] = {'int': 10, 'float': 9.5, 'String': 'Sample data'}
    s['MM'] = [1, 2, 3]
finally:
    s.close()

# 2.如果想要再次访问这个shelf，只需要再次shelve.open()就可以了，然后我们可以像使用字典一样来使用这个shelf

import shelve
try:
    s = shelve.open('test_shelf.db')
    value = s['kk']
    print(value)
finally:
    s.close()

# 3.对shelf对象，增、删、改操作

import shelve
s = shelve.open('test_shelf.db', flag='w', writeback=True)
try:
    # 增加
    s['QQQ'] = 2333
    # 删除
    del s['MM']
    # 修改
    s['kk'] = {'String': 'day day up'}
finally:
    s.close()

# 注意：flag设置为‘r’-只读模式，当程序试图去修改一个以只读方式打开的DB时，将会抛一个访问错误的异常。异常的具体类型取决于anydbm这个模块在创建DB时所选用的DB。异常举例：anydbm.error: need ‘c’ or ‘n’ flag to open new db

# 4.循环遍历shelf对象

import shelve
s = shelve.open('test_shelf.db')
try:
    # 方法一：
    for item in s.items():
        print ('键[{}] = 值[{}]'.format(item[0], s[item[0]]))
    # 方法二：
    for key, value in s.items():
        print(key, value)
finally:
    s.close()

# 5.备注一个错误：
# open中的参数filename，起初认为需要手动新建一个.db，或者.dat的文件，目前电脑中无任何真正的数据库文件，所以采用了新建txt文件，修改后缀的方法创建.db，或者.dat的文件。
# 解释器报错，提示内容为："anydbm.error: db type could not be determined"，
# 原因是是filename已经存在，并且格式与shelve不符，所以提示 “db type could not be determined”。
# 解决方法是，删除该文件。首次运行后会自动生成该filename文件。
# 6.稍微复杂些的案例，实现一个简单提问式的数据库

# encoding:utf-8
# 2018/3/8

# 简单的数据库

import sys,shelve

def print_help():
    '存储（增加）、查找、更新（修改）、循环打印、删除、退出、帮助'
    print('The available commons are: ')
    print('store    : Stores information about a person')
    print('lookup   : Looks up a person from ID numbers')
    print("update   : Update a person's information from ID number")
    print('print_all: Print all informations')
    print("delete   : Delete a person's information from ID number")
    print('quit     : Save changes and exit')
    print('?        : Print this message')


def store_people(db):
    pid = input('Please enter a unique ID number: ')
    person = {}
    person['name'] = input('Please enter the name: ')
    person['age'] = input('Please enter the age: ')
    person['phone'] = input('Please enter the phone: ')
    db[pid] = person
    print("Store information: pid is %s, information is %s" % (pid, person))


def lookup_people(db):
    pid = input('Please enter the number: ')
    field = input('What would you like to know? (name, age, phone) ')
    if pid in db.keys():
        value = db[pid][field]
        print("Pid %s's %s is %s" % (pid, field, value))
    else:
        print('Not found this number')


def update_people(db):
    pid = input('Please enter the number: ')
    field = input('What would you like to update? (name, age, phone)  ')
    newvalue = input('Enter the new information: ')
    if pid in db.keys():
        value = db[pid]
        value[field] = newvalue
        print("Pid %s's %s update information is %s" % (pid, field, newvalue))
    else:
        print("Not found this number, can't update")


def delete_people(db):
    pid = input('Please enter the number: ')
    if pid in db.keys():
        del db[pid]
        print("pid %s's information delete done" % pid)
    else:
        print( "Not found this number, can't delete")

def print_all_people(db):
    print( 'All information are: ')
    for key, value in db.items():
        print(key, value)

def enter_cmd():
    cmd = input('Please enter the cmd(? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('database201803.dat', writeback=True)
    try:
        while True:
            cmd = enter_cmd()
            if cmd == 'store':
                store_people(database)
            elif cmd == 'lookup':
                lookup_people(database)
            elif cmd == 'update':
                update_people(database)
            elif cmd == 'print_all':
                print_all_people(database)
            elif cmd == 'delete':
                delete_people(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__':
    main()
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;
# key必须为字符串，而值可以是python所支持的数据类型
# shelve模块(**)------可以当做数据库用，以后基本不会用，（可以很方面的往文件中写数据类型和读）
import shelve             #存取很方便（可以做一个简单的数据存储方案）
f=shelve.open(r'sheve.txt')
f['stu1_info']={'name':'egon','age':18,'hobby':['piao','smoking','drinking']}   #存
f['stu2_info']={'name':'gangdan','age':53}
f['school_info']={'website':'http://www.pypy.org','city':'beijing'}
print(f['stu1_info']['hobby'])
f.close()
 
import shelve
d=shelve.open(r'a.txt')                   #生成三个文件分别是：a.txt.bak\a.txt.dat\a.txt.dir
d['tom']={'age':18,'sex':'male'}         #存的时候会生成三个文件，不用管，是python的一种处理机制
print(d['tom']['sex'])                   #可以取出字典中的key对应的value
print(d['tom'])                          #取出tom对应的字典
d.close()

import shelve
d=shelve.open(r'a.txt',writeback=True)    #writeback=True，对子字典修改完后要写回，否则不会看到修改后的结果
d['egon']={'age':18,'sex':'male'}         #存的时候会生成三个文件，不用管，是python的一种处理机制
d['egon']['age']=20                       #将年龄修改为20
print(d['egon']['age'])                   #此时拿到的是修改后的年龄
print(d['egon']['sex'])
d.close()
```

# 69. zlib

###  用处不大，不能创建真正的压缩文件，只能够把压缩后的字符串写到一个文本文件里面

#### 参考网站：https://introspelliam.github.io/2017/07/02/misc/python%E7%94%A8%E6%A8%A1%E5%9D%97zlib%E5%8E%8B%E7%BC%A9%E4%B8%8E%E8%A7%A3%E5%8E%8B%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E6%96%87%E4%BB%B6%E7%9A%84%E6%96%B9%E6%B3%95/

#### 参考网址：https://cloud.tencent.com/developer/article/1337130

# 70. **abc** 抽象基类

## Python抽象基类使用总结(https://www.cnblogs.com/luohenyueji/p/18908981)

在Python中，抽象基类是一类特殊的类，它不能被实例化，主要用于作为基类被其他子类继承。抽象基类的核心作用是为一组相关的子类提供统一的蓝图或接口规范，明确规定子类必须实现的方法，从而增强代码的规范性和可维护性。Python通过`abc`（Abstract Base Classes）模块提供了对抽象基类的支持，允许开发者创建和使用抽象基类。

抽象基类的主要特点和用途包括：

1. 接口一致性：通过定义抽象方法，抽象基类确保所有子类必须实现这些方法，从而保证子类具有一致的接口；
2. 避免不完整实现：若子类未实现抽象基类中的所有抽象方法，该子类仍会被视为抽象基类，无法实例化；
3. 提高代码可维护性：清晰定义的接口使代码结构更清晰，便于团队协作和系统扩展。

Python要创建抽象基类，需继承`abc.ABC`并使用`@abstractmethod`装饰器标记必须被重写的方法。在实际应用中，抽象基类广泛用于以下场景：

1. 框架设计：定义接口规范，强制子类实现特定方法，确保框架扩展的一致性；
2. 插件系统：规定插件必须实现的通用接口，方便系统动态加载第三方模块；
3. 团队协作：明确模块间的交互契约，避免开发人员遗漏关键方法的实现；
4. 代码复用：通过抽象基类封装通用逻辑，子类只需实现差异化部分；
5. 类型检查：结合`isinstance()`进行运行时类型验证，确保对象符合预期接口；
6. 复杂系统架构：构建多层次的类继承体系，清晰划分各层级的职责边界。

通过合理使用抽象基类，开发者可以创建更健壮、更具扩展性的代码架构，同时减少因接口不一致导致的错误。

# 1 使用入门

**创建基础抽象基类**

以下代码展示了Python中面向对象编程的几个重要概念：

1. 抽象基类 (Abstract Base Class, ABC)

   - Animal(ABC) 是一个抽象基类，继承自ABC（需要从`abc`模块导入）。
   - 作用：抽象基类用于定义一组方法的接口规范，但不能被直接实例化。它要求子类必须实现这些方法，否则会报错。
   - 关键点：
     抽象基类通过`@abstractmethod`装饰器标记抽象方法。
     如果子类没有实现所有抽象方法，Python会阻止子类的实例化。

2. 抽象方法 (

   ```
   @abstractmethod
   ```

   )

   - move()和sound()是抽象方法，用`@abstractmethod`装饰。
   - 作用：
     - 强制子类必须实现这些方法。
     - 定义了一个统一的接口规范（例如所有动物都必须能“移动”和“发声”）。
   - 关键点：
     - 抽象方法只有声明，没有实现（用`pass`关键字占位）。
     - 如果子类不实现这些方法，尝试实例化时会引发 `TypeError`。

3. 继承 (Bird和Fish继承Animal)

   - Bird和Fish是Animal的子类。子类必须实现父类中所有的抽象方法。
   - 不同子类对同一方法有不同的实现。

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def sound(self):
        pass

class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is flying"

    def sound(self):
        return "Chirp chirp"

class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is swimming"

    def sound(self):
        return "Blub blub"

# 创建实例并调用方法
sparrow = Bird("Sparrow")
print(sparrow.move())  # 输出: Sparrow is flying
print(sparrow.sound()) # 输出: Chirp chirp

salmon = Fish("Salmon")
print(salmon.move())   # 输出: Salmon is swimming
print(salmon.sound())  # 输出: Blub blub

# animal = Animal()  # 尝试实例化抽象基类会引发TypeError
Sparrow is flying
Chirp chirp
Salmon is swimming
Blub blub
```

**抽象属性Abstract property**

以下示例将name方法声明为抽象属性，要求所有继承Person的子类必须实现这个属性。使用`@property`表示这应该是一个属性而不是普通方法。通过`@property`装饰器，用于将类的方法转换为"属性"，使得可以像访问属性一样访问方法，而不需要使用调用语法（即不需要加括号）。注意子类必须同样使用`@property`装饰器来实现该属性。

使用`@property`的优势在于能够控制访问权限,定义只读属性，防止属性被意外修改。例如：

```python
emp = Employee("Sarah", "Johnson")
emp.name = "Alice"  # 会报错，AttributeError: can't set attribute
```

示例代码如下：

```python
from abc import ABC, abstractmethod

class Person(ABC):
    """抽象基类，表示一个人"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """获取人的姓名"""
        pass

    @abstractmethod
    def speak(self) -> str:
        """人说话的抽象方法"""
        pass

class Employee(Person):
    """表示公司员工的类"""
    
    def __init__(self, first_name: str, last_name: str):
        """
        初始化员工对象
        
        Args:
            first_name: 员工的名字
            last_name: 员工的姓氏
        """
        if not first_name or not last_name:
            raise ValueError("名字和姓氏不能为空")
        self._full_name = f"{first_name} {last_name}"

    @property
    def name(self) -> str:
        """获取员工的全名"""
        return self._full_name

    def speak(self) -> str:
        """员工打招呼的具体实现"""
        return f"Hello, my name is {self.name}"

# 创建员工实例并测试
emp = Employee("Sarah", "Johnson")
# emp.name = "Alice"  # 会报错，AttributeError: can't set attribute
print(emp.name)    # 输出: Sarah Johnson
print(emp.speak()) # 输出: Hello, my name is Sarah Johnson
Sarah Johnson
Hello, my name is Sarah Johnson
```

**带类方法的抽象基类**

当方法不需要访问或修改实例状态（即不依赖`self`属性）时，使用类方法可以避免创建不必要的实例，从而提高效率并简化代码。

```python
from abc import ABC, abstractmethod

# 抽象基类：包裹
class Package(ABC):
    
    @classmethod
    @abstractmethod
    def pack(cls, items):
        pass
    
    @classmethod
    @abstractmethod
    def unpack(cls, packed_items):
        pass

# 具体实现类：纸箱包裹
class CardboardBox(Package):
    
    @classmethod
    def pack(cls, items):
        return f"纸箱包裹: {items}"
    
    @classmethod
    def unpack(cls, packed_items):
        return packed_items.replace("纸箱包裹: ", "")

# 具体实现类：泡沫包裹
class FoamPackage(Package):
    
    @classmethod
    def pack(cls, items):
        return f"泡沫包裹: {items}"
    
    @classmethod
    def unpack(cls, packed_items):
        return packed_items.replace("泡沫包裹: ", "")

# 打包物品
cardboard_packed = CardboardBox.pack(["衣服", "鞋子"])
foam_packed = FoamPackage.pack(["玻璃制品", "陶瓷"])

# 解包物品，使用不同的对象
cardboard_items = CardboardBox.unpack(cardboard_packed)
foam_items = FoamPackage.unpack(foam_packed)

# 输出结果
print("解包后 - 纸箱:", cardboard_items) 
print("解包后 - 泡沫:", foam_items)     
解包后 - 纸箱: ['衣服', '鞋子']
解包后 - 泡沫: ['玻璃制品', '陶瓷']
```

**带有具体方法的抽象基类**

该示例呈现了一个兼具抽象方法与具体方法（实例方法）的抽象基类。抽象基类中既包含子类必须实现的抽象方法，也有提供共享功能的具体方法。`operate`具体方法界定了 “启动→运行→停止” 的通用操作流程，而具体实现则由子类负责。此模式让抽象基类能够把控算法结构，同时将细节实现延迟至子类。这不仅提升了代码的可维护性，还便于在不改动现有代码结构的前提下添加摩托车、飞机等新的交通工具。

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def operate(self):
        self.start()
        print("Vehicle is in operation...")
        self.stop()

class Car(Vehicle):
    def start(self):
        print("Starting car engine")

    def stop(self):
        print("Turning off car engine")

class Bicycle(Vehicle):
    def start(self):
        print("Starting to pedal bicycle")

    def stop(self):
        print("Applying bicycle brakes")

# 使用示例
car = Car()
car.operate()

bicycle = Bicycle()
bicycle.operate()
Starting car engine
Vehicle is in operation...
Turning off car engine
Starting to pedal bicycle
Vehicle is in operation...
Applying bicycle brakes
```

**非显式继承**

这个示例展示了如何在不进行显式继承的情况下，将类注册为抽象基类的虚拟子类。`register`方法允许声明某个类实现了抽象基类，却无需直接继承该基类。

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car:
    def move(self):
        return "Driving on the road!"

# 注册Car类为Vehicle的虚拟子类
Vehicle.register(Car)  

car = Car()
# 输出: True（因为 Car 已被注册为 Vehicle 的虚拟子类）
print(isinstance(car, Vehicle)) 
# 输出: True（同上）
print(issubclass(Car, Vehicle)) 
print(car.move())
True
True
Driving on the road!
```

一般来说虚拟子类必须实现所有的抽象方法，但这种检查要等到尝试调用这些方法时才会进行。在处理无法修改的类或者使用鸭子类型时，这种方式十分实用。注意鸭子类型是Python中的一个重要编程概念，源自一句谚语："如果它走起来像鸭子，叫起来像鸭子，那么它就是鸭子"（If it walks like a duck and quacks like a duck, then it must be a duck）。

在Python中，鸭子类型指的是：

- 不关注对象的类型本身，而是关注对象具有的行为（方法或属性）；
- 只要一个对象具有所需的方法或属性，它就可以被当作特定类型使用，而不需要显式地继承或声明。

示例代码如下，`duck_test`函数并不关心传入的对象是Duck还是Person，只要该对象拥有`quack`和`walk`方法，就可以正常调用。

```python
class Duck:
    def quack(self):
        print("嘎嘎嘎")

    def walk(self):
        print("摇摇摆摆地走")

class Person:
    def quack(self):
        print("人类模仿鸭子叫")

    def walk(self):
        print("人类两条腿走路")

def duck_test(duck):
    duck.quack()
    duck.walk()

# 创建Duck和Person的实例
donald = Duck()
john = Person()

# 调用duck_test函数
duck_test(donald)
duck_test(john)
嘎嘎嘎
摇摇摆摆地走
人类模仿鸭子叫
人类两条腿走路
```

**多重继承**

以下例子展示了抽象基类在多重继承中的应用。通过多重继承，可以将多个抽象基类组合，创建出能实现多种接口的类。例如，`RadioRecorder`类同时继承了`Listenable`和`Recordable`两个抽象基类，并实现了它们的所有抽象方法。这种方式既满足了严格的实现要求，又能灵活地定义接口。

```python
from abc import ABC, abstractmethod

# 定义可收听的抽象接口
class Listenable(ABC):
    @abstractmethod
    def listen(self):
        pass

# 定义可录制的抽象接口
class Recordable(ABC):
    @abstractmethod
    def record(self, content):
        pass

# 收音机录音机实现类
class RadioRecorder(Listenable, Recordable):
    def __init__(self, channel):
        self.channel = channel  # 收音机频道
        self.recording = []     # 录制内容存储

    def listen(self):
        return f"Listening to {self.channel}"

    def record(self, content):
        self.recording.append(content)
        return f"Recording '{content}' on {self.channel}"

# 使用示例
radio = RadioRecorder("FM 98.6")
print(radio.listen())          
print(radio.record("Music"))    
Listening to FM 98.6
Recording 'Music' on FM 98.6
```

如果两个抽象基类有相同的方法名，会导致方法冲突。 Python中，当多重继承的父类存在同名方法时，调用顺序由方法解析顺序。例如以下代码中抽象基类都存在change方法，在子类change方法内部可以根据参数类型分别处理不同的逻辑来避免冲突：

```python
from abc import ABC, abstractmethod

# 定义可收听的抽象接口
class Listenable(ABC):
    @abstractmethod
    def listen(self):
        pass
    
    @abstractmethod
    def change(self, channel):
        """切换收听频道"""
        pass

# 定义可录制的抽象接口
class Recordable(ABC):
    @abstractmethod
    def record(self, content):
        pass
    
    @abstractmethod
    def change(self, format):
        """切换录制格式"""
        pass

# 收音机录音机实现类
class RadioRecorder(Listenable, Recordable):
    def __init__(self, channel, format):
        self.channel = channel  # 收音机频道
        self.format = format    # 录制格式
        self.recording = []     # 录制内容存储

    def listen(self):
        return f"Listening to {self.channel}"

    def record(self, content):
        self.recording.append(content)
        return f"Recording '{content}' in {self.format}"
    
    # 解决方法冲突
    def change(self, param):
        # 根据参数类型判断调用哪个父类的change方法
        if isinstance(param, str):  # 假设字符串参数是频道
            self.channel = param
            return f"Changed channel to {param}"
        elif isinstance(param, int):  # 假设整数参数是格式编号
            formats = ["MP3", "WAV", "FLAC"]
            if 0 <= param < len(formats):
                self.format = formats[param]
                return f"Changed format to {self.format}"
        return "Invalid parameter"

# 使用示例
radio = RadioRecorder("FM 98.6", "MP3")
print(radio.listen())          
print(radio.record("Music"))   
print(radio.change("AM 1070"))  
print(radio.change(2))         
Listening to FM 98.6
Recording 'Music' in MP3
Changed channel to AM 1070
Changed format to FLAC
```

此外在Python的多重继承中，方法解析顺序（Method Resolution Order, MRO)是一个重要的概念，它决定了当子类调用一个方法时，Python解释器会按照什么顺序在父类中查找这个方法。MRO的规则：

- 深度优先，从左到右：Python会先检查第一个父类及其祖先，然后再检查第二个父类及其祖先，以此类推。
- C3线性化算法：Python2.3之后使用C3线性化算法计算MRO，确保每个类只被访问一次，解决了经典类中的 "菱形继承" 问题。

以上述代码为例，RadioRecorder继承自Listenable和Recordable。Listenable排在Recordable前面，这意味着当两个父类有同名方法时，Listenable的方法会被优先调用。因此这里的MRO顺序是：RadioRecorder -> Listenable -> Recordable -> object。这意味着：

- 当调用radio.change()时，Python 会先在RadioRecorder中查找change方法。
- 如果没找到，会在Listenable中查找。
- 如果还没找到，会在Recordable中查找。
- 最后查找object类（所有类的基类）。

可以使用`__mro__`属性或`mro()`方法查看类的MRO顺序：

```python
print(RadioRecorder.__mro__)
(<class '__main__.RadioRecorder'>, <class '__main__.Listenable'>, <class '__main__.Recordable'>, <class 'abc.ABC'>, <class 'object'>)
```

# 2 参考

- [Python Abstract Classes](https://zetcode.com/python/abstract-classes/)
- [Python MRO方法解析顺序详解](https://www.zhihu.com/tardis/zm/art/416584599)



![img](https://gitlab.com/luohenyueji/article_picture_warehouse/-/raw/main/wechat/content/%E5%8A%A0%E6%B2%B9%E9%B8%AD.gif)



# 71. **inspect**

### Python中的`inspect`模块解析

Python的`inspect`模块是一个强大的内省工具，允许开发者检查（inspect）活动对象和源代码。它提供了一系列函数，用于获取信息关于正在运行的程序和调用堆栈，非常适合进行调试和动态分析。本文将通过介绍`inspect`模块的关键功能，并结合实际案例代码，来探索其在日常开发中的应用。



### 常用方法



#### 1. 获取当前执行的函数或方法名、文件路径【并不是调用方】

在日志记录或调试时，知道当前执行的函数名是非常有用的

```python
import inspect

def who_am_i():
    # 输出当前文件绝对路径
    print(inspect.currentframe().f_code.co_filename)
    return inspect.currentframe().f_code.co_name

print(who_am_i())  # 输出: who_am_i
```

[![img](https://cdn.nlark.com/yuque/0/2024/png/25442796/1711425445313-964f1d5a-0a94-42c3-bd27-09f9e526bb15.png#averageHue=%232f3e45&clientId=u34573b38-712c-4&from=paste&height=503&id=u87ec7339&originHeight=503&originWidth=411&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63071&status=done&style=none&taskId=u7e8af34b-31f1-4921-b5d4-72f401b482f&title=&width=411)](https://cdn.nlark.com/yuque/0/2024/png/25442796/1711425445313-964f1d5a-0a94-42c3-bd27-09f9e526bb15.png#averageHue=%232f3e45&clientId=u34573b38-712c-4&from=paste&height=503&id=u87ec7339&originHeight=503&originWidth=411&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63071&status=done&style=none&taskId=u7e8af34b-31f1-4921-b5d4-72f401b482f&title=&width=411)
个人认为比较有用的就是 co_filename、co_name



#### 2. 获取调用者信息

获取当前函数或方法的调用者信息

```python
import inspect

def caller_info():
    frame = inspect.currentframe().f_back
    print(f调用者 {frame.f_code.co_filename} 调用行号 d{frame.f_lineno}")

def test():
    caller_info()  # 调用以获取调用者信息

test()
```

这个例子显示了如何获取调用当前函数的代码位置，非常有助于调试复杂的调用链



#### 3. 查看函数参数

`inspect`模块可以用来检查函数或方法的参数，这对于动态分析和生成文档非常有用

```python
import inspect

def sample_function(name, age=25):
    pass

sig = inspect.signature(sample_function)
print(sig)  # 输出: (name, age=25)
```



#### 4. 获取源代码

`inspect`还可以用来获取函数、类或模块的源代码

```python
import inspect

def my_function():
    """A simple function."""
    pass

print(inspect.getsource(my_function))
```



#### 5. 检查类和实例

`inspect`模块提供了多种方式来检查类和实例，比如获取类的所有方法、属性等

```python
class MyClass:
    def method_one(self):
        pass
    
    def method_two(self):
        pass

# 获取类的所有成员方法
methods = inspect.getmembers(MyClass, predicate=inspect.isfunction)
print(methods)  # 输出 MyClass 中定义的方法
```



### 实际案例：自动化场景下的应用

一个常见的使用场景是动态地调用函数或方法，并基于它们的签名自动生成文档。

```python
def test():
    # 获取调用方
    frame = inspect.currentframe().f_back
    # 获取调用方文件绝对路径
    caller_file = inspect.getfile(frame)
    # 这种方式也可以
    caller_file = frame.f_code.co_filename

    ...
    
    params = [
        caller_file,
        "--env-data",
        env_data.json(),
        f"--count={count}",
        "-m",
        mark,
    ]
```

一个基于 Pytest 自动化测试项目

1. 每个 py 模块都会调用这个方法来执行 Pytest 命令来跑测试用例
2. 那怎么才能准确知道要跑哪个文件呢？
3. 通过第一、二行代码即可

# 72. warnings

Python 的 `warnings` 模块用于在运行时发出非致命性提示（即警告），用于提醒用户代码存在潜在问题（如使用过时函数、不兼容配置等），而不会中断程序执行 [5.1, 5.2, 5.5]。其核心功能包括：调用 `warn()` 函数产生警告、通过过滤器 (`filterwarnings`) 控制警告的显示或忽略、以及自定义警告类别 [5.1, 5.7, 5.8]。

1. 核心功能与使用方法

- **发出警告 (`warnings.warn`)**：

  python

  ```
  import warnings
  warnings.warn("这是一个废弃函数警告", DeprecationWarning)
  ```

  请谨慎使用此类代码。

  它支持参数包括：`message`（信息）、`category`（警告类）、`stacklevel`（提示出错位置）[5.4, 5.6]。

- **过滤规则 (`warnings.filterwarnings`)**：
  可以通过规则控制警告是显示、忽略还是转为异常 [5.7]。

  python

  ```
  # 忽略所有警告
  warnings.filterwarnings("ignore")
  # 忽略特定警告类
  warnings.filterwarnings("ignore", category=DeprecationWarning)
  # 将特定警告作为异常抛出
  warnings.filterwarnings("error", message=".*function is deprecated")
  ```

# 73. doctest

Doctest是一个轻量级的单元测试框架，官方对其定义如下：

> doctest 模块寻找像Python交互式代码的文本，然后执行这些代码来确保它们的确就像展示的那样正确运行，有许多方法来使用doctest：

## 示例

```python3
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

上面示例里面，factorial的[docstring](https://zhida.zhihu.com/search?content_id=145303564&content_type=Article&match_order=1&q=docstring&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg1MzIzNTAsInEiOiJkb2NzdHJpbmciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNDUzMDM1NjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.0gqVor36rk8vQqFYLweOsI6dp-dO8WPiMDnjJtOwtTQ&zhida_source=entity)里面的就是测试代码。仔细看的话会不会觉得这些测试代码很眼熟。

![img](https://pic4.zhimg.com/v2-f793d6c767d69b56bc78b1bba229760b_1440w.jpg)



没错，doctest的测试代码就跟[Python交互式控制台](https://zhida.zhihu.com/search?content_id=145303564&content_type=Article&match_order=1&q=Python交互式控制台&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3Nzg1MzIzNTAsInEiOiJQeXRob27kuqTkupLlvI_mjqfliLblj7AiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNDUzMDM1NjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.LhVak_dXt_GSfjbpJe0drQBseTC0s_0LSb_x8ccaC_g&zhida_source=entity)（命令行里输入python跑起来的那个）里的打印一样。

**所以其实Doctest的测试原理是把我们在Python控制台的输入输出记录保存到函数的docstring里，然后一一把这些输入到解析器然后对比输出是否一致用来确定测试结果是否通过。**

说到这里其实docstring基本都讲完了，为什么?

因为你只需要把自己平时在Python交互式控制台上测代码时的输入输出记录，拷贝到docstring里，以后要回归这个函数的时候就可以通过doctest回放测试用例了。至于Python交互式控制台怎么用、怎么测代码，这个跟呼吸吃饭拉屎睡觉一样就不讲了。

## 测试用例基本格式规范

虽然，我们直接把Python交互式控制台的记录直接复制到docstring就是一个可执行的测试用例，但是docstring仍然有些自己的特性和规范的。

### 输入

```bash
>>>
... 
```

`>>>` `...` 这个跟交互控制台的概念是一样的。

### 注释

```bash
>>> # 这是一段注释
```

### 测试代码

```bash
>>> a = 0
... for i in range(10):
...       a=i
```

### 预期结果（输出）

在测试代码后面紧跟文本，就是预期结果，对应就是交互控制台的输出内容。Doctest会拿这些文本去跟测试代码执行的结果对比。

**直接结果**

```bash
9
```

**异常结果**

```bash
Traceback (most recent call last):
        ...
    <异常类型>: <异常信息>
[要空一行]
这里可以写点注释
```

异常结果会匹配 Traceback (most recent call last): 到 <异常类型>: <异常信息>，`...` 的意思是忽略中间行。

## 讲测试用例保存到外部文件

函数如果功能简单直接在docstring里写用例其实还不错，但是如果函数功能比较复杂，测试用例比较多，那么写到docstring里就太长了。Doctest支持把测试代码抽离到另外一个txt里，然后通过解析txt的方式运行用例。

```python3
# doctest只会解析>>>和>>>的下一行（输出）,其他文本会被忽略。
The ``example`` module   # 所以这个不过是个注释
==================

Using ``factorial``  # 这个也是注释
------------------

First import factorial function # 这个是个注释，你喜欢用中文写也行
    >>> from example import factorial  # 这行就是输入命令了

Now use it  # 这个是个注释
    >>> [factorial(n) for n in range(6)]  # 这里到下面就全是测试用例代码了
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
```

## 执行文本用例

执行文本用例的途径有两个

直接命令行调用doctest模块运行文本用例

```bash
python -m doctest -v example.txt
```

但是要注意，你在哪个目录下调用就意味着当前工作目录（cwd）就在那里，这会影响文本用例里`import`查找模块。举个例子，[你把上面的用例文本放到了example.py](https://link.zhihu.com/?target=http%3A//xn--example-fw3k59ai3dtn75xzp1d45hj5aq6q1w0e7dfur6p.py/) 同目录的一个test文件夹里，那么你就该在example.py目录下去调用doctest模块。这样`>>> from example import factorial`[这段代码才能够找到example.py](https://link.zhihu.com/?target=http%3A//xn--example-0b5kk9vevstzx3qah27gi89a0f2a3x3c.py/)。总之就是个模块查找问题。

```bash
python -m doctest -v test/example.txt
```

在py脚本里调用

```bash
doctest.testfile('example_text.txt')
```

这个方式适合一次运行所有的文本用例。

### 总结

Doctest真的是个十分冷门小众的单元测试框架，看过那么多开源项目就没见过用Doctest做单元测试的。这个框架本身属于小品级别，看看就好，实际甚少应用。还是Pytest Unittest之流比较入流

# 74 . **asyncio**

## [Python异步编程库asyncio使用](https://www.cnblogs.com/luohenyueji/p/18562526)

Python的`asyncio`模块提供了基于协程（coroutines）的异步编程（asynchronous programming）模型。作为一种高效的编程范式，异步编程允许多个轻量级任务并发执行，且相比传统的多线程模型，具有更低的内存消耗。因此，`asyncio`在需要高并发处理的场景中，尤其是在Web开发、网络请求、API调用和套接字编程等领域，得到了广泛应用。本文将详细介绍如何在Python中使用`asyncio`进行异步编程。

本文在学习`asyncio`的过程中参考了以下文献：

- [asyncio — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [Python Asyncio: The Complete Guide](https://superfastpython.com/python-asyncio/)
- [深度解密 asyncio](https://www.cnblogs.com/traditional/tag/深度解密 asyncio/)

# 1 异步编程介绍

异步编程是一种非阻塞的编程范式。在这种范式中，请求和函数调用会在未来某个时刻以某种方式在后台执行。非阻塞意味着当一个请求被发出时，程序不会停下来等待该请求的结果，而是会继续执行后续的操作。当请求的结果准备好时，程序会在适当的时机处理该结果，而不会影响程序其他部分的执行。因此，调用者可以继续执行其他任务，并在结果准备好或需要时，稍后处理已发出的调用结果。

## 1.1 什么是异步任务

异步操作指的是在程序运行时，有些任务不会立即完成，而是安排在未来某个时刻执行。与同步操作不同，后者要求任务在当前步骤中完成。

**异步函数调用**（Asynchronous Function Call）是实现异步操作的一种方式。这种方式允许程序在等待某些任务完成时，继续执行其他工作，从而避免程序被卡住，提升效率。

通常，异步函数调用会返回一个被称为“未来”（Future）的对象（句柄）。这个对象可以看作是一个指向异步操作结果的标识符。程序可以通过它来查看任务的进度，或者等到任务完成时获取最终结果。这样，程序就可以在等待任务完成时做其他事情，而不是一直停下来等。

结合异步函数调用和Future，就得到了**异步任务**（Asynchronous Task）的概念。异步任务不仅仅是调用一个函数，它还包括了如任务取消、错误处理等更多的内容。这样，程序就可以更加灵活和高效地管理多个任务，提高并发性和整体性能。

简单来说，以下是这几个概念的总结：

- **异步函数调用**：指触发一个函数执行的请求，它会在未来某个时刻开始执行，而不会阻止程序继续做其他事情。
- **Future**：是异步函数调用的一个标识符，允许调用者检查任务的状态，并在任务完成时获取结果。
- **异步任务**：指代一个包含异步函数调用和结果（Future）的集合，用于管理和跟踪整个异步操作的过程。

![img](https://gitlab.com/luohenyueji/article_picture_warehouse/-/raw/main/CSDN/%5Bpython%5D%20Python%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B%E5%BA%93asyncio%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8C%97/img/img1.jpg)

## 1.2 Python中的异步编程

### 1.2.1 非阻塞I/O与异步编程

输入input/输出output，简称I/O，指的是从资源中读取或写入数据。以下是I/O操作的一些典型应用场景：

- 硬盘驱动器：对文件进行读取、写入、追加、重命名、删除等操作。
- 外围设备：鼠标、键盘、屏幕、打印机、串行设备、摄像头等。
- 互联网：下载和上传文件、获取网页、查询RSS等。
- 数据库：执行选择、更新、删除等SQL查询。
- 电子邮件：发送邮件、接收邮件、查询收件箱等。

相较于中央处理器（CPU）执行的计算任务，I/O操作通常具有较低的效率。在程序设计中，I/O请求通常以同步方式实现，即发起I/O请求的线程在数据传输完成之前会被挂起，等待操作完成。这种模式被称为阻塞式I/O（Blocking I/O）。在此模式下，操作系统能够识别线程的阻塞状态，并执行上下文切换，以便调度其他可执行的线程，从而优化CPU资源的利用率。尽管如此，阻塞式I/O操作会导致发起请求的线程或进程在I/O操作完成前无法继续执行。虽然这种设计不会对整个系统的运行造成影响，但它确实会在I/O操作期间暂时阻塞发起请求的线程或进程，影响其响应性和并发处理能力。

作为对阻塞I/O的替代方案，非阻塞I/O提供了更高效的选择。与阻塞I/O类似，非阻塞I/O同样需要底层操作系统的支持，但现代操作系统普遍提供了某种形式的非阻塞I/O功能。通过非阻塞I/O，应用程序可以以异步方式发起读写请求，操作系统将负责处理这些请求，并在数据准备好时通知应用程序。

异步编程（Asynchronous Programming）是一种专门用于处理非阻塞I/O操作的编程方式。与传统的阻塞I/O不同，非阻塞I/O使得系统在发出读写请求后不会等待操作完成，而是可以同时处理其他请求。操作结果或数据会在准备好时返回，或者在需要时提供给程序。因此，非阻塞I/O是实现异步编程的核心技术，通常这两者被统称为异步I/O。

### 1.2.2 asyncio模块介绍

在Python中，异步编程泛指非阻塞的请求处理方式，即发起请求后不暂停程序执行，而是继续处理其他任务。Python支持多种异步编程技术，其中部分与并发性紧密相关。为了支持异步编程，Python3.4版本首次引入了asyncio（asynchronous I/O的缩写）模块，为异步编程提供了基础设施。随后，在Python 3.5版本中，引入了async/await语法。其中：

- asyncio模块旨在支持异步编程，并提供了底层和高级API。高级API提供了执行异步任务、处理回调、执行I/O操作等工具。而底层API则为高级API提供了支撑，包括事件循环的内部机制、传输协议和策略等。
- async/await语法的引入是为了更好地支持协程，这是asyncio模块中实现并发的核心。因为协程提供了一种轻量级的并发方式，可以让单个线程在多个任务之间高效切换，从而实现并发执行，而无需使用传统的线程或进程。

协程是一种特殊的函数，它能够在执行过程中的多个点被暂停和恢复，实现协作式的多任务处理。与传统的子程序或函数相比，协程提供了更灵活的控制流，允许在多个点进行进入、退出和恢复执行。

目前，asyncio模块是Python异步编程的常用工具，它结合async/await语法和非阻塞I/O操作，为开发者提供了一个全面的异步编程框架。那么为什么要在Python程序使用异步编程：

- 提升并发性能：通过使用协程，asyncio使得程序能够以单线程的方式高效地处理大量并发任务，避免了传统多线程编程中的复杂性和资源消耗。
- 简化异步编程：asyncio提供了一套简洁的异步编程范例，使得编写和维护异步代码变得更加容易，同时也提高了代码的可读性和可维护性。
- 优化I/O操作：asyncio支持非阻塞I/O操作，这意味着程序在等待I/O操作（如文件读写、网络通信等）时，不会阻塞主线程，从而可以同时执行其他任务，显著提高了I/O操作的效率。

## 1.3 Python并发单元的选择与比较

**线程、进程、协程**

在现代编程中，有效地处理并发是提高程序性能和响应能力的关键。Python提供了多种并发单元，包括线程、进程和协程，每种都有其特定的用途和优势。以下是对这三种并发单元的详细介绍：

1. 线程（Threads）

线程是一种并发单元，Python中由threading模块提供，并得到操作系统的支持。线程适合处理阻塞I/O任务，例如从文件、套接字和设备中进行读写操作。然而，由于全局解释器锁（GIL）的存在，Python中的线程在执行CPU密集型任务时效率不高。

1. 进程（Processes）

进程也是由操作系统支持的并发单元，Python中由multiprocessing模块提供。进程适合执行CPU密集型任务，尤其是那些不需要大量进程间通信的计算任务。与线程相比，进程可以绕过全局解释器锁，因此在处理CPU密集型任务时更为高效。

1. 协程（Coroutines）

协程是Python语言和运行时（标准解释器）提供的并发单元，Python中由asyncio模块进一步支持。相较于线程，程序中可以拥有更多的协程同时运行。协程适用于非阻塞I/O操作，如与子进程和套接字的交互。此外，虽然阻塞I/O和CPU密集型任务并非协程的直接应用场景，但可以通过在后台使用线程和进程以模拟非阻塞的方式执行这些任务。

关于线程、进程、协程的详细介绍见：[进程、线程、协程](https://blog.csdn.net/m0_48173416/article/details/143191901)。

![https://semfionetworks.com/blog/multi-threading-vs-multi-processing-programming-in-python/](https://gitlab.com/luohenyueji/article_picture_warehouse/-/raw/main/CSDN/%5Bpython%5D%20Python%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B%E5%BA%93asyncio%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8C%97/img/img2.jpg)

**在Python中使用协程的利弊**

在Python中，使用协程相比于线程和进程有以下几个主要好处：

- 轻量级：协程的创建和切换比线程和进程更高效，消耗的资源更少。
- 避免上下文切换开销：协程切换由程序控制，不依赖操作系统调度，减少了CPU时间消耗。
- 共享内存：协程在同一线程内运行，数据共享更简单，不需要锁和复杂的同步机制。
- 简洁的代码结构：协程使异步代码能够以同步的方式书写，代码更易理解和维护。
- 高并发处理：协程非常适合处理大量I/O密集型任务，能够高效利用单个线程实现并发。

当然在Python中使用协程也存在一些缺点：

- 编程复杂性：协程要求开发者理解异步编程模式，这增加了编程的复杂性，尤其是在编写、测试和调试异步代码时。
- 库支持有限：并非所有Python库都支持异步操作，这可能限制了协程在某些场景下的应用。
- 调试难度：异步代码的调试比同步代码更困难，因为传统的调试工具可能无法有效地跟踪协程的执行流程。
- 错误处理：异步代码中的错误处理比同步代码更为复杂，因为需要处理协程挂起和恢复时的状态。
- 执行机制：根据Python底层设计，协程在执行时是协作式的，一次只能运行一个协程。这种机制类似于全局解释器锁下的线程执行。

# 2 asyncio的使用

## 2.1 协程的使用

了解协程的创建和运行是学习`asyncio`库的基础，因为`asyncio`正是通过协程实现异步编程的。因此，在学习`asyncio`之前，先掌握协程的基本概念非常重要。

协程是异步编程中实现并发的核心，它是一种特殊的函数，能够在执行过程中暂停并稍后恢复。与传统的函数不同，传统函数只能在一个固定的入口和出口点运行，而协程则允许在多个地方挂起、恢复或退出。这种特性使得协程在执行时可以暂停并等待其他任务完成，比如等待其他协程的执行结果、外部资源的返回（例如网络连接或数据处理），然后再继续执行。正是因为协程具备这种暂停和恢复的能力，它们能够同时执行多个任务，而且能够精确控制任务何时暂停和何时恢复。

**协程的定义**

在Python中，协程可以通过使用`async def`关键字来定义。这种定义方式允许协程接受参数，并在执行完毕后返回一个值，类似于常规函数的行为：

```python
# 定义一个协程
async def custom_coroutine():
    # 协程体，可以包含异步操作
    pass
```

使用`async def`声明的协程被称为“协程函数”，这是一种特殊的函数，其返回值是一个协程对象。协程函数在其内部使用`await`（用于等待另一个协程完成）、`async for`（用于异步迭代）和`async with`（用于异步上下文管理器）等关键字来处理异步操作。如下所示：

```python
# 定义一个异步协程
async def custom_coroutine():
    # 等待另一个协程执行
    # await表达式将暂停当前协程的执行，并将控制权转交给被等待的协程，以便其能够执行
    await asyncio.sleep(1)
```

**协程的创建**

在定义了协程之后，可以创建具体的协程实例：

```python
# 实例化协程
coroutine_instance = custom_coroutine()
```

需要注意的是，调用协程函数本身并不会导致任何用户定义的代码被执行，其作用仅限于创建并返回一个`coroutine`对象。`coroutine`对象是Python中的一种特殊对象类型，它提供了如`send()`和`close()`等方法，用于控制协程的执行流程和生命周期管理。

可以通过创建协程实例并调用`type()`函数来报告其类型来演示这一点：

```python
import asyncio
# 定义协程
async def custom_coroutine():
    print("运行自定义协程")
    # 等待另一个协程
    await asyncio.sleep(1)

# 创建协程
coro = custom_coroutine()
# 检查协程的类型
print(type(coro))
```

代码运行结果为：

```none
<class 'coroutine'>
sys:1: RuntimeWarning: coroutine 'custom_coroutine' was never awaited
```

该警告是因为在Python中，当定义一个协程函数并调用它时，返回的是一个协程对象，而不是立即执行。这个协程对象需要通过`await`关键字或事件循环来执行。代码中的`print(type(coro))`正确地打印出了协程对象的类型。但是，由于协程没有被await，所以会有一个RuntimeWarning警告。

**协程的运行**

协程可以被定义和创建，但只有在事件循环中才能执行。事件循环是异步应用程序的核心，负责调度异步任务和回调，处理网络 I/O 操作。它还负责协调协程之间的协作和多任务处理。

事件循环的工作方式类似于一个不断运行的“调度器”，它会检查哪些任务已经准备好执行，并按顺序执行这些任务。如果某个任务需要等待，例如等待网络响应或文件读取，事件循环会暂时挂起这个任务，并把控制权交给其他可以继续执行的任务。这样，程序就可以在等待的同时，处理其他任务，从而避免了阻塞操作。

通常，通过调用 `asyncio.run()` 函数启动事件循环。该函数会启动事件循环并接收一个协程作为参数，等待协程执行完成并返回结果。代码示例如下：

```python
import asyncio

# 定义协程
async def custom_coroutine():
    print("运行自定义协程")
    # 等待另一个协程
    await asyncio.sleep(1)

# 创建协程
coro = custom_coroutine()

# 运行协程
asyncio.run(coro)

# 检查协程的类型
print(type(coro))
```

代码运行结果为：

```none
运行自定义协程
<class 'coroutine'>
```

## 2.2 asyncio任务的使用

在asyncio框架中，任务（Task）是协程的封装，它将协程交给事件循环调度执行。任务通常由协程创建，并在事件循环中运行，但它独立于协程本身。创建任务时，不需要等待其完成，可以继续执行其他操作。任务对象代表一个将在事件循环中异步执行的操作，借助任务管理，可以更方便地处理异步编程中的复杂场景。

协程是异步操作的基本单元，任务则负责管理和调度这些协程。任务不仅支持同时执行多个协程，还能处理结果、取消任务和捕获异常等。如果只关注协程，而忽视任务，就无法有效调度多个异步操作，也难以管理任务的生命周期。因此，理解任务对于掌握异步编程至关重要。

任务的生命周期可以从多个阶段来描述。首先，任务是由协程（coroutine）创建的，并被安排在事件循环（event loop）中独立执行。随着时间的推移，任务会进入运行状态。在执行过程中，任务可能会因为等待其他协程或任务完成而被挂起（suspended）。任务有可能在正常情况下完成并返回结果，或者由于某些异常而失败。如果有其他协程介入，任务也可能会被取消（canceled）。一旦任务完成，它将无法再被重新执行。因此，任务的生命周期可以总结为以下几个阶段：

1. 创建（Created）：任务被创建，但尚未开始执行。
2. 调度（Scheduled）：任务被安排到事件循环中，准备开始执行。
3. 取消（Canceled）：任务在执行之前或执行过程中被取消。
4. 运行（Running）：任务开始执行，进入活跃状态。
5. 挂起（Suspended）：任务在运行过程中被挂起，等待其他操作完成。
6. 结果（Result）：任务成功完成并返回结果。
7. 异常（Exception）：任务执行过程中遇到错误或异常，导致失败。
8. 完成（Done）：任务无论是否成功，都已结束，无法再执行。

![https://superfastpython.com/asyncio-task-life-cycle/](https://gitlab.com/luohenyueji/article_picture_warehouse/-/raw/main/CSDN/%5Bpython%5D%20Python%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B%E5%BA%93asyncio%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8C%97/img/img3.jpg)

### 2.2.1 asyncio任务创建和运行

**任务的创建**

任务是通过协程实例创建的，因此只能在协程内部创建和调度。可以使用 `asyncio.create_task()` 函数来创建任务，该函数会返回一个 `asyncio.Task` 实例：

```python
import asyncio
# 定义协程
async def custom_coroutine():
    # 等待另一个协程
    await asyncio.sleep(1)

# 创建协程
coro = custom_coroutine()

# 从协程创建任务
# name参数为设置任务的名称
task = asyncio.create_task(coro, name='task')
# 也可以用函数设置任务名称
task.set_name('MyTask')
```

此外，`asyncio.ensure_future`函数也可以用来创建和安排任务，它会确保返回一个Future或Task实例：

```python
# 创建并安排任务
task = asyncio.ensure_future(custom_coroutine())
```

当然也可以直接通过事件循环来创建任务，可以使用事件循环对象的`create_task`方法。示例如下：

```python
# 获取当前事件循环
loop = asyncio.get_event_loop()
# 创建并安排任务
task = loop.create_task(custom_coroutine())
```

**任务的运行**

在创建任务后，尽管可以使用`create_task`函数将协程安排为独立任务，但任务未必会立即执行。任务的执行依赖于事件循环的调度，它会在其他所有协程执行完成后才会开始。例如，在一个asyncio程序中，若某个协程创建并安排了任务，任务只有在该协程挂起后才有可能开始执行。具体来说，任务的执行通常会等到协程进入休眠、等待其他协程或任务时，才会被事件循环调度执行：

```python
import asyncio

# 定义一个简单的异步函数
async def my_coroutine(name):
    print(f"任务 {name} 开始执行")
    await asyncio.sleep(1)  # 模拟任务的延时
    print(f"任务 {name} 完成")

# 获取事件循环
loop = asyncio.get_event_loop()

print("任务创建之前")

# 创建任务并加入事件循环
task = loop.create_task(my_coroutine("A"))
print("任务创建之后，任务已加入事件循环")

# 运行事件循环，直到任务完成
loop.run_until_complete(task)

# 关闭事件循环
loop.close()

print("事件循环已关闭")
```

代码运行结果为：

```none
任务创建之前
任务创建之后，任务已加入事件循环
任务 A 开始执行
任务 A 完成
事件循环已关闭
```

**多任务的运行**

`gather`函数可以同时启动多个协程（任务）并发执行，同时将它们存储在一个集合中进行管理。它还支持等待所有协程执行完成，并且可以提供取消操作的功能。

以下是具体的代码示例：

```python
# 并发执行多个协程，并返回结果
# 如果协程没有返回值，则返回None
results = asyncio.gather(coro1(), coro2())
```

或者，使用展开语法：

```python
# 使用展开语法收集多个协程
asyncio.gather(*[coro1(), coro2()])
```

需要注意的是，直接传递一个协程列表是无效的：

```python
# 直接传递协程列表是不允许的
asyncio.gather([coro1(), coro2()])
```

### 2.2.2 asyncio任务状态

本节将介绍以下内容：

- 任务的完成与取消
- 获取任务结果
- 任务异常的处理
- 任务回调函数的使用

![img](https://gitlab.com/luohenyueji/article_picture_warehouse/-/raw/main/CSDN/%5Bpython%5D%20Python%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B%E5%BA%93asyncio%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8C%97/img/img4.jpg)

**任务完成与取消**

在任务创建完成后，需要重点检查两个关键状态：一是任务是否已顺利完成；二是任务是否已被正式取消。可以通过`done()`方法来确认任务是否已完成，通过 `cancelled()`方法来检查任务是否已被取消。示例代码如下：

```python
import asyncio

# 异步任务1: 打印任务开始、等待1秒并打印任务完成
async def task_completed():
    print("任务1正在执行")
    await asyncio.sleep(1)  # 模拟异步操作，暂停1秒
    print("任务1完成")

# 异步任务2: 打印任务开始、等待2秒并打印任务完成
async def task_cancelled():
    print("任务2正在执行")
    await asyncio.sleep(2)  # 模拟异步操作，暂停2秒
    print("任务2完成")

# 主异步函数
async def main():
    # 创建并启动两个异步任务
    task1 = asyncio.create_task(task_completed())  # 创建任务1
    task2 = asyncio.create_task(task_cancelled())  # 创建任务2

    # 等待task1任务完成
    await task1

    # 取消task2任务
    task2.cancel()
    
    # 异常处理: 捕获任务2被取消的异常
    try:
        await task2  # 尝试等待task2完成
    except asyncio.CancelledError:
        # 如果task2被取消
        pass

    # 检查task1是否完成
    if task1.done():
        print("任务1已完成")

    # 检查task2是否被取消
    if task2.cancelled():
        print("任务2已取消")

# 运行主异步函数
asyncio.run(main())  # 启动事件循环，执行main函数
```

代码运行结果为：

```none
任务1正在执行
任务2正在执行
任务1完成
任务1已完成
任务2已取消
```

**任务结果获取**

通过调用 `result()` 方法可以获取任务执行的结果。如果任务中包含的协程函数有返回值，则 `result()` 方法将返回该值；若协程函数未显式返回任何值，则默认返回 `None`。

若任务已被取消，在尝试调用 `result()` 方法时会触发 `CancelledError` 异常。因此，建议在调用 `result()` 方法前先检查任务是否已被取消：

```python
# 检查任务是否未被取消
if not task.cancelled():
    # 获取包装协程的返回值
    value = task.result()
else:
    # 任务已被取消
```

如果任务尚未完成，在调用 `result()` 方法时会抛出 `InvalidStateError` 异常。因此，在调用 `result()` 方法之前，最好先确认任务是否已完成：

```python
# 检查任务是否已完成
if not task.done():
    await task
# 获取包装协程的返回值
value = task.result()
```

**任务异常处理**

可以通过 `exception()` 方法获取协程未处理的异常信息。若任务执行过程中发生异常，使用该方法能够捕获并返回该异常：

```python
import asyncio

# 定义一个协程，模拟异常
async def faulty_coroutine():
    raise ValueError("协程中发生了错误。")

# 主程序
async def main():
    # 创建协程任务
    task = asyncio.create_task(faulty_coroutine())
    
    # 等待任务执行完成，捕获异常
    try:
        await task
    except Exception as e:
        # 获取任务中的异常
        exception = task.exception()
        print(f"任务异常: {exception}")

# 运行事件循环
asyncio.run(main())
```

在这个示例中，创建了一个协程`faulty_coroutine`，该协程在执行时会引发 `ValueError`异常。通过`task.exception()`方法捕获并打印该异常信息。执行结果将显示：

```none
任务异常: 协程中发生了错误。
```

**任务的回调函数**

通过`add_done_callback()`方法可以为任务指定一个完成时触发的回调函数。这个方法需要传入一个函数名，该函数将在任务完成时被调用。注意，任务完成可以发生在以下几种情况：包装的协程正常结束、返回结果、抛出未捕获的异常，或者任务被取消。以下是如何定义和注册一个完成回调函数的示例：

```python
# 定义完成回调函数
def handle(task):
    print(task)

# 为任务注册完成回调函数
task.add_done_callback(handle)
```

同样地，如果需要，可以使用`remove_done_callback()`方法来删除或取消之前注册的回调函数：

```python
# 取消注册的回调函数
task.remove_done_callback(handle)
```

但是要注意的是回调函数通常是普通的Python函数，无法进行异步操作：

```python
import asyncio

# 异步函数
async def my_coroutine():
    print("开始任务")
    await asyncio.sleep(1)
    print("任务完成")
    return "任务完成"

# 回调函数
def my_callback(task):
    print("回调函数被调用")
    result = task.result()  # 获取任务的返回结果
    print(f"任务的返回结果是: {result}")

async def main():
    # 创建任务
    task = asyncio.create_task(my_coroutine())

    # 注册回调函数
    task.add_done_callback(my_callback)

    # 等待任务完成
    await task

# 运行主函数
asyncio.run(main())
```

代码运行结果为：

```none
开始任务
任务完成
回调函数被调用
任务的返回结果是: 任务完成
```

### 2.2.3 asyncio任务获取

**当前任务获取**

可以使用 `asyncio.current_task()` 方法来获取当前正在执行的任务。这个方法会返回一个代表当前任务的 `Task` 对象。以下示例展示了如何在主协程中获取当前任务：

```python
# 从当前协程中获取当前任务
import asyncio

# 定义主协程
async def main():
    # 输出开始消息
    print('主协程已启动')
    # 获取当前任务
    current_task = asyncio.current_task()
    # 打印任务详情
    print(current_task)

# 运行主协程
asyncio.run(main())
```

上述代码打印结果包含任务的名称和正在运行的协程信息：

```none
Task pending name='Task-1' coro=<main() 
```

**所有任务获取**

可以使用 `asyncio.all_tasks()` 函数来检索asyncio程序中所有已安排和正在执行（尚未完成）的任务。以下示例首先创建了10个任务，每个任务都封装并执行相同的协程。随后，主协程捕获程序中所有已计划或正在运行的任务集合，并输出它们的详细信息：

```python
import asyncio

# 10个异步任务
async def task_coroutine(value):
    # 输出任务运行信息
    print(f'任务 {value} 开始运行')
    # 模拟异步等待，使每个任务休眠1秒
    await asyncio.sleep(1)
    
    # 输出任务运行信息
    print(f'任务 {value} 结束运行')

# 主协程定义
async def main():
    # 输出主协程启动信息
    print('主协程已启动')
    # 创建10个任务
    # 注意。任务的执行依赖于事件循环的调度，它会在其他所有协程执行完成后才会开始
    # 例如当前协程创建了任务，但是任务只有在当前协程挂起后才有可能开始执行
    started_tasks = [asyncio.create_task(task_coroutine(i), name=f'任务{i}') for i in range(10)]
    # 使得当前的协程（即 main 协程）挂起0.1秒，从而使得子任务运行
    # 如果没有这句代码，也没有之后的gather函数，子任务会在main函数将要结束时运行，此时事件循环还存在
    await asyncio.sleep(0.1)
    # 获取所有任务的集合
    all_tasks = asyncio.all_tasks()
    # 输出所有任务的详细信息
    for task in all_tasks:
        print(f'> {task.get_name()}, {task.get_coro()}')
    print("等待任务完成")
    # gather会收集传入的所有任务，并阻塞当前协程，直到所有任务都执行完毕
    # 没有gather函数，这样当前协程会直接结束，导致部分任务未能执行或未完成
    await asyncio.gather(*started_tasks)
    # gather函数类似于以下代码
    # 逐个等待每个任务完成
    # for task in started_tasks:
    #     await task  # 等待单个任务完成

# 运行异步程序
asyncio.run(main())
```

### 2.2.4 asyncio任务等待

**asyncio.wait函数**

`asyncio.wait()`函数用于等待多个 asyncio.Task 实例（即封装了协程的任务）完成。它允许配置等待策略，比如等待全部任务、第一个完成或第一个出错的任务。这些任务实际上是 asyncio.Task 类的实例，它们封装了协程，使得协程可以被调度并独立运行，并提供了查询状态和获取结果的接口。

`asyncio.wait()` 函数接收一组可等待对象，通常为 `Task` 实例，或者 `Task` 的列表、字典或集合。该函数会持续等待，直到任务集合中的某些条件得到满足，默认情况下，这些条件是所有任务都已完成。`asyncio.wait()` 返回一个包含两个集合的元组：第一个集合是所有已满足条件的任务对象，称为“完成集”（"done" set）；第二个集合是尚未满足条件的任务对象，称为“待处理集”（"pending" set）。

例如：

```python
tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
# 等待所有任务完成
done, pending = await asyncio.wait(tasks)
```

在上面的示例中，`asyncio.wait()`被加上了 `await`，原因在于从技术角度来看，`asyncio.wait()`是一个返回协程的协程函数。`await`用于暂停异步函数的执行，以便调用 `asyncio.wait`，从而等待所有任务完成。

**等待条件设置**

在`asyncio.wait()`函数中，`return_when`参数允许指定等待的条件，其默认值为`asyncio.ALL_COMPLETED`，意味着只有当所有任务都完成时，才会停止等待并返回结果。如果将`return_when`参数设置为`asyncio.FIRST_COMPLETED`，将等待直到列表中的第一个任务完成。一旦第一个任务完成并从等待集中移除，将继续执行当前代码，但其余的任务将继续执行，不会被取消：

```python
import asyncio
import random

# 模拟一个可能需要不同时间完成的异步任务
async def async_task(name, duration):
    print(f"任务 {name} 开始，预计耗时 {duration} 秒")
    await asyncio.sleep(duration)
    print(f"任务 {name} 完成")
    return f"结果 {name}"

# 主函数，用于启动和管理异步任务
async def main():
    # 创建两个任务，一个快一个慢
    fast_task = asyncio.create_task(async_task("任务1", random.randint(1, 3)), name='任务1')
    slow_task = asyncio.create_task(async_task("任务2", random.randint(4, 6)), name='任务2')

    # return_when=asyncio.FIRST_COMPLETED表示第一个任务以下代码完成后，会继续后续等待，而不用等待其余任务
    # done和pending都是集合类型（set），包含完成的任务集合和未完成的集合
    done, pending = await asyncio.wait([fast_task, slow_task], return_when=asyncio.FIRST_COMPLETED)
    
    # 处理完成的任务
    for task in done:
        # 提取结果
        result = task.result()
        print(f"{task.get_name()}的执行结果：{result}")

    print(f"已完成任务数：{len(done)}")
    
    # 等待剩余的任务完成（如果需要）
    if len(pending) >0:
        await asyncio.wait(pending)

# 运行主函数
asyncio.run(main())
```

此外，可以通过将 `return_when` 参数设置为 `FIRST_EXCEPTION` 来等待第一个因异常失败的任务。如果没有任务因异常失败，`done` 集合将包含所有已完成的任务，且 `wait()` 函数仅在所有任务完成后才会返回结果。

**任务超时**

可以通过`timeout`参数指定等待任务的最大时间（以秒为单位）。如果超时，则函数将返回一个包含当前满足条件的任务子集的元组，例如，如果等待所有任务完成，则返回的是已完成的任务子集。示例代码如下：

```python
import asyncio
import random

# 在新任务中执行的协程
async def task_coro(arg):
    # 模拟不同的执行时间
    value =  random.uniform(0, 2)  # 保证每个任务的执行时间为0到2秒
    await asyncio.sleep(value)
    print(f'> 任务 {arg} 完成，执行时间 {value:.2f} 秒')

# 主协程
async def main():
    # 创建多个任务
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    
    # 设置最大等待时间为1秒，超时后返回已完成的任务
    done, pending = await asyncio.wait(tasks, timeout=1)
    
    # 打印结果：已完成的任务和待处理的任务
    print(f'已完成的任务数量: {len(done)}')
    print(f'待处理的任务数量: {len(pending)}')
    
    # 如果超时后有任务未完成，显示它们的状态
    if pending:
        print('以下任务未在超时时间内完成：')
        for task in pending:
            print(f'- 任务 {tasks.index(task)}')

# 启动异步程序
asyncio.run(main())
```

**单个任务等待**

`asyncio.wait_for()` 函数用于等待协程或任务的完成，并提供超时控制。与 `asyncio.wait()` 不同，`wait_for()` 仅等待一个任务，并且在超时之前会检查该任务是否已完成。如果任务未能在指定的超时时间内完成，函数会抛出 `asyncio.TimeoutError` 异常。如果没有设置超时，函数将一直等待任务完成。

`wait_for()` 会返回一个协程对象，实际执行时需要通过 `await` 显式等待结果，或者将其调度为任务。如果超时，任务将被取消。`wait_for()` 接受两个参数：

1. 第一个参数是待等待的协程或任务。
2. 第二个参数是超时时间（单位为秒），可以是整数或浮点数。如果设置为 `None`，表示没有超时限制。

示例代码如下：

```python
from random import random
import asyncio

# 定义异步函数 task_coro，作为协程任务执行
async def task_coro(arg):
    # 生成一个1到2之间的随机数
    value = 1 + random()
    # 打印接收到的值
    print(f'>任务接收到 {value}')
    # 异步等待，模拟耗时操作，等待时间由随机数决定
    await asyncio.sleep(value)
    # 打印任务完成消息
    print('>任务完成')

# 定义主协程函数 main
async def main():
    # 创建协程任务并传入参数1
    task = task_coro(1)
    # 尝试执行任务并设置超时为0.2秒
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        # 超时处理：打印任务取消消息
        print('放弃等待，任务已取消')
    except Exception:
        # 捕获其他可能的异常
        pass

# 启动异步程序，运行主协程
asyncio.run(main())
```

### 2.2.5 asyncio任务保护

异步任务可通过调用 `cancel()` 方法取消。将任务包装在 `asyncio.shield()` 中可防止其被取消。`asyncio.shield()` 会将协程或可等待对象包装在一个特殊对象中，吸收所有取消请求。即便外部请求取消，任务仍会继续执行。此功能在异步编程中尤为重要，特别是当某些任务可取消，而其他关键任务需持续运行时。`asyncio.shield()`接受可等待对象并返回一个 `asyncio.Future` 对象，可直接等待该对象或传递给其他任务：

```none
# 防止任务被取消
shielded = asyncio.shield(task)
# 等待屏蔽任务
await shielded
```

返回的 `Future` 对象可以通过调用 `cancel()`方法来取消。如果内部任务仍在执行，取消请求会被视为成功。例如：

```python
# 取消屏蔽任务
was_canceled = shielded.cancel()
```

至关重要的是，向`Future`对象发出的取消请求并不会传递给其内部任务：

```python
import asyncio

async def coro():
    print("任务开始")
    await asyncio.sleep(3)
    print("任务完成")

async def main():
    # 创建异步任务
    task = asyncio.create_task(coro())
    
    # 使用shield包装任务，以创建一个不可取消的任务
    shield = asyncio.shield(task)
    
    # 尝试取消shield，但这不会影响内部的task
    shield.cancel()
    
    try:
        # 等待任务执行完成
        await task
    except asyncio.CancelledError:
        print("任务被取消")

# 启动异步事件循环
asyncio.run(main())
```

代码运行结果为：

```none
任务开始
任务完成
```

如果一个正在被屏蔽的任务被取消了，那么取消请求将会传递给`shield`对象，导致`shield`对象也被取消，并且会触发`asyncio.CancelledError` 异常。以下是代码示例：

```python
import asyncio

async def coro():
    print("任务开始")
    await asyncio.sleep(3)
    print("任务完成")

async def main():
    # 创建异步任务
    task = asyncio.create_task(coro())
    
    # 使用 shield 包装任务，以创建一个不可取消的任务
    shield = asyncio.shield(task)
    
    # 取消task
    task.cancel()
    
    try:
        # 等待任务执行完成
        await task
    except asyncio.CancelledError:
        print("任务被取消")

# 启动异步事件循环
asyncio.run(main())
```

代码运行结果为：

```none
任务被取消
```

最后，以下示例展示了如何创建、调度和保护协程任务，首先，创建一个主协程 `main()`，作为应用程序的入口点，并创建一个任务协程，确保任务不会被取消。随后，使用 `asyncio.shield()` 保护任务，将其传递给 `cancel_task()` 协程，在其中模拟`shielded`任务取消请求。主协程等待该任务并捕获 `CancelledError` 异常。任务在运行一段时间后休眠，最终，任务完成并返回结果，`shielded` 任务被标记为取消，而内部任务则正常完成：

```python
import asyncio

# 定义一个简单的异步任务，模拟处理逻辑
async def simple_task(number):
    await asyncio.sleep(1)
    return number

# 定义一个异步任务，稍后取消指定任务
async def cancel_task(task):
    await asyncio.sleep(0.2)
    was_cancelled = task.cancel()
    print(f'已取消: {was_cancelled}')

# 主协程，调度其他任务
async def main():
    coro = simple_task(1)
    task = asyncio.create_task(coro)
    shielded = asyncio.shield(task)

    # 创建取消任务的协程
    asyncio.create_task(cancel_task(shielded))
    
    try:
        result = await shielded
        print(f'>获得: {result}')
    except asyncio.CancelledError:
        print('任务已被取消')

    await asyncio.sleep(1)
    
    print(f'保护任务: {shielded}')
    print(f'任务: {task}')

# 启动主协程
asyncio.run(main())
```

### 2.2.6 asyncio中运行阻塞任务

asyncio专注于异步编程和非阻塞I/O操作。然而，异步应用中执行阻塞函数调用是不可避免的，原因包括：

- 执行CPU密集型任务，如复杂计算。
- 处理阻塞I/O任务，如文件读写。
- 调用未与asyncio集成的第三方库。阻塞调用会导致事件循环暂停，阻止其他协程运行。

`asyncio` 模块提供了两种方法来在 `asyncio` 程序中执行阻塞调用。第一种方法是使用 `asyncio.to_thread()` 函数，它是一个高级API，专为应用程序开发者设计。`asyncio.to_thread()`在单独的线程中执行并返回一个协程。这个协程可以被等待或调度作为独立任务执行。同时`asyncio.to_thread()` 会在后台创建一个 `ThreadPoolExecutor` 来执行阻塞操作，因此它适用于 I/O 密集型任务。

在以下代码中，`asyncio.to_thread`的作用是将一个阻塞的同步任务（即 `blocking_task()` 函数）封装成异步任务，并将其交给一个独立的线程池运行。这样做的目的是避免阻塞主事件循环，从而确保其他异步任务可以继续执行。具体而言，`blocking_task` 是一个同步函数，其中的 `time.sleep(2)` 会阻塞当前线程 2 秒。由于线程在这段时间内无法执行其他任务，如果在传统的 `asyncio` 环境中直接调用阻塞函数，事件循环会被暂停，无法继续调度其他任务。但是`asyncio.to_thread` 的使用确保了阻塞任务不会影响到主事件循环的执行：

```python
import asyncio
import time

# 定义一个阻塞 IO 绑定任务
def blocking_task():
    # 报告任务开始
    print('任务开始')
    # 模拟阻塞操作：休眠2秒
    time.sleep(2)  # 这里的 time.sleep 是阻塞当前线程的操作
    # 报告任务结束
    print('任务完成')

# 主协程
async def main():
    # 报告主协程正在运行并启动阻塞任务
    print('主协程正在执行阻塞任务')

    # 将阻塞任务封装成协程并通过asyncio.to_thread函数运行
    # asyncio.to_thread 会将阻塞任务分配给一个独立的线程池来执行
    coro = asyncio.to_thread(blocking_task)

    # 创建一个 asyncio 任务来执行上述协程
    # asyncio.create_task 将协程封装为 Task 对象，使其能够在后台执行
    task = asyncio.create_task(coro)

    # 主协程继续执行其他事情
    print('主协程正在做其他事情')

    # 使用 await asyncio.sleep(0) 允许任务被调度
    # 这个操作确保协程任务有机会开始执行，因为 main() 协程的执行会在此处暂停
    await asyncio.sleep(0)  # 让出控制权，确保 task 能被执行

    # 等待任务执行完成
    await task

# 运行异步程序
# asyncio.run(main()) 负责启动整个异步事件循环并执行 main() 协程
asyncio.run(main())
```

另一种方法是使用 `loop.run_in_executor()` 函数，首先通过 `asyncio.get_running_loop()` 获取当前事件循环。`loop.run_in_executor()` 函数接收一个执行器和一个要执行的函数，如果传入 `None` 作为执行器参数，则默认使用 `ThreadPoolExecutor`。该函数返回一个可等待对象，可以选择等待它，且任务会立即开始执行，因此不需要额外等待或安排返回的可等待对象来启动阻塞调用。示例如下：

```python
# 获取事件循环
loop = asyncio.get_running_loop()
# 在单独的线程中执行函数
await loop.run_in_executor(None, task)
```

或者，可以创建一个执行器并将其传递给`loop.run_in_executor()`函数，该函数将在执行器中执行异步调用。在这种情况下，调用者必须管理执行器，在调用者完成后将其关闭：

```python
# 创建进程池
with ProcessPoolExecutor as exe:
    # 获取事件循环
    loop = asyncio.get_running_loop()
    # 在单独的线程中执行函数
    await loop.run_in_executor(exe, task)
    # 进程池自动关闭...
```

## 2.3 异步编程模型

### 2.3.1 异步迭代器

迭代是Python中的基本操作，`asyncio`提供了对异步迭代器的支持。通过定义实现`__aiter__`和`__anext__`方法的对象，能够在`asyncio`程序中创建并使用异步迭代器（Asynchronous Iterators）。

**迭代器**

迭代器是实现了迭代协议的Python对象。具体而言，`__iter__()`方法返回迭代器自身，而`__next__()`方法使迭代器前进并返回下一个元素。当没有更多数据时，迭代器会引发`StopIteration`异常。可以通过内置函数`next()`逐步获取迭代器中的元素，或者使用`for`循环自动遍历迭代器：

```python
# 定义一个名为 MyIterator 的迭代器类
class MyIterator:
    # 初始化方法，接收两个参数：start 和 end，定义迭代的起始值和结束值
    def __init__(self, start, end):
        self.current = start  # 设置当前迭代的位置，初始为 start
        self.end = end        # 设置迭代的结束值

    # 定义迭代器的 __iter__ 方法，返回迭代器自身
    def __iter__(self):
        return self  # 迭代器对象自身是可迭代的

    # 定义迭代器的 __next__ 方法，用于获取下一个值
    def __next__(self):
        # 如果当前值已经达到或超过结束值，抛出 StopIteration 异常，表示迭代结束
        if self.current >= self.end:
            raise StopIteration
        self.current += 1  # 将当前值加 1
        return self.current - 1  # 返回当前值，减去 1 是因为在加 1 后，当前值已经递增过

# 创建 MyIterator 类的一个实例，从 2开始，结束值为 5
my_iter = MyIterator(2, 5)

# 逐步获取元素，调用 next(my_iter) 获取迭代器中的下一个元素
print(next(my_iter))  # 输出 2
print(next(my_iter))  # 输出 3

# 使用 for 循环遍历MyIterator类实例，这里会自动调用 __iter__ 和 __next__ 方法
# MyIterator(0, 3)创建一个新的迭代器实例，迭代的范围是从 0 到 3（不包含 3）
for number in MyIterator(0, 3):
    print(number)
```

**异步迭代器**

异步迭代器是实现了`__aiter__()`和`__anext__()`方法的Python对象。`__aiter__()`返回迭代器实例，`__anext__()`返回一个可等待对象，用于执行迭代步骤。异步迭代器只能在`asyncio`程序中使用，可以通过`async for`表达式遍历，自动调用`__anext__()`并等待其结果。与普通的`for`循环不同，`async for`适用于处理异步操作，如网络请求或文件读取。

要创建异步迭代器，只需定义实现这两个方法的类。`__anext__()`必须返回一个可等待对象，并使用`async def`定义。迭代结束时，`__anext__()`应抛出`StopAsyncIteration`异常。由于异步迭代器依赖`asyncio`事件循环，迭代过程中的每个对象都在协程中执行并等待：

```python
# 定义一个异步迭代器
class AsyncIterator():
    # 构造函数，初始化一些状态
    def __init__(self):
        self.counter = 0

    # 实现迭代器协议的 __aiter__方法
    def __aiter__(self):
        return self

    # 实现异步的 __anext__ 方法
    async def __anext__(self):
        # 如果没有更多项目，抛出StopAsyncIteration异常
        if self.counter >= 10:
            raise StopAsyncIteration
        # 增加计数器
        self.counter += 1
        # 返回当前计数器值
        return self.counter
# 创建迭代器
it = AsyncIterator()
```

通过使用`async for`表达式在循环中遍历异步迭代器，该表达式将自动等待循环的每次迭代：

```python
import asyncio
it = AsyncIterator()

async def main():
    # 遍历异步迭代器
    async for result in AsyncIterator():
        print(result)

# 启动异步任务
asyncio.run(main())
```

如果使用的是Python 3.10或更高版本，可以使用`anext`内置函数遍历迭代器的一步，就像使用`next`函数的经典迭代器一样：

```python
import asyncio
# 获取迭代器一步的等待
awaitable = anext(it)
# 执行迭代器的一步并得到结果
result = await awaitable
```

### 2.3.2 异步生成器

生成器是Python的基本组成部分，指的是包含至少一个`yield`表达式的函数。与常规函数不同，生成器函数可以在执行过程中暂停，并在后续恢复执行，这种特性与协程相似。实际上，Python中的协程是生成器的扩展。通过`asyncio`库，能够实现异步生成器，而异步生成器（Asynchronous Generators）则是基于协程中`yield`表达式的应用。

**生成器**

生成器是一个Python函数，它通过 `yield` 表达式逐步返回值。每当生成器遇到 `yield` 时，它会返回一个值并暂停执行。下一次调用生成器时，它会从暂停的位置继续执行，直到再次遇到 `yield`。虽然生成器可以通过内置的 `next()` 函数逐步执行，但通常更常见的做法是使用迭代器，如 `for` 循环或列表推导式，来遍历生成器并获取所有返回的值：

```python
# 定义一个简单的生成器函数
def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # 暂停并返回当前值
        count += 1

# 使用 next() 函数逐步执行生成器
counter = count_up_to(5)
print(next(counter))  # 输出 1
print(next(counter))  # 输出 2
print(next(counter))  # 输出 3

# 使用 for 循环遍历生成器
for num in count_up_to(5):
    print(num)  # 输出 1, 2, 3, 4, 5

# 也可以使用列表推导式将生成器的结果转为列表
numbers = [num for num in count_up_to(5)]
print(numbers)  # 输出 [1, 2, 3, 4, 5]
```

**异步生成器**

异步生成器是使用 `yield` 表达式的特殊协程，与普通生成器不同，它能在运行时暂停并等待其他协程或任务完成。异步生成器函数创建一个异步迭代器，无法通过 `next()` 遍历，而需使用 `anext()` 获取下一个值。这使得异步生成器支持 `async for` 语法，每次迭代时都会暂停，等待任务完成后继续执行。简单来说，异步生成器在每次迭代时像一个等待中的任务，`async for` 会调度并等待其结果。

异步生成器通过定义一个包含至少一个 `yield` 表达式的协程实现，且该函数需使用 `async def` 语法。由于它本质上是一个协程，每个迭代返回的是一个等待对象，这些对象在 `asyncio` 事件循环中被调度执行，可以在生成器中等待这些对象：

```python
# 定义一个异步生成器
async def async_generator():
    for i in range(10):
        # 暂停并睡眠一会儿
        await asyncio.sleep(1)
        # 向调用者产生一个值
        yield i
        
# 创建迭代器
gen = async_generator()
```

可以使用 `async for` 表达式在循环中遍历异步生成器，该表达式会自动等待每次迭代的结果：

```python
# 异步运行的入口点
import asyncio
async def main():
    # 异步迭代生成器并打印结果
    async for result in async_generator():
        print(result)
    
    # 使用列表推导式收集所有结果
    results = [item async for item in async_generator()]
    print(results)

asyncio.run(main())
```

如果使用的是 Python 3.10 或更高版本，可以使用 anext() 内置函数遍历迭代器的一步，就像使用 next() 函数的经典迭代器一样：

```python
import asyncio
# 获取生成器一步的等待值
awaitable = anext(gen)
# 执行生成器的一步并得到结果
result = await awaitable
```

### 2.3.3 异步推导式

异步推导式（Asynchronous Comprehensions）是经典推导式的异步版本，专门用于处理异步迭代和异步操作。`asyncio`支持两种类型的异步推导式，分别是`async for`推导式和`await`推导式。

**推导式**

推导式是一种通过简洁的语法构建数据集合（如列表、字典和集合）的方法。它允许在单行代码中结合 `for` 循环和条件语句，快速创建并填充数据结构。推导式通常由三部分组成：

1. 输出表达式：表示生成的元素。
2. for循环：用于遍历可迭代对象。
3. 条件表达式（可选）：用于过滤元素，仅保留符合条件的部分。

列表推导式可以通过 `for` 表达式从一个新列表中生成元素。例如：

```python
# 使用列表推导式创建列表
result = [a * 2 for a in range(100)]
```

此外，推导式还可以用于创建字典和集合。例如：

```python
# 使用推导式创建字典
result = {a: i for a, i in zip(['a', 'b', 'c'], range(3))}
# 使用推导式创建集合
result = {a for a in [1, 2, 3, 2, 3, 1, 5, 4]}
```

**async for异步推导式**

异步推导式可通过带异步迭代的`async for`创建列表、集合或字典。该表达式按需生成协程或任务，获取其结果并存入目标容器。需要注意，`async for`仅能在协程或任务中使用。异步迭代器返回可等待对象，`async for`用于遍历并获取每个对象的结果，在内部`async for`自动等待并调度协程。异步生成器实现异步迭代器方法，亦可用于异步推导式。代码示例如下：

```python
import asyncio

# 异步函数，模拟异步操作
async def get_data():
    await asyncio.sleep(1)  # 模拟异步等待
    return [1, 2, 3, 4, 5]

# 异步推导式创建列表
async def async_list_comprehension():
    async_data = await get_data()
    async_list = [x * 2 for x in async_data]
    return async_list

# 异步推导式创建集合
async def async_set_comprehension():
    async_data = await get_data()
    async_set = {x * 2 for x in async_data}
    return async_set

# 异步推导式创建字典
async def async_dict_comprehension():
    async_data = await get_data()
    async_dict = {x: x * 2 for x in async_data}
    return async_dict

# 运行异步推导式
async def main():
    list_result = await async_list_comprehension()
    set_result = await async_set_comprehension()
    dict_result = await async_dict_comprehension()
    
    print("Async List:", list_result)
    print("Async Set:", set_result)
    print("Async Dict:", dict_result)

# 启动事件循环
asyncio.run(main())
```

**await异步推导式**

`await` 表达式不仅适用于常规异步操作，还可用于列表、集合或字典推导式，称为 await 推导。无论在异步还是同步代码中，建议统一使用 await 推导或列表推导。与异步推导式类似，await 推导仅能在异步协程或任务中使用。该机制通过挂起并等待一系列可等待对象，构建数据结构（如列表）。在当前协程中，这些可等待对象按顺序执行：

```python
import asyncio
async def fetch_data(item):
    # 模拟异步数据获取操作
    await asyncio.sleep(1)  # 模拟异步等待
    return f"Data for {item}"

async def main():
    # 创建一个包含可等待对象的列表
    awaitables = [fetch_data(item) for item in range(5)]
    
    # 使用 await 推导式构建列表
    results = [await x for x in awaitables]
    
    # 打印结果
    print(results)

# 运行主函数
asyncio.run(main())
```

### 2.3.4 异步上下文管理器

上下文管理器是Python中的一种结构，它提供了类似`try-finally`的环境，具有统一的接口和简洁的语法，通常通过`with`语句来使用。上下文管理器常用于资源管理，确保资源在使用后能够被正确关闭或释放，无论使用过程是否成功，或是否因异常而导致失败。`asyncio`库支持开发异步上下文管理器。在`asyncio`程序中，异步上下文管理器（asynchronous ContextManagers）可以通过定义一个实现了`__aenter__()`和`__aexit__()`方法的协程对象来创建和使用。

**上下文管理器**

上下文管理器是 Python 中定义了 `__enter__` 和 `__exit__` 方法的对象，它们分别负责在 `with` 语句块开始和结束时执行特定的操作。这一机制使得在进入和退出特定代码块时，能够自动管理资源的生命周期，如文件、套接字或线程池的打开与关闭。通过上下文管理器，可以有效地管理资源，提升代码的安全性与可读性。

通过 `with` 语句使用上下文管理器，可在代码块执行前后自动完成资源的准备与清理工作。上下文管理器对象通常在 `with` 语句中创建，并自动触发 `__enter__` 方法。无论代码块是正常结束还是因异常退出，`__exit__` 方法都会被自动调用。

例如：

```python
# 使用上下文管理器
with ContextManager() as manager:
    # 在此处执行代码块
# 自动管理资源关闭
# 这与 try-finally 结构类似
```

或者，也可以手动创建对象并调用这些方法：

```python
# 创建对象
manager = ContextManager()
try:
    manager.__enter__()
    # 执行代码块
finally:
    manager.__exit__()
```

**异步上下文管理器**

异步上下文管理器指的是能够在其 `__aenter__` 和 `__aexit__` 方法中挂起执行的上下文管理器。这两个方法被定义为协程，并由调用者进行等待。通过 `async with` 表达式，可以实现这一功能。因此，异步上下文管理器通常用于asyncio程序中，尤其是在协程调用时。`async with` 表达式是对传统 `with` 表达式的扩展，专门用于异步上下文管理器，允许在协程中进行异步操作，其使用方式与同步的 `with` 表达式相似，但能够处理异步任务。下面是一个定义异步上下文管理器的例子：

```python
import asyncio
# 定义异步上下文管理器
class AsyncContextManager:
    # 进入异步上下文管理器
    async def __aenter__(self):
        # 报告消息
        print('> entering the context manager')
        # 模拟异步操作，暂时阻塞
        await asyncio.sleep(0.5)

    # 退出异步上下文管理器
    async def __aexit__(self, exc_type, exc, tb):
        # 报告消息
        print('> exiting the context manager')
        # 模拟异步操作，暂时阻塞
        await asyncio.sleep(0.5)
```

在使用异步上下文管理器时，通过 `async with` 表达式来调用它。这不仅会自动等待进入和退出协程，还会确保在执行过程中暂停当前协程，直到相关的异步操作完成：

```python
# 使用异步上下文管理器
async with AsyncContextManager() as manager:
    # 在此块中执行一些异步任务
    # ...
```

以下示例展示了在 asyncio 程序中异步上下文管理器的常见使用模式，首先会创建 `main()` 协程，并将其作为 asyncio 程序的入口点。`main()` 协程执行时，创建了一个 `AsyncContextManager`类的实例，并在 `async with` 表达式中使用它：

```python
import asyncio

# 定义异步上下文管理器
class AsyncContextManager:
    # 进入异步上下文管理器
    async def __aenter__(self):
        # 报告消息
        print('>进入上下文管理器')
        # 暂停一段时间
        await asyncio.sleep(0.5)

    # 退出异步上下文管理器
    async def __aexit__(self, exc_type, exc, tb):
        # 报告消息
        print('>退出上下文管理器')
        # 暂停一段时间
        await asyncio.sleep(0.5)

# 定义一个简单的协程
async def custom_coroutine():
    # 创建并使用异步上下文管理器
    async with AsyncContextManager() as manager:
        # 输出当前状态
        print(f'在上下文管理器内部')

# 启动异步程序
asyncio.run(custom_coroutine())
```

代码运行结果为：

```none
>进入上下文管理器
在上下文管理器内部
>退出上下文管理器
```

## 2.4 asyncio中的非阻塞流

### 2.4.1 非阻塞流介绍

`asyncio`的一个重要特点是能够在进行网络操作时避免阻塞，这意味着在等待数据的过程中，程序仍然可以继续执行其他任务。这一功能通过“流”（streams）来实现，流就像一个管道，用于收发数据。借助流，数据的发送和接收变得更加简便，无需依赖复杂的回调函数或底层实现细节。

具体来说，`asyncio`中的`asyncio streams`支持通过网络连接创建“写”流和“读”流。在这些流中，可以执行数据写入和读取操作，且在等待期间程序不会被某个操作卡住。操作完成后，网络连接即可关闭。尽管在使用流功能时需要自行处理一些网络协议的细节，这种方式仍然能够支持许多常见的网络协议，例如：

- 与网站服务器通信的HTTP或HTTPS协议。
- 用于发送电子邮件的SMTP协议。
- 用于文件传输的FTP协议。

流不仅可以用于创建服务器并处理标准协议的请求，还能帮助开发者定制协议，以满足特定应用需求。接下来，将介绍如何使用异步流：

**打开连接**

可以使用 `asyncio.open_connection()` 函数打开 asyncio TCP 客户端套接字连接，建立网络连接并返回一对（reader、writer）对象。这些返回的对象是 `StreamReader` 和 `StreamWriter` 类的实例，用于与套接字交互。该函数是一个必须等待的协程，一旦套接字连接打开便返回。

例如：

```python
# 打开一个连接
reader, writer = await asyncio.open_connection(...)
```

`asyncio.open_connection()` 函数需要许多参数来配置套接字连接，其中两个必需的参数是主机和端口：

- 主机是一个字符串，指定要连接的服务器，例如域名或 IP 地址。
- 端口是套接字端口号，例如HTTP服务器为80，HTTPS 服务器为 443，SMTP为25 等。

例如，打开与 HTTP 服务器的连接：

```python
# 打开与 http 服务器的连接
reader, writer = await asyncio.open_connection('www.baidu.com', 80)
```

如果需要加密套接字连接（如 HTTPS），可以通过设置 `ssl=True` 实现 SSL 协议支持：

```python
# 打开与 https 服务器的连接
reader, writer = await asyncio.open_connection('www.baidu.com', 443, ssl=True)
```

**启动侦听服务**

要启动一个异步的TCP服务器，可以使用`asyncio.start_server()`函数。这个函数会创建一个服务器，它会在指定的地址和端口上监听来自客户端的连接请求。这个函数是一个需要等待的协程，当调用时，它会返回一个`asyncio.Server`对象，代表正在运行的服务器。

下面是如何使用这个函数的一个示例：

```python
# 启动一个 TCP 服务器
server = await asyncio.start_server(...)
```

这个函数需要三个参数：一个处理连接的函数、服务器的地址和端口号。处理连接的函数是一个用户自定义的函数，每当有客户端连接到服务器时，这个函数就会被调用。这个函数会接收一对对象作为参数，这两个对象分别用于从客户端读取数据（`StreamReader`）和向客户端发送数据（`StreamWriter`）。

**地址**是指客户端用来连接服务器的域名或IP地址，**端口号**则是服务器用来接收连接请求的网络端口，不同的服务通常会使用不同的端口，比如FTP服务常用端口21，而HTTP服务常用端口80。

下面是一个具体的使用示例：

```python
# 定义一个处理客户端连接的函数
async def handler(reader, writer):
    # 在这里添加处理客户端请求的逻辑
    pass

# 使用指定的处理器、地址和端口号启动服务器
server = await asyncio.start_server(handler, '127.0.0.1', 80)
```

在这个例子中，`handler`函数将负责处理每个客户端的连接，`'127.0.0.1'`是本地回环地址，意味着服务器将只在本地计算机上可用，而`80`是HTTP服务的标准端口号。

**使用StreamWriter写入数据**

数据可以通过`asyncio.StreamWriter`写入套接字，套接字是计算机之间通过网络传输数据的通信端点。`StreamWriter`提供API将字节数据写入套接字连接的I/O流，数据会尝试立即发送到目标设备，若无法立即发送，则存储在缓冲区。写入后，最好使用`drain`方法清空缓冲区：

```python
# 写入字节数据
writer.write(byte_data)
# 等待数据传输
await writer.drain()
```

**使用StreamReader读取数据**

数据可以通过`asyncio.StreamReader`从套接字中读取。读取的数据是字节格式，因此在使用之前可能需要进行编码。所有读取操作都是必须等待的协程。可以使用`read()`方法读取任意数量的字节，该方法会一直读取，直到文件末尾（EOF）：

```python
# 读取字节数据
byte_data = await reader.read()
```

也可以通过`n`参数指定要读取的字节数：

```python
# 读取指定字节数的数据
byte_data = await reader.read(n=100)
```

使用`readline`方法可以读取单行数据，直到遇到新行字符`\n`或文件末尾（EOF），返回的是字节数据：

```python
# 读取一行数据
byte_line = await reader.readline()
```

此外，`readexactly()`方法用于读取确切数量的字节，如果读取的字节数不足，则会引发异常。而`readuntil()`方法会读取字节数据，直到遇到指定的字节字符为止。

**关闭连接**

可以通过`asyncio.StreamWriter`来关闭套接字。调用`close()`方法即可关闭套接字，该方法不会阻塞：

```python
#关闭套接字
writer.close()
```

尽管`close()`方法不会阻塞，但可以通过`wait_close()`方法等待套接字完全关闭后再继续操作：

```python
#关闭套接字
writer.close()
#等待套接字关闭
awaitwriter.wait_closed()
```

也可以通过`is_closing()`方法检查套接字是否已经关闭或正在关闭过程中：

```python
#检查套接字是否已关闭或正在关闭
ifwriter.is_closing():
#...
```

### 2.4.2 使用asyncio检查HTTP状态

本节介绍如何使用 `asyncio` 模块通过打开流并进行HTTP请求和响应的读写操作，整个过程通常包括以下四个步骤：

1. 打开连接
2. 发送请求
3. 读取响应
4. 关闭连接

专业的异步HTTP框架可以参考使用：[aiohttp](https://github.com/aio-libs/aiohttp)。

**打开链接**

使用 `asyncio.open_connection()` 函数打开连接。该函数接受主机名和端口号作为参数，并返回一个 `StreamReader` 和 `StreamWriter`，用于通过套接字进行数据的读写。这些功能通常用于在端口 80 上打开 HTTP 连接。

**发送HTTP请求**

在打开HTTSP连接后，可以向`StreamWriter`写入查询以发出 HTTP 请求。以HTTP版本1.1 请求为例，HTTP请求的格式为纯文本，可以请求根路径“/”，其示例如下：

```none
GET / HTTP/1.1
Host: www.google.com
```

HTTP协议请求的具体介绍见：[HTTP协议请求/响应格式详解](https://www.cnblogs.com/binbingg/p/18389166)。需要注意的是，每行末尾必须包含回车符和换行符（\r\n），且请求的末尾需有一个空行。若作为 Python 字符串表示，格式如下所示：

```none
'GET / HTTP/1.1\r\n'
'Host: www.google.com\r\n'
'\r\n'
```

在写入 `StreamWriter` 之前，必须将该字符串编码为字节。可以通过调用 `encode()` 方法实现字符串编码，默认的“utf-8”编码通常适用。例如：

```python
# 将字符串编码为字节
byte_data = string.encode()
```

接着，可以使用 `StreamWriter` 的 `write()` 方法将字节数据写入套接字。例如：

```python
# 将查询写入套接字
# 等待套接字准备好
await writer.drain()
```

**读取HTTP响应**

发出HTTP请求后，可以读取响应。此操作可通过套接字的`StreamReader`实现。使用`read()`方法可一次读取一大块字节，或者使用`readline()`方法逐行读取字节。由于基于文本的HTTP协议通常每次发送一行HTML数据，因此`readline()`方法更加便捷。需要注意的是，`readline()`是一个协程，调用时需要等待其执行完成。示例如下：

```python
#读取一行响应
line_bytes=awaitreader.readline()
```

HTTP/1.1响应由标头和正文两部分组成，二者通过空行分隔。标头部分包含关于请求是否成功以及即将发送的文件类型的信息，正文则包含文件内容，如HTML网页。HTTP标头的第一行通常表示请求页面的HTTP状态。每一行数据需要从字节解码为字符串，通常使用`decode()`方法，默认编码为"utf_8"。示例如下：

```python
#将字节解码为字符串
line_data=line_bytes.decode()
```

**关闭HTTP连接**

可以通过调用`close()`方法关闭`StreamWriter`，从而关闭套接字连接。例如：

```python
#关闭连接
writer.close()
```

此操作不会阻塞，并且可能不会立即关闭套接字。

### 2.4.3 asyncio中的流使用示例

本节介绍了一个用于检查网站状态的示例，代码实现了一个异步HTTP状态码获取工具。通过结合asyncio和urlsplit模块，该工具能够并发请求多个URL，并获取这些URL的HTTP状态行（例如 HTTP/1.1 200 OK）。代码流程如下：

1. **解析URL**：使用 `urlsplit(url)` 解析 URL，提取协议、主机名和路径等信息。
2. **建立连接**：根据协议选择相应端口（80 或 443），并建立异步网络连接。
3. **发送HTTP请求**：构建并发送简单的HTTP请求报文。
4. **读取响应**：异步读取 HTTP 响应的状态行并返回。
5. **处理异常**：若请求失败，捕获异常并输出错误信息，返回 None。
6. **并发执行任务**：通过 `asyncio.gather()` 实现并发执行所有 URL 请求，等待任务完成并返回结果。
7. **输出结果**：输出每个URL的HTTP状态行或错误信息。

![img](https://gitlab.com/luohenyueji/article_picture_warehouse/-/raw/main/CSDN/%5Bpython%5D%20Python%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B%E5%BA%93asyncio%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8C%97/img/img5.jpg)

示例代码如下：

```python
import asyncio
from urllib.parse import urlsplit  # 导入 urlsplit 函数，用于解析 URL

# 定义一个异步函数，用于获取指定 URL 的 HTTP/S 状态
async def get_status(url):
    # 使用 urlsplit 解析 URL，将其分解为各个部分（例如：scheme, hostname, path）
    url_parsed = urlsplit(url)
    
    try:
        # 根据 URL 的 scheme（协议）判断是 http 还是 https，选择相应的端口（80 或 443）
        if url_parsed.scheme == 'https':
            # 如果是 https 协议，连接到 443 端口，并启用 SSL 加密
            reader, writer = await asyncio.open_connection(url_parsed.hostname, 443, ssl=True)
        else:
            # 如果是 http 协议，连接到 80 端口
            reader, writer = await asyncio.open_connection(url_parsed.hostname, 80)
        
        # 构建 HTTP 请求报文：请求目标是 URL 的 path 部分，使用 HTTP/1.1 协议
        query = f'GET {url_parsed.path} HTTP/1.1\r\nHost: {url_parsed.hostname}\r\n\r\n'
        
        # 将请求报文写入连接，并使用 StreamWriter 将编码字节写入套接字。
        writer.write(query.encode())
        # 等待数据写入完成
        await writer.drain()
        
        # 从服务器读取一行响应数据（HTTP 状态行）
        response = await reader.readline()
        # 解码响应并去除多余的空白字符
        status = response.decode().strip()
        
        # 返回 HTTP 状态行（例如："HTTP/1.1 200 OK"）
        return status
    except Exception as e:
        # 如果请求过程中发生任何异常，捕获并输出错误信息
        print(f"Error fetching {url}: {e}")
        # 如果发生错误，返回 None
        return None
    finally:
        # 确保连接关闭
        writer.close()
        await writer.wait_closed()  # 等待连接完全关闭
        reader.feed_eof()  # 通知 reader 没有更多数据会到来

# 主协程，执行多个 URL 状态获取任务
async def main():
    # 定义一个包含多个 URL 的列表，表示我们需要检查的目标网站
    sites = [
        'https://www.baidu.com/',
        'https://www.bilibili.com/',
        'https://www.weibo.com/',
        'https://www.douyin.com/',
        'https://www.zhihu.com/',
        'https://www.taobao.com/',
        'https://www.sohu.com/',
        'https://www.tmall.com/',
        'https://www.xinhuanet.com/',
        'https://www.163.com/'
    ]
    
    # 为每个 URL 创建一个获取状态的异步任务
    tasks = [get_status(url) for url in sites]
    
    # 使用 asyncio.gather 并发执行所有任务，返回所有任务的结果（包括异常）
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # 遍历 URL 和对应的响应状态，输出结果
    for url, status in zip(sites, results):
        # 如果状态不为空，表示请求成功，输出 URL 和 HTTP 状态
        if status is not None:
            print(f'{url:30}:\t{status}')
        else:
            # 如果状态为 None，表示请求失败，输出错误信息
            print(f'{url:30}:\tError')

# 运行主异步程序
asyncio.run(main())
```

# 3 参考

- [asyncio — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [Python Asyncio: The Complete Guide](https://superfastpython.com/python-asyncio/)
- [深度解密 asyncio](https://www.cnblogs.com/traditional/tag/深度解密 asyncio/)
- [进程、线程、协程](https://blog.csdn.net/m0_48173416/article/details/143191901)
- [aiohttp](https://github.com/aio-libs/aiohttp)
- [HTTP协议请求/响应格式详解](https://www.cnblogs.com/binbingg/p/18389166)



# 75. pdb python调试器

Debug功能对于developer是非常重要的，[python](http://lib.csdn.net/base/python)提供了相应的模块pdb让你可以在用文本编辑器写脚本的情况下进行debug. pdb是python debugger的简称。

常用的一些命令如下：

 

| 命令          | 用途                       |
| ------------- | -------------------------- |
| break 或 b    | 设置断点                   |
| continue 或 c | 继续执行程序               |
| list 或 l     | 查看当前行的代码段         |
| step 或 s     | 进入函数                   |
| return 或 r   | 执行代码直到从当前函数返回 |
| exit 或 q     | 中止并退出                 |
| next 或 n     | 执行下一行                 |
| pp            | 打印变量的值               |
| help          | 帮助                       |

## 调试方法对比

| 方法        | 适用场景         | 优势                     | 局限               |
| :---------- | :--------------- | :----------------------- | :----------------- |
| `pdb`       | 命令行环境调试   | 无需额外依赖，灵活控制   | 学习曲线较陡       |
| IDE工具     | 复杂项目调试     | 图形化界面，操作直观     | 依赖特定开发环境   |
| `PySnooper` | 快速定位函数问题 | 自动记录执行过程         | 仅适用于函数级调试 |
| `logging`   | 记录程序运行状态 | 持久化日志，便于问题追溯 | 需要预先设计日志点 |

# 76 concurrent

## **1.1 Executor对象**

class concurrent.futures.Executor

Executor是一个抽象类，它提供了异步执行调用的方法。它不能直接使用，但可以通过它的两个子类ThreadPoolExecutor或者ProcessPoolExecutor进行调用。

### **1.1.1 Executor.submit(fn, \*args, \**kwargs)**

fn：需要异步执行的函数

*args, **kwargs：fn参数

### **1.1.2 Executor.map(func, \*iterables, timeout=None)**

相当于map(func, *iterables)，但是func是异步执行。timeout的值可以是int或float，如果操作超时，会返回raisesTimeoutError；如果不指定timeout参数，则不设置超时间。

func：需要异步执行的函数

*iterables：可迭代对象，如列表等。每一次func执行，都会从iterables中取参数。

timeout：设置每次异步操作的超时时间

### 1.1.3 Executor.shutdown(wait=True)

释放系统资源,在Executor.submit()或 Executor.map()等异步操作后调用。**使用with语句可以避免显式调用此方法**。

## **1.3 ThreadPoolExecutor对象**

ThreadPoolExecutor类是Executor子类，使用线程池执行异步调用.

**class concurrent.futures.ThreadPoolExecutor(max_workers)**

**使用max_workers数目的线程池执行异步调用**

示例

```
def curr_demo1():
    from concurrent import futures
 
    def test(num):
        import time
        return time.ctime(),num
    
    with futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(test,1)
        print(future.result())

def curr_demo2():
    from concurrent import futures
 
    def test(num):
        import time
        return time.ctime(),num
    data = [100,200,300,400,500]
    with futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.map(test,data)
        print(list(future))


if __name__ =='__main__':
    # curr_demo1()
    curr_demo2()
```

## **2. ProcessPoolExecutor对象**

ThreadPoolExecutor类是Executor子类，使用进程池执行异步调用.

**class concurrent.futures.ProcessPoolExecutor(max_workers=None)**

**使用max_workers数目的进程池执行异步调用，如果max_workers为None则使用机器的处理器数目（如4核机器max_worker配置为None时，则使用4个进程进行异步并发）。**

示例：

```
from concurrent import futures
 
def test(num):
    import time
    return time.ctime(),num
 
def muti_exec(m,n):
    #m 并发次数
    #n 运行次数
 
    with futures.ProcessPoolExecutor(max_workers=m) as executor: #多进程
    #with futures.ThreadPoolExecutor(max_workers=m) as executor: #多线程
        executor_dict=dict((executor.submit(test,times), times) for times in range(m*n))
 
    for future in futures.as_completed(executor_dict):
        times = executor_dict[future]
        if future.exception() is not None:
            print('%r generated an exception: %s' % (times,future.exception()))
        else:
            print('RunTimes:%d,Res:%s'% (times, future.result()))
 
if __name__ == '__main__':
    muti_exec(5,1)
 
```

#### concurrent.futures下的多进程+多线程使用

这段多进程+多线程的的模式用来扫5000以内的端口量那速度是又快又准。大概1-3秒就可以出结果。配置是4进程+20000线程。

```
import socket
import concurrent.futures

# 存活探测
def alive_scan(ip):
    port_list = [22, 23, 53, 80, 443, 3389, 10022]
    port_len = len(port_list)
    num = 0
    for port in port_list:
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, port))
            sock.close()
            return True
        except socket.error:
            num += 1
            if num == port_len:
                return False
            else:
                continue

# 全端口探测
# 利用socket tcp进行探测端口存活
def all_port_scan(ip,port,live_port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock_https = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip, port))
        sock_https.connect((ip,port))
        sock.close()
        live_port.append(port)
        return live_port
    except socket.error as error:
        # print(error)
        # print(port)
        return 1

# 线程调度模块
def threadMode(ip):
    thread_list = []
    live_port = []
    num = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=20000) as executor:
        print("目标:{},端口探测中".format(ip))
		# 这里选择探测端口的范围，这里也可以改成列表形式，自定义扫描端口。当然也可以改成(1,65536)进行全端口探测，只是发包太大，结果失真。
        for port in range(1,6000):
            # num+=1
            # if num in [5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000]:
            #     time.sleep(3)
            thread_task = executor.submit(all_port_scan,ip,port,live_port)
            thread_list.append(thread_task)
        for res in concurrent.futures.as_completed(thread_list):
            result = res.result()
            if result != 0 and result != 1:
                # 返回存活端口列表
                return result
            else:
                return 1

# 进程，线程之间的调度逻辑中心模块
def power_control_mode(ip_list):
    process_list = []
	# 这里通过concurrent.futures创建四个进程，每个进程在分配到各自需要探测的IP后后会传入多线程模块，启动多线程~
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as process_executor:
        for ip in ip_list:
            process_task = process_executor.submit(threadMode,ip)
            process_list.append(process_task)
        for res in concurrent.futures.as_completed(process_list):
            port_live = res.result()
            if port_live != 1:
                print("存活端口列表")
                print(port_live)
            else:
                pass


if __name__ == "__main__":
    iplist = ["1.1.1.1"]
    live_ip = []
    for i in iplist:
        status = alive_scan(i)
        print("目标:{}:{}".format(i,status))
        live_ip.append(i)
        if status:
            power_control_mode(live_ip)
```



## **3. 附录：Python GIL相关**

要理解GIL的含义，我们需要从Python的基础讲起。像C++这样的语言是编译型语言，所谓编译型语言，是指程序输入到编译器，编译器再根据语言的语 法进行解析，然后翻译成语言独立的中间表示，最终链接成具有高度优化的机器码的可执行程序。编译器之所以可以深层次的对代码进行优化，是因为它可以看到整 个程序（或者一大块独立的部分）。这使得它可以对不同的语言指令之间的交互进行推理，从而给出更有效的优化手段。

与此相反，Python是解释型语言。程序被输入到解释器来运行。解释器在程序执行之前对其并不了解；它所知道的只是Python的规则，以及在执行过程 中怎样去动态的应用这些规则。它也有一些优化，但是这基本上只是另一个级别的优化。由于解释器没法很好的对程序进行推导，Python的大部分优化其实是 解释器自身的优化。

现在我们来看一下问题的症结所在。要想利用多核系统，Python必须支持多线程运行。作为解释型语言，Python的解释器必须做到既安全又高效。我们都知道多线程编程会遇到的问题，解释器要留意的是避免在不同的线程操作内部共享的数据，同时它还要保证在管理用户线程时保证总是有最大化的计算资源。

那么，不同线程同时访问时，数据的保护机制是怎样的呢？答案是解释器全局锁。从名字上看能告诉我们很多东西，很显然，这是一个加在解释器上的全局（从解释器的角度看）锁（从互斥或者类似角度看）。这种方式当然很安全，但是它有一层隐含的意思（Python初学者需要了解这个）：**对于任何Python程序，不管有多少的处理器，任何时候都总是只有一个线程在执行。**

”为什么我全新的多线程Python程序运行得比其只有一个线程的时候还要慢？“许多人在问这个问题时还是非常犯晕的，因为显然一个具有两个线程的程序要比其只有一个线程时要快（假设该程序确实是可并行的）。事实上，这个问题被问得如此频繁以至于Python的专家们精心制作了一个标准答案：”**不要使用多线程，请使用多进程**”。

所以，对于计算密集型的，我还是建议不要使用python的多线程而是使用多进程方式，而对于IO密集型的，还是劝你使用多进程方式，因为使用多线程方式出了问题，最后都不知道问题出在了哪里，这是多么让人沮丧的一件事情！

**建议使用多进程并发而不是多线程并发！**

[回到目录](https://www.cnblogs.com/lovesoo/p/7741576.html#_labelTop)

## **4. 参考文档**

http://pythonhosted.org/futures/

# 77 io

### 参考网址：https://www.cnblogs.com/liugp/p/17110544.html （传统IO)

### 参考网址2：https://realpython.com/ref/stdlib/io/

### 示例程序

```
def stringio_demo():
    import io
    text_data = "This is a simple text file with some words to remove."
    words_to_remove = {"simple", "some"}
    stream = io.StringIO(text_data)
    filtered_txt = " ".join(
        word for word in stream.read().split() if word not in words_to_remove
    )
    print(filtered_txt)
    with open("filtered_text.txt", mode="w", encoding="utf-8") as file:
        file.write(filtered_txt)
    print("file content:")    
    # read the conent:
    with open("filtered_text.txt", mode="r", encoding="utf-8") as file:
        print(file.read())

def bytesio_demo():
    import io
    bytes_data = b"This is a simple text file with some words to remove."
    words_to_remove = {b"simple", b"some"}
    stream = io.BytesIO(bytes_data)
    filtered_tyes = b" ".join(
        word for word in stream.read().split() if word not in words_to_remove
    )
    print(filtered_tyes)
    with open("filtered.txt", mode="wb") as file:
        file.write(filtered_tyes)
    print("file content:")    
    # read the conent:
    with open("filtered.txt", mode="rb") as file:
        print(file.read())

def io_bufferedreader_demo():
    import io
    with open("filtered.txt",'rb') as f:
        fi = io.FileIO(f.fileno())
        br = io.BufferedReader(fi)
        print(br.read())

def io_bufferedwriter_demo():
    import io

    # 1. Open a file in binary mode with buffering disabled (raw stream)
    # 'wb' = write binary; buffering=0 makes it a FileIO object
    with open("io_writer.txt", "wb", buffering=0) as raw_file:
        
        # 2. Wrap it in a BufferedWriter with a custom buffer size (e.g., 8KB)
        with io.BufferedWriter(raw_file, buffer_size=8192) as writer:
            
            # 3. Write bytes to the buffer
            # Note: BufferedWriter only accepts bytes, not strings
            writer.write(b"Hello, this is buffered data.")
            
            # 4. Flush to ensure the buffer is written to the underlying file
            writer.flush() 

    print("File written successfully.")

if __name__ == '__main__':
    # stringio_demo()
    # bytesio_demo()
    # io_bufferedreader_demo()
    io_bufferedwriter_demo()
```



# 78. dataclasses

## [Python数据类的使用](https://www.cnblogs.com/luohenyueji/p/19269848)

在Python编程中，类定义是组织数据与封装逻辑的核心范式。然而，当需要创建仅用于数据存储的简单类时，开发者往往需编写大量重复机械的样板代码。例如用于属性初始化的`__init__`方法、支持对象信息友好展示的`__repr__`方法、实现对象相等性比较的`__eq__`方法等。这类代码不仅耗费开发精力，还容易因细节疏忽引入潜在错误，导致代码可读性与维护性下降。

为解决这一行业痛点，Python 3.7引入了`dataclasses`模块，其提供的`@dataclass`装饰器堪称数据类开发的高效编程利器。该装饰器能够自动生成上述常用魔术方法，让开发者无需关注冗余的底层实现，仅需聚焦核心属性定义，即可快速构建出功能完备、易用性高的数据类。

# 1 基础使用

## 1.1 基础方法

传统方式下，定义一个简单的数据类需要手动编写大量样板代码：

```python
class Person:
    def __init__(self, name: str, age: int, email: str = "unknown@example.com"):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return (self.name == other.name and 
                self.age == other.age and 
                self.email == other.email)

# 使用示例
p1 = Person("Alice", 25)
p2 = Person("Bob", 30, "bob@example.com")

print(p1)
print(p1 == Person("Alice", 25))
```

借助`@dataclass`装饰器，我们可以用极少的代码实现相同功能：

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown@example.com"  # 默认值

# 使用示例
p1 = Person("Alice", 25)
p2 = Person("Bob", 30, "bob@example.com")

print(p1)
print(p1 == Person("Alice", 25))
```

`@dataclass`默认会为我们生成以下方法：

- `__init__`：初始化方法，根据定义的字段创建实例；
- `__repr__`： 提供友好的字符串表示，便于调试和日志记录；
- `__eq__`： 基于字段值的相等性比较；
- `__hash__`： 默认情况下，如果所有字段都是不可变类型，则生成哈希方法（可通过`unsafe_hash`参数控制）。

还可以在数据类中添加自定义方法和`@property`计算属性，兼顾数据存储与简单业务逻辑：

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Person:
    name: str
    age: int 
    email: str = "unknown@example.com"  # 默认值
    
    # 自定义方法：打招呼
    def greet(self) -> str:
        """返回一个个性化的问候语"""
        return f"Hello, my name is {self.name} and I'm {self.age} years old!"
    
    # 自定义方法：检查是否成年
    def is_adult(self) -> bool:
        """判断是否达到成年年龄（18岁）"""
        return self.age >= 18
    
    # @property计算属性：出生年份（基于当前年龄推算）
    @property
    def birth_year(self) -> int:
        """根据当前年龄和年份，计算出生年份"""
        current_year = datetime.now().year
        return current_year - self.age

# 使用示例
p1 = Person("Alice", 25)
p2 = Person("Bob", 17, "bob@example.com")

# 原有功能保持不变
print(p1)
print(p1 == Person("Alice", 25))

# 调用自定义方法
print(p1.greet())          # 输出: Hello, my name is Alice and I'm 25 years old!
print(f"Alice is adult? {p1.is_adult()}")  # 输出: Alice is adult? True
print(f"Bob is adult? {p2.is_adult()}")    # 输出: Bob is adult? False

# 访问计算属性（像访问普通属性一样）
print(f"Alice was born in {p1.birth_year}")  
```

## 1.2 进阶使用

`@dataclass`的强大之处不仅在于简化基础代码，更在于支持复杂场景的定制化开发。借助它提供的配置函数或参数设定，我们能解决可变类型默认值、字段定制化这类问题，甚至结合自定义方法落地业务逻辑。本节内容将针对这些核心能力展开具体解析，若需进一步的延展学习，可参考：[Data Classes: @dataclass Decorator](https://www.krython.com/tutorial/python/data-classes-dataclass-decorator)。

**可变类型的默认值陷阱**

在Python中，列表、字典等可变对象不适合作为函数或方法的默认参数。这是因为默认参数的值是在函数定义时计算并初始化的，而非每次调用时。这意味着，所有函数调用都会共享同一个可变对象实例，从而导致意外的行为。例如：

```python
# 错误示例：所有实例共享同一个列表
class BadPerson:
    def __init__(self, name: str, hobbies: list = []):  # 危险！
        self.name = name
        self.hobbies = hobbies

p1 = BadPerson("Alice")
p1.hobbies.append("reading")
p2 = BadPerson("Bob")
print(p2.hobbies)  # 输出['reading']——p2意外共享了p1的列表！
```

`dataclasses`模块的field函数可通过default_factory参数指定默认值生成的工厂函数，为可变类型默认值问题提供完美的解决方案：

```python
from dataclasses import dataclass, field  # 导入field函数

@dataclass
class GoodPerson:
    name: str
    # 使用list作为工厂函数，每次创建实例时生成新列表
    hobbies: list = field(default_factory=list)

p1 = GoodPerson("Alice")
p1.hobbies.append("reading")
p2 = GoodPerson("Bob")
print(p2.hobbies)  # 输出[]，每个实例有独立的列表！
```

`field`函数的核心参数：

- `default_factory`：指定一个无参函数（工厂函数），用于生成字段的默认值（如 `list`、`dict`、`lambda` 或自定义函数）；
- `default`：指定不可变类型的默认值（等同于直接赋值，如 `field(default=0)`）；
- `init=False`：表示该字段不参与 `__init__` 方法的参数列表（需手动赋值或通过其他方式初始化）；
- `repr=False`：表示该字段不显示在 `__repr__` 方法的输出中；
- `compare=False`：表示该字段不参与 `__eq__` 等比较方法的逻辑。

```python
from dataclasses import dataclass, field
import uuid
from datetime import date

@dataclass
class Book:
    """一个表示图书信息的数据类"""
    
    # 图书的基本信息，创建实例时必须提供
    title: str          # 书名
    author: str         # 作者
    price: float        # 价格
    
    # 图书的唯一标识，使用UUID自动生成，比较对象时忽略此字段
    book_id: str = field(
        default_factory=lambda: str(uuid.uuid4())[:6],  # 生成6位的唯一ID
        compare=False                                   # 比较对象时不考虑这个字段
    )
    # 出版日期，默认使用当前日期，比较对象时忽略此字段
    publish_date: date = field(
        default_factory=date.today                     # 默认使用今天的日期
    )
    # 内部库存编码，有默认值，打印对象时不显示此字段
    inventory_code: str = field(
        default="N/A",                                  # 默认值为"N/A"
        compare=False,
        repr=False                                      # 打印对象时不显示这个字段
    )

# 创建两本内容相同的图书实例
book1 = Book("Python编程", "张三", 59.90, inventory_code="PY-001")
book2 = Book("Python编程", "张三", 59.90, inventory_code="PY-002")

# 打印第一本书的信息（不会显示inventory_code）
print("第一本书信息:", book1)
# 比较两本书是否相等（只会比较title, author, price）
print("两本书是否相等?", book1 == book2)

# 访问被隐藏的字段
print("第一本书的库存编码:", book1.inventory_code)
print("第一本书的ID:", book1.book_id)
```

**辅助函数**

除了`field`辅助函数外，Python的`dataclasses`模块还提供了一系列实用的工具函数与特殊类型，极大地扩展了数据类的灵活性与功能性：

- `asdict()`：将数据类实例转换为标准字典，
- `astuple()`：将数据类实例转换为元组，
- `replace()`：创建数据类实例的副本，并按需替换指定字段值，
- `fields()`：获取数据类的字段元数据信息，
- `is_dataclass()`：判断对象（类或实例）是否为数据类，
- `make_dataclass()`：动态编程方式创建数据类（无需装饰器），
- `InitVar`：标记仅用于`__init__`初始化的临时变量（不会成为实例属性）。

示例代码如下：

```python
from dataclasses import (
    dataclass, asdict, astuple, replace, fields, 
    is_dataclass, make_dataclass, InitVar,field
)

# 定义基础数据类（含InitVar演示）
@dataclass
class Person:
    name: str
    age: int
    # InitVar标记：address仅用于初始化，不会成为实例属性
    address: InitVar[str] = field(default="未知地址")  # 设置默认值

    def __post_init__(self, address):
        # 利用InitVar参数初始化实例属性
        self.full_info = f"{self.name} ({self.age}), 地址: {address}"

# 创建实例
person = Person("Alice", 30, "123 Main St")

# 1. asdict()：转字典
print("asdict结果:", asdict(person))

# 2. astuple()：转元组
print("astuple结果:", astuple(person))

# 3. replace()：创建副本并修改字段
new_person = replace(person, age=31)
print("replace后的实例:", new_person)

# 4. fields()：获取字段信息
print("\n字段信息:")
for field_info in fields(person):
    print(f"字段名: {field_info.name}, 类型: {field_info.type}, 是否InitVar: {isinstance(field_info.type, InitVar)}")

# 5. is_dataclass()：判断是否为数据类
print("\nis_dataclass(Person):", is_dataclass(Person))
print("is_dataclass(person):", is_dataclass(person))
print("is_dataclass(dict):", is_dataclass(dict))

# 6. make_dataclass()：动态创建数据类
DynamicPerson = make_dataclass(
    "DynamicPerson",  # 类名
    [("name", str), ("age", int)],  # 字段列表
    namespace={"greet": lambda self: f"Hello, {self.name}!"}  # 额外方法/属性
)
dynamic_person = DynamicPerson("Bob", 25)
print("\n动态创建的数据类实例:", dynamic_person)
print("动态类方法调用:", dynamic_person.greet())
```

**初始化后处理**

在`dataclasses`模块中，`__post_init__`是一个魔术方法，会在自动生成的`__init__`方法执行完毕后立即被调用，主要用于实现初始化后的自动处理逻辑（例如计算派生字段、补充属性赋值等）；当与指定`init=False`的字段配合使用时，该方法可灵活处理无需作为构造函数参数传入、仅需通过初始化后逻辑生成的派生属性。

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1
    total_price: float = field(init=False)  # 总价由其他字段计算
    
    def __post_init__(self):
        """初始化后自动计算总价"""
        self.total_price = self.price * self.quantity

# 使用示例
apple = Product("Apple", 5.5, 10)
banana = Product("Banana", 3.0)

print(f"Apple total: ${apple.total_price}")  # 输出: 55.0
print(f"Banana total: ${banana.total_price}")  # 输出: 3.0
```

**字段顺序要求**

在定义`dataclass`类字段时，无默认值的字段必须放在有默认值的字段之前。

- 错误写法：先声明带默认值的`address`，再声明无默认值的`id` → 引发语法错误。
- 正确写法：先声明无默认值的`id`，再声明带默认值的`address` → 正常运行。

这并非`dataclass`的专属限制，而是Python语言的基础语法规则。

`@dataclass`装饰器的核心功能之一，是根据类中定义的字段，自动生成`__init__`构造方法。

- 当你这样写：

  ```python
  @dataclass
  class InvalidFieldOrder:
      address: str = "Beijing"
      id: int
  ```

  它会尝试生成这样的

  ```
  __init__
  ```

  ：

  ```python
  def __init__(self, address: str = "Beijing", id: int):
      ...
  ```

但这在Python中**是完全不允许的**！函数定义时，带默认值的参数（可选参数）不能出现在无默认值的参数（必填参数）之前。

- 而正确的写法：

  ```python
  @dataclass
  class ValidFieldOrder:
      id: int
      address: str = "Beijing"
  ```

  会生成合法的

   

  ```
  __init__
  ```

  ：

  ```python
  def __init__(self, id: int, address: str = "Beijing"):
      ...
  ```

这完全符合Python的语法规范：必填参数在前，可选参数在后。

**数据类继承**

数据类既可以作为父类被其他数据类继承，也可以被普通Python类继承：当数据类继承另一个数据类时，子类会自动合并父类的字段；而普通类继承数据类时，若需使用父类的字段和构造逻辑，则必须手动调用父类的构造函数并处理相关参数。

```python
from dataclasses import dataclass

# 🟡 基类：形状（数据类）
@dataclass
class Shape:
    color: str

# 🟦 子类：正方形（数据类）
@dataclass
class Square(Shape):
    side_length: float = 1.0  # 默认边长为1

# 🟢 子类：圆形（普通类，不是数据类）
class Circle(Shape):
    def __init__(self, color: str, radius: float = 1.0):
        # 必须手动调用父类的构造函数来初始化 color
        super().__init__(color)
        self.radius = radius
    
    # 如果需要友好的打印格式，必须自己实现 __repr__ 方法
    def __repr__(self):
        return f"Circle(color='{self.color}', radius={self.radius})"

# 使用示例
red_square = Square("red")
print(red_square) 

blue_circle = Circle("blue", 5.0)
print(blue_circle) 

default_circle = Circle("green")
print(default_circle) 
```

**@dataclass装饰器参数详解**

`@dataclass`装饰器提供了多个可灵活配置的参数，适配各类开发场景。以下为核心参数的详细说明，涵盖功能作用、使用约束及版本要求：

1. `init=True`
   - 控制是否自动生成 `__init__()` 方法。
   - 如果设为 `False`，你需要自己定义 `__init__` 方法。
2. `repr=True`
   - 控制是否自动生成 `__repr__()` 方法。
   - 生成的 `repr` 会包含类名和所有字段及其值。
3. `eq=True`
   - 控制是否自动生成 `__eq__()` 方法。
   - 基于类的字段值进行相等性比较。
4. `order=False`
   - 控制是否生成比较运算符方法 (`__lt__`, `__le__`, `__gt__`, `__ge__`)。
   - 设为 `True` 时，会根据字段定义的顺序进行比较。
   - 注意：设置 `order=True` 时，`eq` 必须为 `True`（默认）。
5. `unsafe_hash=False`
   - 控制是否生成 `__hash__()` 方法。
   - 默认情况下：
     - 如果 `frozen=True`，会生成基于字段的 `__hash__`
     - 如果 `frozen=False`，`__hash__` 会被设为 `None`
   - 设为 `True` 会强制生成 `__hash__`，但在实例可变时使用可能导致问题。
6. `frozen=False`
   - 如果设为 `True`，会创建一个“冻结”的类，实例属性无法被修改。
   - 尝试修改会抛出 `dataclasses.FrozenInstanceError`。
7. `match_args=True` (Python 3.10+)
   - 控制是否生成 `__match_args__` 属性，用于模式匹配。
8. `kw_only=False` (Python 3.10+)
   - 如果设为`True`，所有字段都将成为关键字参数，实例化时必须通过关键字形式传参，不能使用位置参数。
9. `slots=False` (Python 3.10+)
   - 如果设为 `True`，会生成 `__slots__` 属性，能限制类实例只能拥有预定义的属性，同时节省内存并提高属性访问速度。
10. `weakref_slot=False` (Python 3.11+)
    - 当 `slots=True` 时，如果设为 `True`，会添加一个用于弱引用的槽位。

示例代码如下：

```python
from dataclasses import dataclass, FrozenInstanceError
import weakref

# 1. init=False 示例
@dataclass(init=False)
class Person:
    name: str
    age: int
    
    # 手动定义 __init__ 方法
    def __init__(self, name):
        self.name = name
        self.age = 0  # 设置默认年龄

# 2. repr=False 示例
@dataclass(repr=False)
class Point:
    x: int
    y: int
    
    # 自定义 repr
    def __repr__(self):
        return f"Point at ({self.x}, {self.y})"

# 3. eq=True示例
@dataclass(eq=True)
class Product:
    id: int
    name: str

# 4. order=True 示例
@dataclass(order=True)
class Student:
    score: int
    name: str

# 5. unsafe_hash=True 示例
@dataclass(unsafe_hash=True)
class Book:
    title: str
    author: str

# 6. frozen=True 示例
@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

# 7. match_args=True 示例 (Python 3.10+)
@dataclass(match_args=True)
class Shape:
    type: str
    size: int

# 8. kw_only=True 示例 (Python 3.10+)
@dataclass(kw_only=True)
class Car:
    brand: str
    model: str

# 9. slots=True 示例 (Python 3.10+)
@dataclass(slots=True)
class User:
    id: int
    username: str

# 10. weakref_slot=True 示例 (Python 3.11+)
@dataclass(slots=True, weakref_slot=True)
class Node:
    value: int

# 测试代码
if __name__ == "__main__":
    # 1. 测试 init=False
    p = Person("Alice")
    print(f"1. Person: {p.name}, {p.age}")
    
    # 2. 测试 repr=False
    point = Point(3, 4)
    print(f"2. Point: {point}")
    
    # 3. 测试 eq=True
    p1 = Product(1, "Apple")
    p2 = Product(1, "Apple")
    print(f"3. Products equal? {p1 == p2}")
    
    # 4. 测试 order=True
    s1 = Student(90, "Bob")
    s2 = Student(85, "Alice")
    print(f"4. s1 > s2? {s1 > s2}") # 按照参数定义顺序比较
    
    # 5. 测试 unsafe_hash=True
    book = Book("Python", "Guido")
    print(f"5. Book hash: {hash(book)}")
    
    # 6. 测试 frozen=True
    immutable_point = ImmutablePoint(1, 2)
    try:
        immutable_point.x = 3
    except FrozenInstanceError as e:
        print(f"6. Frozen error: {e}")
    
    # 7. 测试 match_args=True (Python 3.10+)
    shape = Shape("circle", 5)
    match shape:
        case Shape("circle", size):
            print(f"7. Circle with size {size}")
        case Shape("square", size):
            print(f"7. Square with size {size}")
    
    # 8. 测试 kw_only=True
    car = Car(brand="Toyota", model="Camry")
    print(f"8. Car: {car}")
    
    # 9. 测试 slots=True
    user = User(1, "admin")
    print(f"9. User: {user}")
    try:
        user.email = "admin@example.com"
    except AttributeError as e:
        print(f"9. Slots error: {e}")
    
    # 10. 测试 weakref_slot=True
    node = Node(10)
    ref = weakref.ref(node)
    print(f"10. Weakref node value: {ref().value}")
```

# 2 参考

- [Data Classes: @dataclass Decorator](https://www.krython.com/tutorial/python/data-classes-dataclass-decorator)

本文来自博客园，作者：[落痕的寒假](https://www.cnblogs.com/luohenyueji/)，转载请注明原文链接：https://www.cnblogs.com/luohenyueji/p/19269848

« ](https://www.cnblogs.com/luohenyueji/p/19164198)上一篇： [[python\] 代码性能分析工具line_profiler使用指北](https://www.cnblogs.com/luohenyueji/p/19164198)
[» ](https://www.cnblogs.com/luohenyueji/p/19368711)下一篇： [[机器学习\] 类别变量编码库category_encoders使用指南](https://www.cnblogs.com/luohenyueji/p/19368711)



# 79.wsgiref

### 参考网址1：https://cloud.tencent.com/developer/article/1927644

### 参考网址2：https://www.cnblogs.com/yangykaifa/p/19457018

之前写了python的http原生模块，分析了原生http模块的实现原理以及不足;而实际使用过程中，用的比较多的是python的wsgi server和wsgi application; 关于什么是wsgi协议，简单的来说，就是wsgi server调用wsgi application接口的约定，即当有个请求到达wsgi server时，wsgi server通过调用wsgi application提供的接口来处理这个请求;其实，看过python wsgiref模块，也就能理解什么是wsgi模块。

![圆明园遗址(时光相册制作)](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2016/12/9/e69d00e7c1ac6023fb0a7b081fddfb69~tplv-t2oaga2asx-jj-mark:3024:0:0:0:q75.awebp)

现在比较流行的wsgi application有bottle, flask,django等，比较流行的wsgi server有werkzeug,gunicorn,gevent等;今天这篇文章主要分析下python自带的wsgiref模块，以这个为模板，可以理解下wsgi协议；

这篇文章主要有以下两部分：

1. wsgiref简单示例
2. wsgiref实现原理
3. 原理解释示例程序
4. 总结

## wsgiref简单示例

这里先给出wsgiref模块的简单示例，有个感性的认识，后续在分析实现原理；代码如下:

```
 体验AI代码助手 代码解读复制代码from wsgiref.simple_server import make_server
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello, web!']
if __name__ == '__main__':
    httpd = make_server('', 9999, application)
    print("Serving HTTP on port 9999...")
    httpd.serve_forever()
```



这个示例程序很简单，创建一个httpd服务器，并监听9999端口，当有客户端请求时，在浏览器显示Hello, web字符串；

上述例子中的application就是wsgiref application，当然也可以一个类，平时常见的也是类，例如flask,bottle等，这些类实现__call__方法，并且该方法参数为environ, start_response即可，environ为一个字典，保存系统变量以及请求相关属性，例如请求路径，请求参数，请求方法等等；start_response为函数，设置response的状态码和header，然后application函数的返回值为response的body；因此上述例子程序，设置response状态码为200，表示请求成功，在headers添加返回数据类型为text/html，以及返回的response body为[b'

# Hello, web!

']



## wsgiref实现原理

wsgiref模块也是由server和handler组成，server用于监听端口，接收请求；handler用于处理请求；先来看下server

```
 体验AI代码助手 代码解读复制代码class WSGIServer(HTTPServer):
    """BaseHTTPServer that implements the Python WSGI protocol"""
    application = None
    def server_bind(self):
        """Override server_bind to store the server name."""
        HTTPServer.server_bind(self)
        self.setup_environ()
    def setup_environ(self):
        # Set up base environment
        env = self.base_environ = {}
        env['SERVER_NAME'] = self.server_name
        env['GATEWAY_INTERFACE'] = 'CGI/1.1'
        env['SERVER_PORT'] = str(self.server_port)
        env['REMOTE_HOST']=''
        env['CONTENT_LENGTH']=''
        env['SCRIPT_NAME'] = ''
    def get_app(self):
        return self.application
    def set_app(self,application):
        self.application = application
```



WSGIServer继承自HTTPServer，并重载来server_bind方法，同时提供注册和获取server application的接口；其中set_environ函数设置了该web应用程序的环境变量，例如服务器名称，服务器端口等等；

ok，了解来WSGIServer之后，来看下handler是如何实现；WSGIRequestHandler类继承自BaseHTTPRequestHandler，并且重载handle方法，即处理请求的方法；

我们来看下WSGIRequestHandler的handle方法：

```
 体验AI代码助手 代码解读复制代码def handle(self):
        """Handle a single HTTP request"""
	# 读取客户端发送的请求行
        self.raw_requestline = self.rfile.readline(65537)
        if len(self.raw_requestline) > 65536:
            self.requestline = ''
            self.request_version = ''
            self.command = ''
            self.send_error(414)
            return
	# 解析客户端的请求行和请求头
        if not self.parse_request(): # An error code has been sent, just exit
            return
        # Avoid passing the raw file object wfile, which can do partial
        # writes (Issue 24291)
        stdout = BufferedWriter(self.wfile)
        try:
	　　# 用于调用wsgi application的handler
            handler = ServerHandler(
                self.rfile, stdout, self.get_stderr(), self.get_environ()
            )
            handler.request_handler = self      # backpointer for logging
            handler.run(self.server.get_app())
        finally:
            stdout.detach()
```



handle函数首先解析请求行和请求头，然后实例化ServerHandler类，用该类来调用wsgi application；

ServerHandler类接受参数为socket读端，输出端，错误输出端以及一个包含请求信息的字典；self.get_environ()函数返回包含web应用程序的环境变量和请求的环境变量的字典；

最后再来看下ServerHandler;ServerHandler继承自SimpleHandler,SimpleHandler继承自BaseHandler；我们直接看下ServerHandler的run方法；

```
 体验AI代码助手 代码解读复制代码def run(self, application):
	try:
            self.setup_environ()
            self.result = application(self.environ, self.start_response)
            self.finish_response()
        except:
            try:
                self.handle_error()
            except:
                # If we get an error handling an error, just give up already!
                self.close()
                raise   # ...and let the actual server figure it out.
```

1. self.setup_environ函数用于建立每次请求的相关信息，并存储在self.environ；
2. self.start_response为该handler函数，用于设置response的状态码和header；
3. self.result为response body；
4. self.finish_response用于将response返回给客户端；



这个handler类就不一一分析了，详情可以看wsgiref/handlers.py模块；

## 原理解释示例程序

了解了wsgiref模块之后．从原理层面来解释上述例子程序；再次粘帖程序代码如下:

```
 体验AI代码助手 代码解读复制代码from wsgiref.simple_server import make_server
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello, web!']
if __name__ == '__main__':
    httpd = make_server('', 9999, application)
    print("Serving HTTP on port 9999...")
    httpd.serve_forever()
```



示例程序先是调用wsgiref模块的make_server方法，可以看下该方法如下：

```
 体验AI代码助手 代码解读复制代码def make_server(
    host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler
):
    """Create a new WSGI server listening on `host` and `port` for `app`"""
    server = server_class((host, port), handler_class)
    server.set_app(app)
    return server
```



可以看到wsgiref默认的server_class为WSGIServer，handler_class为WSGIRequestHandler；先是实例化一个WSGIServer，然后注册application，最后返回该server实例；

在示例程序中，最后调用httpd.server_forever()方法开启事件监听循环；

当某个请求到来之后，先是实例化一个WSGIRequestHandler，并在该WSGIRequestHandler的handle方法内部解析请求参数，以及实例化一个ServerHandler，以及调用ServerHandler的run方法来处理请求；

在ServerHandler的run方法内部先是建立环境变量字典environ，然后调用wsgi application设置resopnse的状态码和headers，以及返回response body；最后调用finish_response()方法将response返回给客户端；

上述即为一次请求全过程；

## 总结

这篇文章分析了python的wsgiref模块，解释了wsgiref模块一次请求的过程；当然实际应用中，wsgi application可不是示例程序中那么简单的返回一个字符串，因为一个web应用程序需要根据路由来调用相应的view函数以及一些其他特性，这等到分析bottle时再来分析；

wsgi server和wsgi application分离的设计，使python web的开发非常灵活，在部署python web应用程序时，可以根据性能的需求，选择合适的wsgi server；例如flask自带的wsgi server不适合在正式工业环境中使用，因此flask经常的搭配是nginx+gunicorn+flask，而不是用自带的werkzeug；

不同的wsgi server，区别主要是在并发模型的选择上，有单线程，多进程，多线程，协程；而wsgi application主要功能相近，无非就是根据请求路由，执行相应的view函数，当然有一些特性上的不同



# 80 secret

## 使用`secrets`模块生成密码

Python的`secrets`模块是一个生成安全随机数的工具。可以使用它来生成随机密码。

```python
python 体验AI代码助手 代码解读复制代码import secrets
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# 生成12字符的随机密码
password = generate_password()
print(password)
```

上述代码首先导入`secrets`、`string`模块，然后定义了一个`generate_password`函数，该函数接受一个长度参数，并在指定的字符集合中生成随机密码。

### 示例输出：

```bash
bash

 体验AI代码助手
 代码解读
复制代码F8w$Y)qLp#5@
```

使用`secrets`模块生成的密码具有高度的随机性和安全性，适合用于重要账户。

## 使用`random`模块生成密码

除了`secrets`模块，还可以使用Python的内置`random`模块来生成密码。但要注意，`random`模块生成的密码不如`secrets`模块安全。

```python
python 体验AI代码助手 代码解读复制代码import random
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

# 生成12字符的随机密码
password = generate_password()
print(password)
```

上述代码与前面的示例类似，但使用了`random`模块来生成密码。

### 示例输出：

```perl
perl

 体验AI代码助手
 代码解读
复制代码Zu9H|v%fS#bR
```

虽然`random`模块生成的密码可以用于一般用途，但不建议用于重要账户。

## 使用第三方库生成密码

除了Python内置的模块，还可以使用第三方库来生成密码。一个常用的库是`passlib`，它提供了更多密码生成选项和密码安全性配置。

首先，需要安装`passlib`库：

```bash
bash

 体验AI代码助手
 代码解读
复制代码pip install passlib
```

然后可以使用它来生成密码：

```python
python 体验AI代码助手 代码解读复制代码from passlib import pwd

def generate_password():
    return pwd.genword(length=12, charset='ascii_62')

# 生成12字符的随机密码
password = generate_password()
print(password)
```

`passlib`库提供了更多的密码生成选项，例如，可以指定密码长度、字符集合等。

### 示例输出：

```
 体验AI代码助手
 代码解读
复制代码L8X8fz7wrTht
```

## 示例：生成多种类型的随机密码

除了生成随机密码，有时候需要生成不同类型的密码，比如只包含字母、只包含数字、只包含特殊字符等。下面是一些示例代码，演示如何生成不同类型的随机密码。

### 1. 生成只包含字母的密码

```python
python 体验AI代码助手 代码解读复制代码import secrets
import string

def generate_alpha_password(length=12):
    alphabet = string.ascii_letters
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# 生成12字符的只包含字母的随机密码
alpha_password = generate_alpha_password()
print(alpha_password)
```

### 示例输出：

```
 体验AI代码助手
 代码解读
复制代码cXWYzPrAxVqR
```

### 2. 生成只包含数字的密码

```python
python 体验AI代码助手 代码解读复制代码import secrets
import string

def generate_numeric_password(length=12):
    digits = string.digits
    password = ''.join(secrets.choice(digits) for _ in range(length))
    return password

# 生成12字符的只包含数字的随机密码
numeric_password = generate_numeric_password()
print(numeric_password)
```

### 示例输出：

```
 体验AI代码助手
 代码解读
复制代码738214965023
```

### 3. 生成只包含特殊字符的密码

```python
python 体验AI代码助手 代码解读复制代码import secrets
import string

def generate_special_password(length=12):
    special_chars = string.punctuation
    password = ''.join(secrets.choice(special_chars) for _ in range(length))
    return password

# 生成12字符的只包含特殊字符的随机密码
special_password = generate_special_password()
print(special_password)
```

### 示例输出：

```ruby
ruby

 体验AI代码助手
 代码解读
复制代码%&$!#*@~?^><
```

通过这些示例代码，可以根据需要生成不同类型的随机密码。

## 自定义密码生成函数

如果有特定的密码生成要求，可以自定义一个密码生成函数，以满足你的需求。

以下是一个示例，生成包含大写字母、小写字母和数字的密码：

```python
python 体验AI代码助手 代码解读复制代码import secrets
import string

def generate_custom_password(length=12):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# 生成12字符的自定义随机密码
custom_password = generate_custom_password()
print(custom_password)
```

### 示例输出：

```
 体验AI代码助手
 代码解读
复制代码vE3XgYw6Ks2R
```

通过自定义密码生成函数，可以根据自己的需求生成符合特定要求的密码。

## 总结

本文介绍了多种方法来生成随机密码，包括使用Python的`secrets`模块、`random`模块，以及第三方库`passlib`。同时，还演示了如何生成不同类型的密码，如只包含字母、只包含数字、只包含特殊字符等。生成强密码对于保护账户和数据的安全至关重要。希望本文中的示例代码和技巧对大家有所帮助，能够生成安全的密码，提高信息安全水平。

------

# Python学习路线

[更多学习内容：ipengtao.com](https://link.juejin.cn?target=http%3A%2F%2Fipengtao.com%2F)

![Python基础知识.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/326fd2f36433408b944365d881ec80e3~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=1200&h=1146&s=53628&e=webp&b=fffcfc)



# 81 dbm
## 参考文档1

### 使用 Python Shelve 和 DBM 模块实现简单的数据持久化

原创于 2024-11-26 08:50:10 发布·793 阅读

·![img](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)14

·![img](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png) 13·

CC 4.0 BY-SA版权

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)[#数据库](https://so.csdn.net/so/search/s.do?q=数据库&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

Python3.8一键部署

Python 是一种高级、解释型、通用的编程语言，以其简洁易读的语法而闻名，适用于广泛的应用，包括Web开发、数据分析、人工智能和自动化脚本

![推荐](https://i-operation.csdnimg.cn/images/6eb9ff06260940f7818aa8dc9f2db97b.png)

在 Python 开发中，常常需要将数据持久化以便后续使用。虽然有许多数据库解决方案可供选择，但在某些场景下，我们只需要一个简单、快速且易于使用的方式来存储数据。这时，Python 的 `shelve` 和 `dbm` 模块就显得尤为重要。本文将详细介绍这两个模块的使用方法及其优缺点。

### 什么是 Shelve？

`shelve` 是 Python 的标准库之一，提供了一种方便的持久化存储方式。它允许开发者以键值对的形式存储 Python 对象，数据存储在文件中，使用起来类似于字典（`dict`）。`shelve` 模块使用 `pickle` 模块将对象序列化并保存，因此几乎可以存储所有类型的 Python 对象。

### 什么是 DBM？

`dbm` 模块也是 Python 标准库的一部分，提供了一种基于文件的键值对数据库接口。`dbm` 允许使用简单的字符串作为键，支持对键值的持久化存储。与 `shelve` 不同，`dbm` 模块更接近于低级数据库操作，通常适合需要高效存储和快速访问的场景。

#### 主要特点

- dbm

  :

  - **轻量级**：`dbm` 提供了轻量级的键值对存储。
  - **速度快**：适合高效存储和快速访问。
  - **简单接口**：提供简单的接口来管理数据，适合基本的键值对存储需求。

### Shelve 和 DBM 的对比

| 特点     | Shelve                   | DBM                    |
| -------- | ------------------------ | ---------------------- |
| 数据类型 | 任意 Python 对象         | 字符串键，字节值       |
| 存储方式 | 使用 `pickle` 序列化     | 直接存储键值对         |
| 使用场景 | 简单数据持久化，快速原型 | 高效存储和快速访问     |
| 复杂性   | 简单易用，类似字典       | 低级接口，需要处理字节 |
| 适用性   | 小型应用，快速开发       | 高效、高性能应用       |

### 使用示例

#### 1. Shelve 模块使用示例

```python
import shelve

# 创建或打开一个 shelve 数据库
with shelve.open('my_shelve.db') as db:
    # 向数据库中写入数据
    db['name'] = 'Alice'
    db['age'] = 30
    db['hobbies'] = ['reading', 'hiking', 'coding']

# 读取数据
with shelve.open('my_shelve.db') as db:
    name = db['name']
    age = db['age']
    hobbies = db['hobbies']
    
    print(f'Name: {name}')        # 输出：Name: Alice
    print(f'Age: {age}')          # 输出：Age: 30
    print(f'Hobbies: {hobbies}')  # 输出：Hobbies: ['reading', 'hiking', 'coding']
AI写代码python运行123456789101112131415161718
```

#### 2. DBM 模块使用示例

使用 `dbm` 模块存储键值对数据，首先需要选择一个 DBM 实现，例如 `dbm.dumb`（内存中的简单实现）或 `dbm.gnu`（GNU dbm 的实现）。

```python
import dbm

# 创建或打开一个 DBM 数据库
with dbm.open('my_dbm.db', 'c') as db:
    # 向数据库中写入数据
    db[b'name'] = b'Alice'  # 需要将字符串转换为字节
    db[b'age'] = b'30'
    db[b'hobbies'] = b'reading,hiking,coding'

# 读取数据
with dbm.open('my_dbm.db', 'r') as db:
    name = db[b'name'].decode('utf-8')  # 读取字节并解码为字符串
    age = db[b'age'].decode('utf-8')
    hobbies = db[b'hobbies'].decode('utf-8').split(',')

    print(f'Name: {name}')        # 输出：Name: Alice
    print(f'Age: {age}')          # 输出：Age: 30
    print(f'Hobbies: {hobbies}')  # 输出：Hobbies: ['reading', 'hiking', 'coding']
AI写代码python运行123456789101112131415161718
```

### 使用场景

#### Shelve

- **简单的数据持久化**：如果你需要快速存储和检索数据，而不想使用复杂的数据库，`shelve` 是理想选择。
- **原型开发**：在快速原型开发过程中，`shelve` 提供了一个方便的存储解决方案。
- **小型应用**：当应用的规模较小，不需要高性能的数据库时，使用 `shelve` 可以简化代码。

#### DBM

- **高效存储和快速访问**：当需要高效的键值对存储时，使用 `dbm` 模块更为合适。
- **简化的数据库管理**：对于不需要复杂结构的小型应用，`dbm` 可以提供足够的功能。
- **嵌入式应用**：适合需要快速读写和低延迟的嵌入式场景。

### 注意事项

- **shelve**：
  - **并发限制**：不适合多线程或多进程同时写入操作。
  - **序列化限制**：存储的对象必须支持 `pickle` 序列化，特别是自定义类的实例。
- **dbm**：
  - **数据类型限制**：仅支持字符串键和字节值，使用时需要注意类型转换。
  - **简单接口**：虽然接口简单，但没有像 `shelve` 那样的复杂对象支持。

### 总结

Python 的 `shelve` 和 `dbm` 模块为开发者提供了两种简单易用的键值对持久化存储方式。`shelve` 适合简单数据持久化和原型开发，而 `dbm` 则更适合高效存储和快速访问。根据不同的需求，开发者可以选择最合适的存储方案

## 参考文档2

Python 的 `dbm` 模块是标准库中用于创建和管理**基于磁盘的轻量级键值对数据库**的通用接口。它允许像操作字典一样存储和检索字节字符串数据，特别适用于小型应用、缓存、配置文件等需要持久化存储且不希望配置庞大数据库（如 SQLite）的场景。 

1. `dbm` 核心特性与优势

- **持久化存储：** 数据存储在磁盘文件上，即使程序关闭数据也不会丢失。
- **字典接口：** 操作方式极度类似于 Python 字典（`__getitem__`, `__setitem__`）。
- **轻量级：** 无需安装任何第三方库，内置即可使用。
- **通用性：** 自动在 `dbm.gnu` (gdbm), `dbm.ndbm` 或 `dbm.dumb`（纯 Python 实现）之间选择最好的实现方式。 
- 快速入门：基本用法

使用 `dbm.open()` 打开数据库，操作完成后必须使用 `.close()` 关闭。

python

```
import dbm

# 1. 打开/创建数据库 (模式: 'c' - 如果不存在则创建)
with dbm.open('my_database', 'c') as db:
    # 2. 像字典一样插入数据 (键和值必须是 bytes 或 string)
    db['key1'] = 'value1'
    db['key2'] = 'value2'
    
    # 3. 读取数据
    print(db['key1'])  # 输出: b'value1' (返回的是bytes)
    
    # 4. 检查键是否存在
    if 'key2' in db:
        print(db['key2'])

# 5. 读取数据 (使用 .get() 方法，避免键不存在报错)
with dbm.open('my_database', 'r') as db:
    value = db.get('key3', b'default_value')
    print(value)
```

请谨慎使用此类代码。

3. `dbm.open()` 模式参数详解

`dbm.open(filename, flag='r', mode=0o666)` 中的 `flag` 参数决定了文件的操作模式：

| 模式  | 描述                             |
| ----- | -------------------------------- |
| `'r'` | 只读（默认）                     |
| `'w'` | 读写，不创建新文件               |
| `'c'` | 读写，如果不存在则创建（最常用） |
| `'n'` | 始终创建新空数据库，进行读写     |

4. `dbm` 与其他持久化模块的区别

- **dbm vs Dict:** `dbm` 的键和值必须是字符串或字节串（bytes），而 Python 字典可以存储任何 Python 对象。
- **dbm vs shelve:** `dbm` 仅存字符/字节。如果需要直接将复杂的 Python 对象（如列表、字典、自定义类实例）持久化，应该使用 [`shelve`](https://docs.python.org/zh-cn/3/library/dbm.html) 模块，它是 `dbm` 的封装。
- **dbm vs sqlite3:** `dbm` 是无结构映射，SQLite 是关系型数据库。适用于极小应用场景，不支持 SQL 查询。 
- 注意事项

- **数据类型：** 存入的数据如果非字符串/字节类型，需要先进行序列化（例如使用 `json` 或 `pickle`）。
- **文件兼容性：** 不同平台（Linux/Windows）可能使用不同的底层 DBM 实现，导致生成的文件在不同系统之间不一定通用。 

#### 示例

```
"""
dbm.open() 模式参数详解dbm.open(filename, flag='r', mode=0o666) 中的 flag 参数决定了文件的操作模式：模式 
描述'r'只读（默认）'w'读写，不创建新文件'c'读写，如果不存在则创建（最常用）'n'始终创建新空数据库，进行读写
"""

import  dbm

def create_data():
    db = dbm.open("user.db",'c')
    db['user_id'] = '1'
    db['name'] = "Kenny rogers"
    db.setdefault(b"age", b"30")
    db.close()

def show_data():
    db=dbm.open("user.db",'r')
    for k, v in db.items():
        print(f"{k.decode()}: {v.decode()}")

    print(f"keys: {db.keys()}") # Output: keys: [b'age', b'name', b'user_id']
    print(f"values: {list(db.values())}") # Output: values: [b'30', b'John Doe', b'1']
    db.close()

def change_data(): # after you change data,you need to close the db first,or something comes out strange
     db = dbm.open("user.db",'c') 
     db['user_id'] = '2'
     db['name'] = b"James Lou"
     db['gender'] = 'male'
     db.close()

def del_record():
      db = dbm.open("user.db",'c') 
      # del the gender field
      del db['gender']
      db.close()  

def search_key():
    db = dbm.open("user.db",'c')   
    print("name" in db)  #True
    print("age" in db) #True
    print("gender" in db)# False

if __name__ == '__main__':
    # create_data()
    # show_data()
    # change_data()
    # del_record()
    search_key()
```





