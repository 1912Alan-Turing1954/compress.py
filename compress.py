import zlib, sys, base64, os 
from time import perf_counter

def main_program():
    root = ''

    option = str(input('Enter if you would to compress a file or dcompress a file, (Compress/Decompress): '))
        
    drive = str(input('Enter the drive the file is located in (C/E/D), (Optional): '))

    if drive == '':
        root = 'C:\\'
    else:
        root = f'{drive[0].upper()}:\\'

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

    def decompress():
        filename = str(input('Enter filename that you wish to decompress: '))
        start_time = perf_counter()
        
        for relPath, dirs, files in os.walk(root):
            if filename in files:
                fullPath = os.path.join(root, relPath, filename)
                text = open(fullPath, 'rb').read()
                print('---------------')
                print(f'Compressed file size: {sys.getsizeof(text)}')
                print('---------------')
                decompressed = zlib.decompress(base64.b64decode(text))
                print(f'Raw file size: {sys.getsizeof(decompressed)}')
                print('---------------')
                print(f'Decompress percentage: {round(100.0 - (float(sys.getsizeof(text))/float(sys.getsizeof(decompressed)) * 100.0), 2)}%')
                print('---------------')
                print(f'Fullpath to compressed file: {fullPath}')
                end_time = perf_counter()
                print(f'(Time to execute and decompress: {round(end_time - start_time, 2)}s)')
                savecomp = open(fullPath, 'wb').write(decompressed)
                return savecomp


    if option.lower() == 'compress' or option.lower() == 'c':
        compress()
    elif option.lower() == 'decompress' or option.lower() == 'd':
        decompress()
    else:
        print('Empty or Invalid Context\n')
        main_program()

main_program()
start = True

while start == True:
    answer = str(input('Would you like to restart the program? (y/n): '))
    if answer.lower() == 'y' or answer.lower() == 'yes':
        main_program()  # user input calls program again
    elif answer.lower() == 'n' or answer.lower() == 'no':
        start = False # user input finishes program
    else:
        print('Sorry, not a valid answer.')
        