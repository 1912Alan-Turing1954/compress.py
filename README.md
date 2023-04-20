# compress.py

## This is a compression command, that can iterate through your entire Drive and find a file of your choice and compress it down 50% - 90%.

### To use simply Download the project.zip file, extract and place the compress.exe in this directory 'C:\Windows\System32'

```Python
def compress():
        filename = str(input('Enter filename that you wish to compress: '))
        start_time = perf_counter()

        for relPath, dirs, files in os.walk(root):
            if filename in files:
                fullPath = os.path.join(root, relPath, filename)
                text = open(fullPath, 'rb').read()
                print('---------------')
                print(f'Raw file size: {sys.getsizeof(text)}')
                print('---------------')
                compressed = base64.b64encode(zlib.compress(text, 9))
                print(f'Compressed file size: {sys.getsizeof(compressed)}')
                print('---------------')
                print(f'Compress percentage: {round(100.0 - ((float(sys.getsizeof(compressed))/float(sys.getsizeof(text))) * 100.0), 2)}%')
                print('---------------')
                print(f'Fullpath to compressed file: {fullPath}')
                end_time = perf_counter()
                print(f'(Time to execute and compress: {round(end_time - start_time, 2)}s)')
                savecomp = open(fullPath, 'wb').write(compressed)
                return savecomp

```
