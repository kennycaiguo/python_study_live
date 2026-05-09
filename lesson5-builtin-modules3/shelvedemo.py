def shelve_demo1():
    import shelve
    s = shelve.open('test_shelf.db')         #
    try:
        s['kk'] = {'int': 10, 'float': 9.5, 'String': 'Sample data'}
        s['MM'] = [1, 2, 3]
    finally:
        s.close()

def shelve_demo2():
    import shelve
    s = shelve.open('test_shelf.db')
    for k,v in s.items():
        print(f"{k}==>{v}")
    s.close()  
 
def shelve_demo3():
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


if __name__ == '__main__':
    # shelve_demo1()        
    shelve_demo2()        
    # shelve_demo3()        