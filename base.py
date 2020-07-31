import zlib
import os


def compress(infile, dst, level=9):
    infile = open(infile, 'rb')
    dst = open(dst, 'wb')
    compress = zlib.compressobj(level)
    data = infile.read(1024)
    while data:
        dst.write(compress.compress(data))
        data = infile.read(1024)
    dst.write(compress.flush())


def decompress(infile, dst):
    infile = open(infile, 'rb')
    dst = open(dst, 'wb')
    decompress = zlib.decompressobj()
    data = infile.read(1024)
    while data:
        dst.write(decompress.decompress(data))
        data = infile.read(1024)
    dst.write(decompress.flush())

def dirlist(path):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            os.mkdir(filepath.replace("src_c","src_c1"))
            dirlist(filepath)
        else:
            print(filepath)
            decompress(filepath,filepath.replace("src_c","src_c1"))

            print(filepath[:-4]+"decrypt success")


if __name__ == "__main__":
    dirlist("d:/Desktop/xxx/assets1/src_c")

