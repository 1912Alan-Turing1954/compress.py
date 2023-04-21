import zlib, sys, base64, os
from time import perf_counter

root = 'C:\\'

def main_program():
    root = ''

    option = str(input('Enter if you would to compress dcompress a file or folder, (Compress/Decompress): '))
        
    drive = str(input('Enter the drive the file is located in (C/E/D), (Optional): '))

    if drive == '':
        root = 'C:\\'
    else:
        root = f'{drive[0].upper()}:\\'

    def compress():
        name = str(input('Enter filename or foldername that you wish to compress: '))
        start_time = perf_counter()

        amount_of_files = []
        
        for relPath, dirs, files in os.walk(root):
            if name in dirs:
                folderPath = os.path.join(root, relPath, name)
                print(folderPath)
                for relPath, dirs, files in os.walk(folderPath):
                    for file in files:
                        fold = os.path.join(folderPath, relPath, file)
                        text = open(fold, 'rb').read()
                        compressed = base64.b64encode(zlib.compress(text, 9))                        
                        end_time = perf_counter()
                        savecomp = open(fold, 'wb').write(compressed)
                        amount_of_files.append(1)
                        
                print('---------------')
                print(f'Amount of files compressed: {len(amount_of_files)}')
                print('---------------')
                print(f'Fullpath to compressed folder: {folderPath}')
                print(f'(Time to execute and compress: {round(end_time - start_time, 2)}s)')
                        
            if name in files:
                fullPath = os.path.join(root, relPath, name)
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
        name = str(input('Enter filename or foldername that you wish to decompress: '))
        start_time = perf_counter()
        
        amount_of_files = []
        
        for relPath, dirs, files in os.walk(root):
            if name in dirs:
                folderPath = os.path.join(root, relPath, name)
                print(folderPath)
                for relPath, dirs, files in os.walk(folderPath):
                    for file in files:
                        fold = os.path.join(folderPath, relPath, file)
                        text = open(fold, 'rb').read()
                        decompressed = zlib.decompress(base64.b64decode(text))                        
                        end_time = perf_counter()
                        savecomp = open(fold, 'wb').write(decompressed)
                        amount_of_files.append(1)
                print('---------------')
                print(f'Amount of files compressed: {len(amount_of_files)}')
                print('---------------')
                print(f'Fullpath to decompressed folder: {folderPath}')
                print(f'(Time to execute and decompress: {round(end_time - start_time, 2)}s)')
            
            if name in files:
                fullPath = os.path.join(root, relPath, name)
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
        