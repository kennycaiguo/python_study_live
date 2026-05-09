def zlib_demo1():
    import zlib

    MESSAGE = b"life of brian"

    compressed_message = zlib.compress(MESSAGE)
    decompressed_message = zlib.decompress(compressed_message)

    print("original:", repr(MESSAGE)) 
    print("compressed message:", repr(compressed_message)) 
    print("decompressed message:", repr(decompressed_message)) 

#文件的内容决定了压缩比率
def zlib_demo2():
    import zlib
    import glob

    for file in glob.glob("samples/*"):

        indata = open(file, "rb").read()
        outdata = zlib.compress(indata, zlib.Z_BEST_COMPRESSION)

        print(file, len(indata), "=>", len(outdata),) 
        print("%d%%" % (len(outdata) * 100 / len(indata))) 

        

if __name__ == '__main__':
    # zlib_demo1()
    zlib_demo2()
   