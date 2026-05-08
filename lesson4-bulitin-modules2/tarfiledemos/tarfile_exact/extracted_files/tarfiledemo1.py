import tarfile

def create_tar(tfname,file):
    with tarfile.open(tfname,'w') as tf:
        tf.add(file)

def create_gz_from_tar(gzfile,tfname):
    with tarfile.open(gzfile,'w:gz') as gz:
        gz.add(tfname)


if __name__ == '__main__':
    # create_tar("test.tar","test.txt")
    create_gz_from_tar("test.tar.gz","test.tar")