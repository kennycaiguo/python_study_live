import codecs

def test1():
    bstr1 = b"welcome to python course"
    encoded = codecs.encode(bstr1,"hex") # 需要字节串，而不是字符串
    print(f"Encoded: {encoded}")
    decoded = codecs.decode(encoded,"hex")
    print(f"Decoded:{decoded}")


if __name__ == '__main__':
    test1()
