import zlib, sys, time, base64, os

option = str(input('Enter if you would to compress a file or dcompress a file, (Compress/Decompress): '))

drive = str(input('Enter the drive the file is located in (C/E/D), (Optional): '))

root = ''

if drive == '':
    root = 'C:\\'
else:
    root = drive[0]

def compress():
    start_time = time.time()
    filename = str(input('Enter filename that you wish to compress: '))

    for relPath, dirs, files in os.walk(root):
        if filename in files:
            fullPath = os.path.join(root, relPath, filename)
            text = open(fullPath, 'rb').read()
            print('---------------')
            print(f'Raw size: {sys.getsizeof(text)}')
            print('---------------')
            compressed = base64.b64encode(zlib.compress(text, 9))
            print(f'Compressed size: {sys.getsizeof(compressed)}')
            print('---------------')
            print(f'Compress percentage: {round(100.0 - ((float(sys.getsizeof(compressed))/float(sys.getsizeof(text))) * 100.0), 2)}%')
            print('---------------')
            print(f'Fullpath to compressed file: {fullPath}')
            print(f'(Tinme to execute and compress the file: {time.time() - start_time})')
            savecomp = open(fullPath, 'wb').write(compressed)
            return savecomp

def decompress():
    start_time = time.time()
    filename = str(input('Enter filename that you wish to decompress: '))
    
    for relPath, dirs, files in os.walk(root):
        if filename in files:
            fullPath = os.path.join(root, relPath, filename)
            text = open(fullPath, 'rb').read()
            print('---------------')
            print(f'Compressed size: {sys.getsizeof(text)}')
            print('---------------')
            decompressed = zlib.decompress(base64.b64decode(text))
            print(f'Raw size: {sys.getsizeof(decompressed)}')
            print('---------------')
            print(f'Decompress percentage: {round(100.0 - (float(sys.getsizeof(text))/float(sys.getsizeof(decompressed)) * 100.0), 2)}%')
            print('---------------')
            print(f'Fullpath to compressed file: {fullPath}')
            print(f'(Tinme to execute and compress the file: {time.time() - start_time})')
            savecomp = open(fullPath, 'wb').write(decompressed)
            return savecomp

if option == 'compress' or option == 'Compress' or option == 'COMPRESS' or option == 'c' or option == 'C':
    compress()
elif option == 'decompress' or option == 'Decompress' or option == 'DECOMPRESS' or option == 'd' or option == 'D':
    decompress()
else:
    print('Invalid option\n')
    option = str(input('Enter if you would to compress a file or dcompress a file, (Compress/Decompress): '))