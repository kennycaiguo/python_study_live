import tarfile

tar = tarfile.open("all.tar.gz","w:gz")

tar.add("tarfiledemo1.py")
tar.add("test.txt")
tar.add("test.tar")
tar.add("test.tar.gz")

tar.close()