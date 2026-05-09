import base64

def base64encode_test(str1):
    
    print(f"original string:{str1}")

    bytes1 = str1.encode('utf-8')
    print(f"encoded:{bytes1}")

    encoded = base64.b64encode(bytes1)
    print(f"base64 encoded : {encoded}")

    processed_str = encoded.decode('ascii')
    print(f"decoded string:{processed_str}")

    return processed_str

def base64decode_test(str2):
    decoded_bytes = base64.b64decode(str2)
    print(f"解码后的字节串: {decoded_bytes}")

    # 将字节串解码回原始文本
    decoded_text = decoded_bytes.decode('utf-8')
    print(f"解码后的文本: {decoded_text}")  
    return decoded_text

if __name__ == '__main__':
    str1 = "Hello, 世界! This is a test."
    # base64encode_test(str1)
    str2 = 'SGVsbG8sIOS4lueVjCEgVGhpcyBpcyBhIHRlc3Qu'
    base64decode_test(str2) # Hello, 世界! This is a test.