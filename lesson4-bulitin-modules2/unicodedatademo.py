import unicodedata

def test1():
    print(unicodedata.lookup('Cjk Compatibility Ideograph-2f80f')) # 兔
    print(unicodedata.lookup('Armenian Small Ligature Men Now')) # ﬓ

def test2():
    print(unicodedata.name('a')) # LATIN SMALL LETTER A
    print(unicodedata.name('❋')) # HEAVY EIGHT TEARDROP-SPOKED PROPELLER ASTERISK
    print(unicodedata.name('✍')) # WRITING HAND

def test3():
    print(unicodedata.numeric('①')) # 1.0
    print(unicodedata.numeric('一')) # 1.0
    print(unicodedata.numeric('壹')) # 1.0
    print(unicodedata.numeric('Ⅰ')) # 1.0
    print(unicodedata.numeric('1')) # 1.0

def test4():
    '''获取字符的常规分类'''
    print(unicodedata.category('①'))  # 符号
    # No
    print(unicodedata.category('壹'))  # 中文
    # Lo
    print(unicodedata.category('✔'))  # 符号
    # So

def test5():
    '''获取字符的双向字符类型'''
    print(unicodedata.bidirectional(' '))  # WS
    print(unicodedata.bidirectional('①'))   # ON
    print(unicodedata.bidirectional('壹')) # L
    print(unicodedata.bidirectional('✔'))   # ON
    print(unicodedata.bidirectional('1')) # EN
    

def test6():
    '''获取字符的字符宽度分类'''
    print(unicodedata.east_asian_width('①'))  # 符号  -> A
    print(unicodedata.east_asian_width('壹'))  # 中文 ->W
    print(unicodedata.east_asian_width('あ'))  # 日文 ->W
    print(unicodedata.east_asian_width(' '))  # 阿拉伯语中的一个字母 ->Na
    print(unicodedata.east_asian_width('1'))  # 数字 ->Na
    print(unicodedata.east_asian_width('A'))  # 英文字母 ->Na

# test6()
# test5()
# test4()
# test3()
test2()