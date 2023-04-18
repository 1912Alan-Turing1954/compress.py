import zlib, sys, time, base64, os

option = str(input('Enter if you would to compress a file or dcompress a file, (Compress/Decompress): '))

# hint = str(input('Enter a hint of where this file may be located (opiontional): '))

# if hint:
#     root = f'C:\{hint}'
# else:
root = 'C:\\'


def compress():

    filename = str(input('Enter filename that you wish to compress: '))

    for relPath, dirs, files in os.walk(root):
        if filename in files:
            fullPath = os.path.join(root, relPath, filename)
            text = open(fullPath, 'rb').read()
            path = os.path.split(fullPath)[0]
            name = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            print(f'\nRaw size: {sys.getsizeof(text)}')
            print('---------------')
            compressed = base64.b64encode(zlib.compress(text,9))
            print(f'9 compressed size: {sys.getsizeof(compressed)}')
            print('---------------')
            print(f'Compress percentage: {100.0 - ((float(sys.getsizeof(compressed))/float(sys.getsizeof(text))) * 100.0)}%')
            print('---------------')
            
            savecomp = open(fullPath, 'wb').write(compressed)
            return savecomp

def decompress():
    filename = str(input('Enter filename that you wish to decompress: '))

    for relPath, dirs, files in os.walk(root):
        if filename in files:
            fullPath = os.path.join(root, relPath, filename)
            text = open(fullPath, 'rb').read()
            path = os.path.split(fullPath)[0]
            name = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            print(f'\nCompressed size: {sys.getsizeof(text)}')
            print('---------------')
            decompressed = zlib.decompress(base64.b64decode(text))
            print(f'Raw size: {sys.getsizeof(decompressed)}')
            print('---------------')
            print(f'Decompress percentage: {100.0 - (float(sys.getsizeof(text))/float(sys.getsizeof(decompressed)) * 100.0)}%')
            print('---------------')
            
            savecomp = open(fullPath, 'wb').write(decompressed)
            return savecomp

if option == 'compress' or option == 'Compress' or option == 'COMPRESS' or option == 'c' or option == 'C':
    compress()
elif option == 'decompress' or option == 'Decompress' or option == 'DECOMPRESS' or option == 'd' or option == 'D':
    decompress()