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



# 71. **inspect**



# 72. warnings



# 73. doctest



# 74 . **asyncio**



# 75. pdb python调试器



# 76 concurrent



# 77 io



# 78. dataclasses



# 79.wsgiref



# 80 secret



# 81 dbm









