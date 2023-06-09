import zlib, sys, base64, os 
from datetime import datetime
from time import perf_counter

root = 'C:\\'

def main_program():
    root = ''

    option = str(input('Enter if you would to compress or dcompress a file/folder, (Compress/Decompress): '))
        
    drive = str(input('Enter the drive the file is located in (C/E/D), (Optional): '))

    if drive == '':
        root = 'C:\\'
    else:
        root = f'{drive[0].upper()}:\\'

    def compress():
        name = str(input('Enter filename or foldername that you wish to compress: '))
        start_time = perf_counter()

        amount_of_files = []
        before = 0
        after = 0
                
        for relPath, dirs, files in os.walk(root):
            if name in dirs:
                folderPath = os.path.join(root, relPath, name)
                print(folderPath)
                for relPath, dirs, files in os.walk(folderPath):
                    if os.listdir(folderPath) == []:
                        print('---------------')
                        print('Error: Folder is empty')
                        print('---------------')
                        main_program()
                    for file in files:
                        fold = os.path.join(folderPath, relPath, file)
                        text = open(fold, 'rb').read()
                        before += sys.getsizeof(text)
                        compressed = base64.b64encode(zlib.compress(text, 9))
                        after += sys.getsizeof(compressed)                                   
                        end_time = perf_counter()
                        savecomp = open(fold, 'wb').write(compressed)
                        amount_of_files.append(1)
                        
                print('---------------')
                print(f'Amount of files compressed: {len(amount_of_files)}')
                print(f'Folder size before compression: {before}')
                print(f'Folder size after compression: {after}')
                print(f'Compress percentage: {round((float(after)/float(sys.getsizeof(before))), 2)}%')
                print('---------------')
                print(f'Fullpath to compressed folder: {folderPath}')
                print(f'(Time to execute and compress: {round(end_time - start_time, 2)}s)')
                today = datetime.now().date()
                print(f"Current date: {today}")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f'Current Time: {current_time}')
                print('---------------')
                        
            if name in files:
                fullPath = os.path.join(root, relPath, name)
                if os.path.getsize(fullPath) == 0:
                    print('---------------')
                    print("Error: File is empty")
                    print('---------------')
                    main_program() 
                text = open(fullPath, 'rb').read()
                print('---------------')
                print(f'Raw file size: {sys.getsizeof(text)}')
                print('---------------')
                compressed = base64.b64encode(zlib.compress(text, 9))
                print(f'Compressed file size: {sys.getsizeof(compressed)}')
                print('---------------')
                print(f'Compress percentage: {round(((float(sys.getsizeof(compressed))/float(sys.getsizeof(text)))), 2)}%')
                print('---------------')
                print(f'Fullpath to compressed file: {fullPath}')
                end_time = perf_counter()
                print(f'(Time to execute and compress: {round(end_time - start_time, 2)}s)')
                today = datetime.now().date()
                print(f"Current date: {today}")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f'Current Time: {current_time}')
                print('---------------')
                savecomp = open(fullPath, 'wb').write(compressed)
                return savecomp

    def decompress():
        name = str(input('Enter filename or foldername that you wish to decompress: '))
        start_time = perf_counter()
        
        amount_of_files = []
        before = 0
        after = 0
                
        for relPath, dirs, files in os.walk(root):
            if name in dirs:
                folderPath = os.path.join(root, relPath, name)
                print(folderPath)
                for relPath, dirs, files in os.walk(folderPath):
                    if os.listdir(folderPath) == []:
                        print('---------------')
                        print('Error: Folder is empty')
                        print('---------------')
                        main_program()
                    for file in files:
                        fold = os.path.join(folderPath, relPath, file)
                        text = open(fold, 'rb').read()
                        before += sys.getsizeof(text)
                        decompressed = zlib.decompress(base64.b64decode(text))   
                        after += sys.getsizeof(decompressed)                     
                        end_time = perf_counter()
                        savecomp = open(fold, 'wb').write(decompressed)
                        amount_of_files.append(1)
                print('---------------')
                print(f'Amount of files decompressed: {len(amount_of_files)}')
                print(f'Folder size before decompression: {before}')
                print(f'Folder size after decompression: {after}')
                print(f'Decompress percentage: {round((float(after)/float(sys.getsizeof(before))), 2)}%')
                print('---------------')
                print(f'Fullpath to decompressed folder: {folderPath}')
                print(f'(Time to execute and decompress: {round(end_time - start_time, 2)}s)')
                today = datetime.now().date()
                print(f"Current date: {today}")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f'Current Time: {current_time}')
                print('---------------')
            
            if name in files:
                fullPath = os.path.join(root, relPath, name)
                if os.path.getsize(fullPath) == 0:
                    print('---------------')
                    print("Error: File is empty")
                    print('---------------')
                    main_program() 
                text = open(fullPath, 'rb').read()
                print('---------------')
                print(f'Compressed file size: {sys.getsizeof(text)}')
                print('---------------')
                decompressed = zlib.decompress(base64.b64decode(text))
                print(f'Raw file size: {sys.getsizeof(decompressed)}')
                print('---------------')
                print(f'Decompress percentage: {round((float(sys.getsizeof(text))/float(sys.getsizeof(decompressed))), 2)}%')
                print('---------------')
                print(f'Fullpath to compressed file: {fullPath}')
                end_time = perf_counter()
                print(f'(Time to execute and decompress: {round(end_time - start_time, 2)}s)')
                today = datetime.now().date()
                print(f"Current date: {today}")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f'Current Time: {current_time}')
                print('---------------')
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
        