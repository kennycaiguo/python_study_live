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