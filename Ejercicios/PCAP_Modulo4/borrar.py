import errno

try:
    x = open("fichero.txt")
except IOError as ioe:
    if ioe.errno==errno.ENOENT:
        print(ioe.errno)