import os
import shutil

os.chdir(r'C:\Users\81UJ006KBM\Desktop\FileManager')
CURR_DIR = os.getcwd()

list_of_commands = ["create_folder", "delete_folder", "replace_folder", "create_file", "write_to_file",
                    "read_file", "delete_file", "copy_files", "replace_file", "rename_file",
                    "my_dir(to see your current directory)", "change_dir(to change the current directory to a new one)"]

print('')
print('Possible commands are:')
print('')
print(' - '.join(list_of_commands))
print('')


def create_folder(path):  # 1 Здесь мы создадим пустую папку
    try:
        os.makedirs(path)
    except OSError:
        print('Folder already exists:', path)


def delete_folder(path):  # 2 Здесь мы удалим папку
    try:
        shutil.rmtree(path)
    except OSError:
        print('No such a folder in: ', CURR_DIR)


def replace_folder(original, target):  # 3 Здесь мы изменим директорий на папку (на территории основной папки)
    try:
        shutil.move(original, target)
    except:
        print('An error occurred, check the folder you wanna move')


def create_file(name):  # 4 Здесь мы создадим пустой файл
    with open(name, 'a') as file:
        pass


def write_to_file(file_directory, text):  # 5 Здесь мы сохраним текст в файл
    with open(file_directory, 'a') as file:
        file.write(text)


def read_file(file_directory):  # 6 Здесь мы будем читать текст из файла
    if os.path.exists(file_directory):
        with open(file_directory, 'r') as file:
            print('')
            print(file.read())
    else:
        print("No such a file in: ", CURR_DIR)


def delete_file(name):  # 7 Здесь мы удалим файл
    if os.path.exists(name):
        os.remove(name)
    else:
        print('No such a file in: ', CURR_DIR)


def copy_files(original, target):  # 8 Здесь мы скопируем файл из одной папки в другую
    try:
        shutil.copy(original, target)
    except:
        print('No such a file in: ', CURR_DIR)


def replace_file(original, target):  # 9 Здесь мы изменим директорий файла (на территории основной папки)
    shutil.move(original, target)


def rename_file(old_name, new_name):  # 10 Здесь мы переименуем файл
    shutil.move(old_name, new_name)


while True:
    f = input("Enter command: ")

    if f == 'end':
        break

    elif f == "my_dir":
        print('Your current directory is:', CURR_DIR)
        print('')

    elif f == 'change_dir':
        print('Your current directory is:', CURR_DIR)
        while True:
            directory = input("Input your new directory:")

            if directory == 'end':
                print('Directory successfully changed to:', CURR_DIR)
                break

            if directory.startswith(r"C:\Users\81UJ006KBM\Desktop\FileManager"):
                try:
                    os.chdir(directory)
                    CURR_DIR = os.getcwd()
                    print("Your new directory is:", CURR_DIR)
                except FileNotFoundError:
                    print('File not found!')

    elif f == "create_file":
        file_name = input('Input File Name: ')
        create_file(file_name)

    elif f == "write_to_file":
        directory = input('Where you wanna write something: ')
        text = ''
        while True:
            info = input()
            if info == 'end':
                break
            text += info + '\n'
        write_to_file(directory, text)

    elif f == 'delete_file':
        file_name = input('Input file name to delete: ')
        delete_file(file_name)

    elif f == 'create_folder':
        directory = input('Input folder name: ')
        path = os.path.join(CURR_DIR, directory)
        create_folder(path)

    elif f == 'delete_folder':
        directory = input('Input folder name to delete: ')
        path = os.path.join(CURR_DIR, directory)
        delete_folder(path)

    elif f == 'read_file':
        directory = input('Name a file to read: ')
        read_file(directory)

    elif f == 'replace_file':
        original = input('Witch file you wanna move [full directory name]:')
        target = input('Where you wanna move it [full directory name]: ')
        if target.startswith(r"C:\Users\81UJ006KBM\Desktop\FileManager"):
            replace_file(original, target)
        else:
            print(r'Directoory notin if directory not in C:\Users\81UJ006KBM\Desktop\FileManager')

    elif f == "copy_files":
        original = input('Witch file you wanna move [full directory name]:')
        target = input('Where you wanna move it [full directory name]: ')
        copy_files(original, target)

    elif f == 'replace_folder':
        original = input('Witch folder you wanna move [full directory name]:')
        target = input('Where you wanna move it [full directory name]: ')
        if target.startswith(r"C:\Users\81UJ006KBM\Desktop\FileManager"):
            replace_folder(original, target)
        else:
            print(r'Directoory notin if directory not in C:\Users\81UJ006KBM\Desktop\FileManager')

    elif f == "rename_file":
        original = input('Witch file you wanna rename [full directory name]:')
        target = input('How You wana rename it [full directory name]: ')
        rename_file(original, target)

    elif f == "help":
        print('Possible commands are:')
        print('')
        print(' - '. join(list_of_commands))
        print('')

    else:
        print("There's no such a command")
        print('')
